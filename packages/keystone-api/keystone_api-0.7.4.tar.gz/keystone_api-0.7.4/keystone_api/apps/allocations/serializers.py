"""Serializers for casting database models to/from JSON representations.

Serializers handle the casting of database models to/from HTTP compatible
representations in a manner that is suitable for use by RESTful endpoints.
They encapsulate object serialization, data validation, and database object
creation.
"""

from mimetypes import guess_type

from django.conf import settings
from django.core.files.uploadedfile import UploadedFile
from rest_framework import serializers

from apps.logging.nested import AuditLogSummarySerializer
from apps.research_products.nested import *
from apps.users.models import User
from apps.users.nested import *
from .models import *
from .nested import *

__all__ = [
    'AllocationRequestSerializer',
    'AllocationReviewSerializer',
    'AllocationSerializer',
    'AttachmentSerializer',
    'ClusterSerializer',
    'CommentSerializer',
    'JobStatsSerializer',
]


class AllocationRequestSerializer(serializers.ModelSerializer):
    """Object serializer for the `AllocationRequest` class."""

    _submitter = UserSummarySerializer(source='submitter', read_only=True)
    _team = TeamSummarySerializer(source='team', read_only=True)
    _assignees = UserSummarySerializer(source='assignees', many=True, read_only=True)
    _publications = PublicationSummarySerializer(source='publications', many=True, read_only=True)
    _grants = GrantSummarySerializer(source='grants', many=True, read_only=True)
    _history = AuditLogSummarySerializer(source='history', many=True, read_only=True)
    _allocations = AllocationSummarySerializer(source='allocation_set', many=True, read_only=True)
    _comments = CommentSummarySerializer(source='comments', many=True, read_only=True)

    class Meta:
        """Serializer settings."""

        model = AllocationRequest
        fields = '__all__'
        extra_kwargs = {
            'submitted': {'read_only': True},
        }


class AllocationReviewSerializer(serializers.ModelSerializer):
    """Object serializer for the `AllocationReview` class."""

    _request = AllocationRequestSummarySerializer(source='request', read_only=True)
    _reviewer = UserSummarySerializer(source='reviewer', read_only=True)
    _history = AuditLogSummarySerializer(source='history', many=True, read_only=True)

    class Meta:
        """Serializer settings."""

        model = AllocationReview
        fields = '__all__'
        extra_kwargs = {
            'reviewer': {'required': False},  # Default reviewer value is set by the view class
            'submitted': {'read_only': True},
        }

    def validate_reviewer(self, value: User) -> User:
        """Validate the reviewer matches the user submitting the request."""

        if value != self.context['request'].user:
            raise serializers.ValidationError("Reviewer cannot be set to a different user than the submitter")

        return value


class AllocationSerializer(serializers.ModelSerializer):
    """Object serializer for the `Allocation` class."""

    _cluster = ClusterSummarySerializer(source='cluster', read_only=True)
    _request = AllocationRequestSummarySerializer(source='request', read_only=True)
    _history = AuditLogSummarySerializer(source='history', many=True, read_only=True)

    class Meta:
        """Serializer settings."""

        model = Allocation
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    """Object serializer for the `Attachment` class."""

    file = serializers.FileField(use_url=False)
    name = serializers.CharField(required=False)
    _request = AllocationRequestSummarySerializer(source='request', read_only=True)
    _history = AuditLogSummarySerializer(source='history', many=True, read_only=True)

    class Meta:
        """Serializer settings."""

        model = Attachment
        fields = '__all__'

    @staticmethod
    def validate_file(value: UploadedFile) -> UploadedFile:
        """Validate the uploaded file against size and type constraints.

        Returns:
            The validated file.

        Raises:
            serializers.ValidationError: If the file exceeds the size limit or has a disallowed MIME type.
        """

        max_size = settings.MAX_FILE_SIZE
        if value.size > max_size:
            limit_in_mb = max_size / (1024 * 1024)
            raise serializers.ValidationError(f"File size should not exceed {limit_in_mb:.2f} MB.")

        allowed_types = settings.ALLOWED_FILE_TYPES
        mime_type, _ = guess_type(value.name)
        if mime_type not in allowed_types:
            raise serializers.ValidationError(f"File type '{mime_type}' is not allowed.")

        return value


class ClusterSerializer(serializers.ModelSerializer):
    """Object serializer for the `Cluster` class."""

    _history = AuditLogSummarySerializer(source='history', many=True, read_only=True)

    class Meta:
        """Serializer settings."""

        model = Cluster
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Object serializer for the `Comment` class."""

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    _user = UserSummarySerializer(source='user', read_only=True)
    _request = AllocationRequestSummarySerializer(source='request', read_only=True)
    _history = AuditLogSummarySerializer(source='history', many=True, read_only=True)

    class Meta:
        """Serializer settings."""

        model = Comment
        fields = '__all__'

    def validate(self, attrs: dict) -> dict:
        """Limit modification of the `private` field to staff users.

        Args:
            attrs: The record attributes to validate.

        Returns:
            The validated attributes.
        """

        request = self.context.get('request')
        user = getattr(request, 'user', None)

        # Determine if the comment is or will be private
        private_value = attrs.get('private', False)
        if self.instance:
            private_value = self.instance.private or private_value

        # Reject if private is true and user is not staff
        if private_value and (not user or not user.is_staff):
            raise serializers.ValidationError({
                'private': 'Only staff users can write comments marked as private.'
            })

        return attrs


class JobStatsSerializer(serializers.ModelSerializer):
    """Object serializer for the `JobStats` class."""

    _team = TeamSummarySerializer(source='team', read_only=True)
    _cluster = ClusterSummarySerializer(source='cluster', read_only=True)

    class Meta:
        """Serializer settings."""

        model = JobStats
        fields = '__all__'
        read_only = ['team']
