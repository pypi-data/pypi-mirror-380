"""Extends the builtin Django admin interface for the parent application.

Extends and customizes the site-wide administration utility with
interfaces for managing application database constructs.
"""

import auditlog.admin
import auditlog.models
import django_celery_results.admin
import django_celery_results.models
from django.conf import settings
from django.contrib import admin

from .models import *

settings.JAZZMIN_SETTINGS['icons'].update({
    'logging.AuditLog': 'fa fa-lock',
    'logging.AppLog': 'fa fa-clipboard-list',
    'logging.RequestLog': 'fa fa-exchange-alt',
    'logging.TaskResult': 'fa fa-tasks',
})

settings.JAZZMIN_SETTINGS['order_with_respect_to'].extend([
    'logging.AppLog',
    'logging.RequestLog',
    'django_celery_results.TaskResult',
])

admin.site.unregister(django_celery_results.models.TaskResult)
admin.site.unregister(django_celery_results.models.GroupResult)
admin.site.unregister(auditlog.models.LogEntry)


class ReadOnlyModelAdminMixin:
    """Mixin class for creating model admins with read only permissions."""

    def has_change_permission(self, request, obj=None) -> False:
        """Disable permissions for modifying records."""

        return False

    def has_add_permission(self, request, obj=None) -> False:
        """Disable permissions for creating new records."""

        return False

    def has_delete_permission(self, request, obj=None) -> False:
        """Disable permissions for deleting records."""

        return False


@admin.register(RequestLog)
class RequestLogAdmin(ReadOnlyModelAdminMixin, admin.ModelAdmin):
    """Admin interface for viewing request logs."""

    readonly_fields = [field.name for field in RequestLog._meta.fields]
    list_display = ['timestamp', 'method', 'endpoint', 'response_code', 'remote_address', 'cid']
    search_fields = ['endpoint', 'method', 'response_code', 'remote_address', 'cid']
    ordering = ['-timestamp']
    actions = []
    list_filter = [
        ('timestamp', admin.DateFieldListFilter),
        ('method', admin.AllValuesFieldListFilter),
        ('response_code', admin.AllValuesFieldListFilter),
    ]


@admin.register(TaskResult)
class TaskResultAdmin(ReadOnlyModelAdminMixin, django_celery_results.admin.TaskResultAdmin):
    """Admin interface for viewing Celery task results."""


@admin.register(AuditLog)
class AuditLogAdmin(ReadOnlyModelAdminMixin, auditlog.admin.LogEntryAdmin):
    """Admin interface for viewing Audit log entries."""
