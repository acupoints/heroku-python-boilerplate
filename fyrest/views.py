from django.shortcuts import render
##
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .serializers import GeeksSerializer, NewsContentSerializer
from .models import GeeksModel, NewsContent
##
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class GeeksViewSet(viewsets.ModelViewSet):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksSerializer

class IsReporter(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.reporter == request.user

class NewsContentViewSet(viewsets.ModelViewSet):
    # queryset = NewsContent.objects.all()
    serializer_class = NewsContentSerializer
    permission_classes = (IsReporter,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return NewsContent.objects.filter(reporter=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)
