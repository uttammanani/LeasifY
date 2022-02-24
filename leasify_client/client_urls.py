from leasify_client import client_views
from django.urls import path

urlpatterns = [
    path('home/', client_views.loadhome),
    ]