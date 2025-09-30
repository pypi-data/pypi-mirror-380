from django.apps import AppConfig


class LdcDashboardRbacConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ldc_dashboard_rbac'
    verbose_name = 'LDC Dashboard RBAC'
    
    def ready(self):
        """Import signals when Django starts"""
        try:
            from . import signals  # This will register the signal handlers for logging
            import logging
            logger = logging.getLogger(__name__)
            logger.info("RBAC signals loaded (caching disabled for immediate effects)")
        except ImportError as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"Could not load RBAC signals: {e}")