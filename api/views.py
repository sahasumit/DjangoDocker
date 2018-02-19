from api.models import *
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.utils import timezone
from rest_framework import generics
from django.db.models import Q
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt


class SnippetList(generics.ListCreateAPIView):
    now=  timezone.now() - timedelta(minutes=5)
    queryset = Store.objects.filter(Q(date_modified__gte=now))
    serializer_class = StoreSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    now=  timezone.now() - timedelta(minutes=5)
    queryset = Store.objects.filter(Q(date_modified__gte=now))
    serializer_class = StoreSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
