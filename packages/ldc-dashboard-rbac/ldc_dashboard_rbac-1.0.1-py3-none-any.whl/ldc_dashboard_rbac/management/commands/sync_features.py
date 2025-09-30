from django.core.management.base import BaseCommand
from django.conf import settings
from django.apps import apps
from ...permissions import get_rbac_config


class Command(BaseCommand):
    help = 'Sync features from URL patterns'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be created without actually creating',
        )
    
    def handle(self, *args, **options):
        config = get_rbac_config()
        feature_model = apps.get_model(config.get('FEATURE_MODEL', 'dashboard.Feature'))
        
        # Define your features here or auto-discover from URLs
        features_to_create = [
            {
                'name': 'Mandate Management',
                'url_name': 'mandate_details',
                'description': 'Access to mandate management functionality',
                'category': 'Management'
            },
            {
                'name': 'User Management', 
                'url_name': 'user_management',
                'description': 'Access to user management functionality',
                'category': 'Administration'
            },
            {
                'name': 'Feature Management',
                'url_name': 'feature_management', 
                'description': 'Access to feature management functionality',
                'category': 'Administration'
            },
            {
                'name': 'Access Management',
                'url_name': 'access_management',
                'description': 'Access to access management functionality', 
                'category': 'Administration'
            },
        ]
        
        created_count = 0
        updated_count = 0
        
        for feature_data in features_to_create:
            if options['dry_run']:
                self.stdout.write(f"Would create/update: {feature_data['name']}")
                continue
                
            feature, created = feature_model.objects.get_or_create(
                url_name=feature_data['url_name'],
                defaults=feature_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Created feature: {feature.name}")
                )
            else:
                # Update existing feature
                for key, value in feature_data.items():
                    if key != 'url_name':
                        setattr(feature, key, value)
                feature.save()
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f"Updated feature: {feature.name}")
                )
        
        if not options['dry_run']:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully synced features: {created_count} created, {updated_count} updated"
                )
            )