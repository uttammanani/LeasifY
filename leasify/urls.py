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
from django.urls import path, include
from leasify_client import urls
import leasify_client
from leasify_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.show),
    path('load/', views.loadadmin),
    path('cust_table/', views.cust_table),
    path('owner_table/', views.owner_table),
    path('house_details_table/', views.house_details_table),
    path('area_table/', views.area_table),
    path('house_gallery_table/', views.house_gallery_table),
    path('pg_details_table/', views.pg_details_table),
    path('pg_gallery_table/', views.pg_gallery_table),
    path('tiffin_owner_table/', views.tiffi_owner_table),
    path('tiffin_details_table/', views.tiffin_details_table),
    path('status_table/', views.status_table),
    path('notification_table/', views.notification_table),
    path('feedback_table/', views.feedback_table),
    path('insert_house_details/', views.insert_house_details),
    path('insert_owner/', views.insert_owner_details),
    path('insert_area/', views.insert_area),
    path('insert_pg_details/', views.insert_pg_details),
    path('insert_tiffin_owner/', views.insert_tiffin_owner_details),
    path('insert_tiffin_details/', views.insert_tiffin_details),
    path('insert_house_gallery/', views.insert_house_gallery),
    path('insert_pg_gallery/', views.insert_pg_gallery),
    path('del_area/<int:id>', views.del_area),
    path('del_house_details/<int:id>', views.del_house_details),
    path('del_tiffin_details/<int:id>', views.del_tiffin_details),
    path('del_house_gallery/<int:id>', views.del_house_gallery),
    path('del_owner/<int:id>', views.del_owner),
    path('del_pg_details/<int:id>', views.del_pg_details),
    path('del_pg_gallery/<int:id>', views.del_pg_gallery),
    path('del_tiffin_owner/<int:id>', views.del_tiffin_owner),
    path('update_area/<int:id>', views.update_area),
    path('update_house_details/<int:id>', views.update_house_details),
    path('update_house_gallery/<int:id>', views.update_house_gallery),
    path('update_owner/<int:id>', views.update_owner),
    path('update_pg_details/<int:id>', views.update_pg_details),
    path('update_pg_gallery/<int:id>', views.update_pg_gallery),
    path('update_tiffin_details/<int:id>', views.update_tiffin_details),
    path('update_tiffin_owner/<int:id>', views.update_tiffin_owner),
    path('update_admin/', views.update_admin),
    path('admin_login/', views.admin_login),
    path('forgot_password/', views.forgot_pass),
    path('send_otp/', views.send_otp),
    path('reset/', views.set_password),
    path('index/', views.index),
    path('Client/', include('leasify_client.urls')),
]
