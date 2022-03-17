from django.contrib import admin
from django.urls import path
from leasify_client import client_views

urlpatterns = [
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
    path('verify_otp/',client_views.verify_otp)
]
