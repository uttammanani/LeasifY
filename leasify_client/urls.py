from django.contrib import admin
from django.urls import path
from leasify_client import client_views
import leasify_client

urlpatterns = [
<<<<<<< HEAD
    path('register/', client_views.register),
    path('log/', client_views.login),
    path('home/', client_views.home),
    path('checkout/', client_views.checkout),
    path('user_profile/', client_views.user_profile),
    path('about_us/', client_views.about_us),
    path('blog/', client_views.blog),
    path('contact_us/', client_views.contact_us),
    path('setpass/', client_views.setpassword),
    path('forgot/', client_views.forgot),
    path('sendotp/', client_views.otp),
    path('verify_otp/', client_views.verify_otp),
    path('properties/', client_views.properties_grid),
    path('home_details/', client_views.home_details),
    path('pg1_details/', client_views.pg1_details),
    path('home_desc/<int:id>', client_views.home_desc),
    path('pg_desc/<int:id>', client_views.pg_desc),
    path('mybookings/',client_views.mybookings),
=======
    path('home/',client_views.home),
    path('log/',client_views.login),
    path('dashboard/',client_views.dashboard),
    path('checkout/',client_views.checkout),
    path('user_profile/',client_views.user_profile),
    path('about_us/',client_views.about_us),
    path('blog/',client_views.blog),
    path('contact_us/',client_views.contact_us),
    path('setpass/',client_views.setpassword),
    path('forgot/',client_views.forgot),
    path('sendotp/',client_views.otp),
    path('verify_otp/',client_views.verify_otp),
    # path('about_us',client_views.about_us),
>>>>>>> 3ea18f51104c009cb8c55edc4bffa6e27e4e045f
]
