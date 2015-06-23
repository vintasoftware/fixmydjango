from rest_framework import generics

from .filtersets import ExceptionSearchFilter
from .serializers import ErrorPostSerializer
from .models import ErrorPost


class ExceptionSearchAPIView(generics.ListAPIView):
    filter_class = ExceptionSearchFilter
    serializer_class = ErrorPostSerializer

    def get_queryset(self):
        return ErrorPost.publisheds.order_by('-created')
