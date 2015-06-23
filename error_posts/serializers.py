from rest_framework import serializers

from .models import ErrorPost


class ErrorPostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='error_posts:detail',
        lookup_field='pk')

    class Meta:
        model = ErrorPost
        fields = ('id', 'url', 'exception_type', 'error_message',
                  'raised_by', 'raised_by_line', 'django_version')
