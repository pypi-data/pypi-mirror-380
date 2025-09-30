"""
Utility functions for group RBAC
"""
from django.core.cache import cache
from django.conf import settings
from django.apps import apps
from django.utils import timezone
from .permissions import clear_user_permissions_cache
import logging

logger = logging.getLogger(__name__)


def sync_features_from_urls():
    """
    Synchronize features from Django URL patterns
    
    This function scans all URL patterns and creates Feature objects
    for any named URLs that don't already exist.
    """
    from django.urls import get_resolver
    from .permissions import get_models
    
    try:
        User, Feature, Group, UserGroup, GroupFeaturePermission = get_models()
        
        resolver = get_resolver()
        created_count = 0
        
        def extract_url_names(url_patterns, namespace=''):
            """Recursively extract URL names from patterns"""
            names = []
            for pattern in url_patterns:
                if hasattr(pattern, 'name') and pattern.name:
                    full_name = f"{namespace}:{pattern.name}" if namespace else pattern.name
                    names.append(full_name)
                elif hasattr(pattern, 'url_patterns'):
                    # Handle included URL patterns
                    pattern_namespace = getattr(pattern, 'namespace', '')
                    if pattern_namespace:
                        pattern_namespace = f"{namespace}:{pattern_namespace}" if namespace else pattern_namespace
                    names.extend(extract_url_names(pattern.url_patterns, pattern_namespace))
            return names
        
        url_names = extract_url_names(resolver.url_patterns)
        
        for url_name in url_names:
            if not Feature.objects.filter(url_name=url_name).exists():
                # Create a human-readable name from URL name
                display_name = url_name.replace('_', ' ').replace(':', ' - ').title()
                
                Feature.objects.create(
                    name=display_name,
                    url_name=url_name,
                    description=f"Auto-generated feature for {url_name}",
                    is_active=False  # Start as inactive for security
                )
                created_count += 1
                logger.info(f"Created feature: {display_name} ({url_name})")
        
        logger.info(f"Feature sync completed. Created {created_count} new features.")
        return created_count
        
    except Exception as e:
        logger.error(f"Error syncing features from URLs: {e}")
        raise


def clear_all_permission_cache():
    """Clear all RBAC permission cache"""
    try:
        # This is a simplified approach
        # In production, consider using cache tagging for more efficient clearing
        cache.clear()
        logger.info("All RBAC permission cache cleared")
    except Exception as e:
        logger.error(f"Error clearing permission cache: {e}")


def get_user_permission_summary(user):
    """
    Get a summary of user's permissions
    
    Returns a dictionary with user's groups, features, and permission levels
    """
    from .permissions import get_models, get_user_features, get_user_groups
    
    try:
        User, Feature, Group, UserGroup, GroupFeaturePermission = get_models()
        
        if not user or user.is_anonymous:
            return {
                'groups': [],
                'features': [],
                'total_groups': 0,
                'total_features': 0,
                'permission_levels': {}
            }
        
        groups = get_user_groups(user)
        features = get_user_features(user)
        
        # Get permission levels for each feature
        permission_levels = {}
        permissions = GroupFeaturePermission.objects.filter(
            group__user_memberships__user=user,
            group__user_memberships__is_active=True,
            group__is_active=True,
            is_enabled=True
        ).select_related('feature')
        
        for perm in permissions:
            feature_name = perm.feature.url_name
            current_level = permission_levels.get(feature_name, 'read')
            
            # Keep the highest permission level
            level_hierarchy = {'read': 1, 'write': 2, 'admin': 3}
            if level_hierarchy.get(perm.permission_level, 1) > level_hierarchy.get(current_level, 1):
                permission_levels[feature_name] = perm.permission_level
        
        return {
            'groups': list(groups.values('id', 'name', 'description')),
            'features': list(features.values('id', 'name', 'url_name', 'category')),
            'total_groups': groups.count(),
            'total_features': features.count(),
            'permission_levels': permission_levels
        }
        
    except Exception as e:
        logger.error(f"Error getting user permission summary: {e}")
        return {
            'groups': [],
            'features': [],
            'total_groups': 0,
            'total_features': 0,
            'permission_levels': {}
        }


def validate_rbac_configuration():
    """
    Validate RBAC configuration and return any issues
    
    Returns a list of configuration issues or empty list if valid
    """
    issues = []
    
    try:
        config = getattr(settings, 'GROUP_RBAC', {})
        
        # Check required configuration
        if not config.get('USER_GETTER'):
            issues.append("GROUP_RBAC['USER_GETTER'] is not configured")
        
        if not config.get('SUPER_ADMIN_CHECK'):
            issues.append("GROUP_RBAC['SUPER_ADMIN_CHECK'] is not configured")
        
        if not config.get('ADMIN_CHECK'):
            issues.append("GROUP_RBAC['ADMIN_CHECK'] is not configured")
        
        # Check if models exist
        try:
            from .permissions import get_models
            get_models()
        except Exception as e:
            issues.append(f"Error loading RBAC models: {e}")
        
        # Check if user getter function is callable
        user_getter = config.get('USER_GETTER')
        if user_getter and not callable(user_getter):
            issues.append("GROUP_RBAC['USER_GETTER'] is not callable")
        
        # Check if admin check functions are callable
        super_admin_check = config.get('SUPER_ADMIN_CHECK')
        if super_admin_check and not callable(super_admin_check):
            issues.append("GROUP_RBAC['SUPER_ADMIN_CHECK'] is not callable")
        
        admin_check = config.get('ADMIN_CHECK')
        if admin_check and not callable(admin_check):
            issues.append("GROUP_RBAC['ADMIN_CHECK'] is not callable")
        
    except Exception as e:
        issues.append(f"Error validating RBAC configuration: {e}")
    
    return issues


def export_rbac_configuration():
    """
    Export current RBAC configuration for backup or migration
    
    Returns a dictionary with all groups, features, and permissions
    """
    from .permissions import get_models
    
    try:
        User, Feature, Group, UserGroup, GroupFeaturePermission = get_models()
        
        # Export features
        features = list(Feature.objects.values(
            'name', 'url_name', 'description', 'category', 'is_active'
        ))
        
        # Export groups
        groups = list(Group.objects.values(
            'name', 'description', 'is_active'
        ))
        
        # Export permissions
        permissions = list(GroupFeaturePermission.objects.select_related(
            'group', 'feature'
        ).values(
            'group__name', 'feature__url_name', 'permission_level', 'is_enabled'
        ))
        
        # Export user-group memberships
        user_groups = list(UserGroup.objects.select_related(
            'user', 'group'
        ).values(
            'user__username', 'group__name', 'role', 'is_active'
        ))
        
        return {
            'features': features,
            'groups': groups,
            'permissions': permissions,
            'user_groups': user_groups,
            'export_timestamp': timezone.now().isoformat(),
            'version': '1.0'
        }
        
    except Exception as e:
        logger.error(f"Error exporting RBAC configuration: {e}")
        raise


def import_rbac_configuration(config_data):
    """
    Import RBAC configuration from exported data
    
    Args:
        config_data: Dictionary from export_rbac_configuration()
        
    Returns:
        Dictionary with import statistics
    """
    from .permissions import get_models
    from django.contrib.auth import get_user_model
    from django.db import transaction
    
    try:
        User, Feature, Group, UserGroup, GroupFeaturePermission = get_models()
        UserModel = get_user_model()
        
        stats = {
            'features_created': 0,
            'groups_created': 0,
            'permissions_created': 0,
            'user_groups_created': 0,
            'errors': []
        }
        
        with transaction.atomic():
            # Import features
            for feature_data in config_data.get('features', []):
                feature, created = Feature.objects.get_or_create(
                    url_name=feature_data['url_name'],
                    defaults=feature_data
                )
                if created:
                    stats['features_created'] += 1
            
            # Import groups
            for group_data in config_data.get('groups', []):
                group, created = Group.objects.get_or_create(
                    name=group_data['name'],
                    defaults=group_data
                )
                if created:
                    stats['groups_created'] += 1
            
            # Import permissions
            for perm_data in config_data.get('permissions', []):
                try:
                    group = Group.objects.get(name=perm_data['group__name'])
                    feature = Feature.objects.get(url_name=perm_data['feature__url_name'])
                    
                    permission, created = GroupFeaturePermission.objects.get_or_create(
                        group=group,
                        feature=feature,
                        defaults={
                            'permission_level': perm_data['permission_level'],
                            'is_enabled': perm_data['is_enabled']
                        }
                    )
                    if created:
                        stats['permissions_created'] += 1
                        
                except (Group.DoesNotExist, Feature.DoesNotExist) as e:
                    stats['errors'].append(f"Permission import error: {e}")
            
            # Import user-group memberships
            for ug_data in config_data.get('user_groups', []):
                try:
                    user = UserModel.objects.get(username=ug_data['user__username'])
                    group = Group.objects.get(name=ug_data['group__name'])
                    
                    user_group, created = UserGroup.objects.get_or_create(
                        user=user,
                        group=group,
                        defaults={
                            'role': ug_data['role'],
                            'is_active': ug_data['is_active']
                        }
                    )
                    if created:
                        stats['user_groups_created'] += 1
                        
                except (UserModel.DoesNotExist, Group.DoesNotExist) as e:
                    stats['errors'].append(f"User-group import error: {e}")
        
        logger.info(f"RBAC configuration imported successfully: {stats}")
        return stats
        
    except Exception as e:
        logger.error(f"Error importing RBAC configuration: {e}")
        raise