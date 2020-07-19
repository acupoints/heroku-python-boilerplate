from django.urls import path
from apis import views as apis_views

##

urlpatterns = [
    path('', apis_views.hello)
]
