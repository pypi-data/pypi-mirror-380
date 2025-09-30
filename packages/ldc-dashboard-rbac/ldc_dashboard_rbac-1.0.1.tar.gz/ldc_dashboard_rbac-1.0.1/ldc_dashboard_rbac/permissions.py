"""
Core permission checking logic (without caching)
"""
from typing import Any, Optional, Union
from django.apps import apps
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def get_rbac_config() -> dict:
    """Get RBAC configuration from Django settings"""
    return getattr(settings, 'GROUP_RBAC', {})


def is_superadmin_user(user: Any) -> bool:
    """
    Check if user is superadmin using configured admin check function
    
    Args:
        user: User instance (any model)
    
    Returns:
        bool: True if user is superadmin
    """
    if not user or getattr(user, 'is_anonymous', True):
        return False
    
    try:
        config = get_rbac_config()
        admin_check = config.get('ADMIN_CHECK')
        
        if admin_check and callable(admin_check):
            return admin_check(user)
        
        # Fallback: check common superadmin attributes
        if hasattr(user, 'is_superuser') and user.is_superuser:
            return True
        if hasattr(user, 'role') and user.role in ['super_admin', 'superadmin']:
            return True
        if hasattr(user, 'user_type') and user.user_type in ['super_admin', 'superadmin']:
            return True
            
        return False
        
    except Exception as e:
        logger.error(f"Error checking superadmin status for {user}: {e}")
        return False


def user_has_feature_permission(user: Any, feature_url_name: str, permission_level: str = 'read') -> bool:
    """
    Check if user has permission for a feature (without caching)
    
    Args:
        user: User instance (any model)
        feature_url_name: URL name of the feature
        permission_level: Required permission level
    
    Returns:
        bool: True if user has permission
    """
    if not user or getattr(user, 'is_anonymous', True):
        return False
    
    # ✅ SUPERADMIN BYPASS: Always allow superadmin access
    if is_superadmin_user(user):
        logger.info(f"Superadmin {user} granted access to {feature_url_name}")
        return True
    
    try:
        config = get_rbac_config()
        
        # Get models
        feature_model = apps.get_model(config.get('FEATURE_MODEL', 'dashboard.Feature'))
        group_model = apps.get_model(config.get('GROUP_MODEL', 'dashboard.Group'))
        user_group_model = apps.get_model(config.get('USER_GROUP_MODEL', 'dashboard.UserGroup'))
        permission_model = apps.get_model(config.get('GROUP_FEATURE_PERMISSION_MODEL', 'dashboard.GroupFeaturePermission'))
        
        # Check if feature exists and is active
        try:
            feature = feature_model.objects.get(url_name=feature_url_name, is_active=True)
        except feature_model.DoesNotExist:
            logger.warning(f"Feature '{feature_url_name}' not found or inactive")
            return False
        
        # Get user's active groups
        user_groups = user_group_model.objects.filter(
            user=user,
            is_active=True,
            group__is_active=True
        ).values_list('group_id', flat=True)
        
        if not user_groups:
            return False
        
        # Check permissions (immediate database query, no cache)
        has_permission = permission_model.objects.filter(
            group_id__in=user_groups,
            feature=feature,
            is_enabled=True,
            permission_level__in=get_permission_hierarchy(permission_level)
        ).exists()
        
        return has_permission
        
    except Exception as e:
        logger.error(f"Error checking permission for {user} on {feature_url_name}: {e}")
        return False


def get_permission_hierarchy(level: str) -> list:
    """Get permission hierarchy (admin includes write and read)"""
    hierarchy = {
        'read': ['read', 'write', 'admin'],
        'write': ['write', 'admin'],
        'admin': ['admin']
    }
    return hierarchy.get(level, ['read'])


def get_user_features(user: Any) -> list:
    """Get all features accessible to the user (without caching)"""
    if not user or getattr(user, 'is_anonymous', True):
        return []
    
    # ✅ SUPERADMIN BYPASS: Return all active features for superadmin
    if is_superadmin_user(user):
        try:
            config = get_rbac_config()
            feature_model = apps.get_model(config.get('FEATURE_MODEL', 'dashboard.Feature'))
            return list(feature_model.objects.filter(is_active=True))
        except Exception as e:
            logger.error(f"Error getting all features for superadmin: {e}")
            return []
    
    try:
        config = get_rbac_config()
        feature_model = apps.get_model(config.get('FEATURE_MODEL', 'dashboard.Feature'))
        user_group_model = apps.get_model(config.get('USER_GROUP_MODEL', 'dashboard.UserGroup'))
        permission_model = apps.get_model(config.get('GROUP_FEATURE_PERMISSION_MODEL', 'dashboard.GroupFeaturePermission'))
        
        # Get user's active groups
        user_groups = user_group_model.objects.filter(
            user=user,
            is_active=True,
            group__is_active=True
        ).values_list('group_id', flat=True)
        
        if not user_groups:
            return []
        
        # Get features with permissions (immediate database query)
        feature_ids = permission_model.objects.filter(
            group_id__in=user_groups,
            is_enabled=True,
            feature__is_active=True
        ).values_list('feature_id', flat=True).distinct()
        
        return list(feature_model.objects.filter(id__in=feature_ids))
        
    except Exception as e:
        logger.error(f"Error getting user features: {e}")
        return []


def get_models():
    """
    Get RBAC models dynamically based on configuration
    
    Returns:
        tuple: (User, Feature, Group, UserGroup, GroupFeaturePermission) models
    """
    try:
        config = get_rbac_config()
        
        # Get user model
        user_model_path = config.get('USER_MODEL', 'auth.User')
        user_model = apps.get_model(user_model_path)
        
        # Get RBAC models
        feature_model = apps.get_model(config.get('FEATURE_MODEL', 'dashboard.Feature'))
        group_model = apps.get_model(config.get('GROUP_MODEL', 'dashboard.Group'))
        user_group_model = apps.get_model(config.get('USER_GROUP_MODEL', 'dashboard.UserGroup'))
        permission_model = apps.get_model(config.get('GROUP_FEATURE_PERMISSION_MODEL', 'dashboard.GroupFeaturePermission'))
        
        return user_model, feature_model, group_model, user_group_model, permission_model
        
    except Exception as e:
        logger.error(f"Error getting RBAC models: {e}")
        raise


def get_user_groups(user: Any):
    """
    Get all active groups for a user (without caching)
    
    Args:
        user: User instance (any model)
    
    Returns:
        QuerySet: Active groups for the user
    """
    if not user or getattr(user, 'is_anonymous', True):
        # Return empty queryset
        config = get_rbac_config()
        group_model = apps.get_model(config.get('GROUP_MODEL', 'dashboard.Group'))
        return group_model.objects.none()
    
    # ✅ SUPERADMIN BYPASS: Return all active groups for superadmin
    if is_superadmin_user(user):
        try:
            config = get_rbac_config()
            group_model = apps.get_model(config.get('GROUP_MODEL', 'dashboard.Group'))
            return group_model.objects.filter(is_active=True)
        except Exception as e:
            logger.error(f"Error getting all groups for superadmin: {e}")
            config = get_rbac_config()
            group_model = apps.get_model(config.get('GROUP_MODEL', 'dashboard.Group'))
            return group_model.objects.none()
    
    try:
        config = get_rbac_config()
        group_model = apps.get_model(config.get('GROUP_MODEL', 'dashboard.Group'))
        user_group_model = apps.get_model(config.get('USER_GROUP_MODEL', 'dashboard.UserGroup'))
        
        # Get user's active groups
        group_ids = user_group_model.objects.filter(
            user=user,
            is_active=True,
            group__is_active=True
        ).values_list('group_id', flat=True)
        
        return group_model.objects.filter(id__in=group_ids)
        
    except Exception as e:
        logger.error(f"Error getting user groups: {e}")
        config = get_rbac_config()
        group_model = apps.get_model(config.get('GROUP_MODEL', 'dashboard.Group'))
        return group_model.objects.none()


# Keep these functions for backward compatibility but make them no-ops
def clear_user_permissions_cache(user: Any):
    """No-op function for backward compatibility"""
    pass


def clear_all_rbac_cache():
    """No-op function for backward compatibility"""
    pass