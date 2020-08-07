"""django_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apis import views as apis_views
## Solve the problem that Django React cannot find /favicon.ico
# from django.contrib.staticfiles.views import serve
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apis_views.hello),
    ## Solve the problem that Django React cannot find /favicon.ico
    # path('favicon.ico', serve, {'path': 'favicon.ico'}),
    # path('logo192.png', serve, {'path': 'logo192.png'}),
    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    # path('logo192.png', RedirectView.as_view(url=staticfiles_storage.url('logo192.png'))),
] 

##
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)