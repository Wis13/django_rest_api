from django.urls import path

from . import views

# from


urlpatterns = [
    path('', views.api_home)
]
