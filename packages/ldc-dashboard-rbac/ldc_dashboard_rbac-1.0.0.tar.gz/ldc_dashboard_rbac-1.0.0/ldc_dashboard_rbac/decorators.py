"""
Decorators for feature-based access control
"""
from functools import wraps
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .permissions import user_has_feature_permission, get_rbac_config, is_superadmin_user
import logging

logger = logging.getLogger(__name__)


def _is_api_request(request):
    """
    Improved detection for API requests.
    Returns True if the request appears to be from an API client.
    """
    # Check for common API indicators
    content_type = request.headers.get('Content-Type', '').lower()
    accept = request.headers.get('Accept', '').lower()
    
    # Common API request patterns
    api_indicators = [
        # AJAX requests
        request.headers.get('X-Requested-With') == 'XMLHttpRequest',
        # JSON content type
        'application/json' in content_type,
        # API-specific accept headers
        'application/json' in accept,
        'application/vnd.api+json' in accept,
        # DRF browsable API
        'text/html' not in accept or 'application/json' in accept,
        # Common API user agents (partial matches)
        any(agent in request.headers.get('User-Agent', '').lower() 
            for agent in ['postman', 'insomnia', 'curl', 'python-requests', 'axios']),
        # API path patterns (customize these based on your URL structure)
        '/api/' in request.path.lower(),
    ]
    
    return any(api_indicators)


def _handle_permission_denied(request, error_message, feature_url_name=None, permission_level=None, status_code=403):
    """
    Handle permission denied responses for both web and API requests.
    """
    if _is_api_request(request):
        response_data = {'error': error_message}
        if feature_url_name:
            response_data['feature'] = feature_url_name
        if permission_level:
            response_data['required_permission'] = permission_level
        
        return JsonResponse(response_data, status=status_code)
    
    # Web request - return HTML page
    context = {'error': error_message}
    if feature_url_name:
        context['feature'] = feature_url_name
    if permission_level:
        context['required_permission'] = permission_level
    
    return render(request, 'ldc_dashboard_rbac/permission_denied.html', context, status=status_code)


def feature_required(feature_url_name: str, permission_level: str = 'read'):
    """
    Decorator to check if user has permission for a specific feature.
    Works with both Django views and API endpoints.
    
    Usage:
        @feature_required('user_management')
        def my_view(request):
            pass
            
        @feature_required('user_management', 'write')
        def my_api_view(request):
            pass
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            config = get_rbac_config()
            user_getter = config.get('USER_GETTER')
            
            if not user_getter:
                logger.error("USER_GETTER not configured in GROUP_RBAC settings")
                return _handle_permission_denied(
                    request, 
                    'Access control not configured',
                    status_code=500
                )
            
            user = user_getter(request)
            
            # ✅ SUPERADMIN BYPASS: Always allow superadmin access
            if is_superadmin_user(user):
                logger.info(f"Superadmin {user} granted access to {feature_url_name} via decorator")
                return view_func(request, *args, **kwargs)
            
            # Regular permission check
            if not user_has_feature_permission(user, feature_url_name, permission_level):
                return _handle_permission_denied(
                    request,
                    "You don't have permission to access this feature.",
                    feature_url_name,
                    permission_level
                )
            
            return view_func(request, *args, **kwargs)
        
        return _wrapped_view
    return decorator


def admin_required(view_func=None):
    """
    Decorator to check if user is superadmin.
    Works with both Django views and API endpoints.
    
    Usage:
        @admin_required
        def my_admin_view(request):
            pass
    """
    def decorator(func):
        @wraps(func)
        def _wrapped_view(request, *args, **kwargs):
            config = get_rbac_config()
            user_getter = config.get('USER_GETTER')
            
            if not user_getter:
                logger.error("USER_GETTER not configured in GROUP_RBAC settings")
                return _handle_permission_denied(
                    request,
                    'Access control not configured',
                    status_code=500
                )
            
            user = user_getter(request)
            
            if not is_superadmin_user(user):
                return _handle_permission_denied(
                    request,
                    "You don't have admin permission to access this feature."
                )
            
            return func(request, *args, **kwargs)
        
        return _wrapped_view
    
    if view_func:
        return decorator(view_func)
    return decorator


# Alias for backward compatibility
feature_permission_required = feature_required