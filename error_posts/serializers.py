import urllib

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import ErrorPost, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'message')


class ErrorPostSearchSerializer(serializers.ListSerializer):

    def _get_list_url(self, request):
        return "{url}?{query}".format(
            url=reverse('error_posts:list', request=request),
            query=urllib.parse.urlencode(request.GET))

    def to_representation(self, data):
        error_post_list = super(ErrorPostSearchSerializer, self).to_representation(data)
        return {
            'error_post_list': error_post_list,
            'list_url': self._get_list_url(self.context['request'])
        }

    @property
    def data(self):
        # yes we want ListSerializer super, which is BaseSerializer
        return super(serializers.ListSerializer, self).data


class ErrorPostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='error_posts:detail',
        lookup_field='slug')
    answers = AnswerSerializer(many=True)

    class Meta:
        model = ErrorPost
        fields = ('id', 'url', 'exception_type', 'error_message',
                  'raised_by', 'raised_by_line', 'django_version',
                  'answers')
        list_serializer_class = ErrorPostSearchSerializer
