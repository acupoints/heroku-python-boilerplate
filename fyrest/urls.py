from django.urls import path, include
from rest_framework import routers
from . import views as fyrest_views

##
router = routers.DefaultRouter()
router.register(r'geeks', fyrest_views.GeeksViewSet, basename='geeks')
router.register(r'news-content', fyrest_views.NewsContentViewSet, basename='news_content')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('hello/', fyrest_views.HelloView.as_view(), name='hello'),
]
