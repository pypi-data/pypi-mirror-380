"""
Management command to show RBAC status and configuration
"""
from django.core.management.base import BaseCommand
from django.conf import settings
from ...utils import validate_rbac_configuration, get_user_permission_summary
from ...permissions import get_models
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Show RBAC status and configuration'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--user',
            type=str,
            help='Show permissions for a specific user (username)',
        )
        
        parser.add_argument(
            '--validate',
            action='store_true',
            help='Validate RBAC configuration',
        )
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== GROUP RBAC STATUS ===\n'))
        
        # Validate configuration if requested
        if options['validate']:
            self.stdout.write(self.style.HTTP_INFO('Configuration Validation:'))
            issues = validate_rbac_configuration()
            if issues:
                for issue in issues:
                    self.stdout.write(self.style.ERROR(f'  ❌ {issue}'))
            else:
                self.stdout.write(self.style.SUCCESS('  ✅ Configuration is valid'))
            self.stdout.write('')
        
        try:
            User, Feature, Group, UserGroup, GroupFeaturePermission = get_models()
            
            # Show statistics
            self.stdout.write(self.style.HTTP_INFO('Statistics:'))
            self.stdout.write(f'  Features: {Feature.objects.count()} total, {Feature.objects.filter(is_active=True).count()} active')
            self.stdout.write(f'  Groups: {Group.objects.count()} total, {Group.objects.filter(is_active=True).count()} active')
            self.stdout.write(f'  Permissions: {GroupFeaturePermission.objects.count()} total, {GroupFeaturePermission.objects.filter(is_enabled=True).count()} enabled')
            self.stdout.write(f'  User-Group Memberships: {UserGroup.objects.count()} total, {UserGroup.objects.filter(is_active=True).count()} active')
            self.stdout.write('')
            
            # Show feature categories
            categories = Feature.objects.values_list('category', flat=True).distinct().exclude(category__isnull=True).exclude(category='')
            if categories:
                self.stdout.write(self.style.HTTP_INFO('Feature Categories:'))
                for category in sorted(categories):
                    count = Feature.objects.filter(category=category).count()
                    self.stdout.write(f'  {category}: {count} features')
                self.stdout.write('')
            
            # Show user permissions if requested
            if options['user']:
                UserModel = get_user_model()
                try:
                    user = UserModel.objects.get(username=options['user'])
                    self.show_user_permissions(user)
                except UserModel.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'User "{options["user"]}" not found'))
            
            # Show configuration
            config = getattr(settings, 'GROUP_RBAC', {})
            self.stdout.write(self.style.HTTP_INFO('Configuration:'))
            self.stdout.write(f'  USER_MODEL: {config.get("USER_MODEL", "Not set")}')
            self.stdout.write(f'  FEATURE_MODEL: {config.get("FEATURE_MODEL", "ldc_dashboard_rbac.Feature")}')
            self.stdout.write(f'  GROUP_MODEL: {config.get("GROUP_MODEL", "ldc_dashboard_rbac.Group")}')
            self.stdout.write(f'  USER_GETTER: {"✅ Set" if config.get("USER_GETTER") else "❌ Not set"}')
            self.stdout.write(f'  SUPER_ADMIN_CHECK: {"✅ Set" if config.get("SUPER_ADMIN_CHECK") else "❌ Not set"}')
            self.stdout.write(f'  ADMIN_CHECK: {"✅ Set" if config.get("ADMIN_CHECK") else "❌ Not set"}')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error getting RBAC status: {e}'))
    
    def show_user_permissions(self, user):
        """Show detailed permissions for a specific user"""
        self.stdout.write(self.style.HTTP_INFO(f'User Permissions for "{user.username}":'))
        
        summary = get_user_permission_summary(user)
        
        self.stdout.write(f'  Groups ({summary["total_groups"]}):')
        for group in summary['groups']:
            self.stdout.write(f'    - {group["name"]}')
        
        self.stdout.write(f'  Features ({summary["total_features"]}):')
        for feature in summary['features']:
            permission_level = summary['permission_levels'].get(feature['url_name'], 'read')
            category = f" [{feature['category']}]" if feature['category'] else ""
            self.stdout.write(f'    - {feature["name"]} ({permission_level}){category}')
        
        self.stdout.write('')