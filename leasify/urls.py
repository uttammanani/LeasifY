"""leasify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from leasify_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/',views.show),
    path('load/',views.loadadmin),
    path('cust_table/',views.cust_table),
    path('owner_table/',views.owner_table),
    path('house_details_table/',views.house_details_table),
    path('area_table/',views.area_table),
    path('house_gallery_table/',views.house_gallery_table),
    path('pg_details_table/',views.pg_details_table),
    path('pg_gallery_table/',views.pg_gallery_table),
    path('tiffin_owner_table/',views.tiffi_owner_table),
    path('tiffin_details_table/',views.tiffin_details_table),
    path('status_table/',views.status_table),
    path('notification_table/',views.notification_table),
    path('feedback_table/',views.feedback_table),
    path('insert_house_details/',views.insert_house_details),
    path('insert_owner/',views.insert_owner_details)


]
