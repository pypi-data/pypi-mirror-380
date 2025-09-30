"""
Django Feature RBAC - Group-based Role-Based Access Control
"""

# Core permission functions
from .permissions import (
    user_has_feature_permission,
    get_user_features,
    is_superadmin_user,
    get_rbac_config,
)

# Decorators for Django views
from .decorators import (
    feature_required,
    feature_permission_required,  # alias for backward compatibility
    admin_required,
)

# DRF Permission Classes (with graceful import handling)
try:
    from .drf_permissions import (
        HasFeaturePermission,
        IsFeatureAdmin,
        DynamicFeaturePermission,
    )
    __all_drf__ = [
        'HasFeaturePermission',
        'IsFeatureAdmin', 
        'DynamicFeaturePermission'
    ]
except ImportError:
    # Django Rest Framework not installed
    __all_drf__ = []

# Abstract models
from .models import (
    AbstractFeature,
    AbstractGroup,
    AbstractGroupFeaturePermission,
    AbstractUserGroup,
)

__version__ = '1.0.0'

__all__ = [
    # Core functions
    'user_has_feature_permission',
    'get_user_features',
    'is_superadmin_user',
    'get_rbac_config',
    
    # Decorators
    'feature_required',
    'feature_permission_required',
    'admin_required',
    
    # Abstract models
    'AbstractFeature',
    'AbstractGroup',
    'AbstractGroupFeaturePermission',
    'AbstractUserGroup',
] + __all_drf__