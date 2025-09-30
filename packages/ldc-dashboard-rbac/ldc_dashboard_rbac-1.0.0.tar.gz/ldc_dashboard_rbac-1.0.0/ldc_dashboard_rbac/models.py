"""
Abstract models for feature-based RBAC system
"""
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class AbstractFeature(models.Model):
    """Abstract base model for features"""
    name = models.CharField(max_length=100, unique=True)
    url_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True


class AbstractGroup(models.Model):
    """Abstract base model for groups"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True


class AbstractGroupFeaturePermission(models.Model):
    """Abstract base model for group-feature permissions"""
    is_enabled = models.BooleanField(default=True)
    permission_level = models.CharField(
        max_length=20,
        choices=[
            ('read', 'Read Only'),
            ('write', 'Read & Write'),
            ('admin', 'Full Admin'),
        ],
        default='read'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class AbstractUserGroup(models.Model):
    """Abstract base model for user-group relationships"""
    is_active = models.BooleanField(default=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('member', 'Member'),
            ('admin', 'Group Admin'),
        ],
        default='member'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True