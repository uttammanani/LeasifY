import sys
import random
from datetime import date

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from leasify_admin.models import customer
from django.core.mail import send_mail
from leasify import settings
from leasify_admin.forms import customer_form


# from leasify_admin.forms import Userform

# Create your views here.
def home(request):
    if request.method == "POST":
        form = customer_form(request.POST)
        print("=======REGISTER", form)
        print("-------------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cust_table/')
            except:
                print("---------------", sys.exc_info())

    else:
        form = customer_form()

    return render(request, 'client_home.html', {'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        val = customer.objects.filter(c_email=email, c_pass=password, c_is_admin=0).count()
        print("-------------------", email, "-----------------", password, val)
        if val == 1:
            print("=====INSIDE IFFFFF")
            udata = customer.objects.filter(c_email=email, c_pass=password, c_is_admin=0)
            for item in udata:
                request.session['client_email'] = item.c_email
                request.session['client_pass'] = item.c_pass
                request.session['client_id'] = item.c_id
                if request.POST.get("remember"):
                    print("==INSIDE COOKIEEEEEE=", )
                    response = redirect("/Client/deshbored/")
                    response.set_cookie('cookie_client_email', request.POST["email"], 3600 * 24 * 365 * 2)
                    response.set_cookie('cookie_client_password', request.POST["pass"], 3600 * 24 * 365 * 2)
                    return response
            return redirect('/Client/deshbored/')

        else:
            messages.error("invalid password")
            return redirect('/cust_table/')
    else:
        if request.COOKIES.get("cookie_client_email"):
            return render(request, "client_login.html",
                          {'client_email': request.COOKIES['cookie_client_email'],
                           'client_password': request.COOKIES[
                               'cookie_client_password']})
        else:
            return render(request, 'client_login.html')


def deshboard(request):
    return render(request, 'client_deshbord.html')


def checkout(request):
    return render(request, 'client_checkout.html')


def user_profile(request):
    return render(request, 'client_user-profile.html')


def about_us(request):
    return render(request, 'client_about.html')


def blog(request):
    return render(request, 'client_blog.html')


def contact_us(request):
    return render(request, 'client_contact-us.html')


def setpassword(request):
    if request.method == "POST":
        T_pass = request.POST['pass']
        T_cpass = request.POST['cpass']

        if T_pass == T_cpass:
            e = request.session['temail']
            val = customer.objects.filter(c_email=e, otp_used=0).count()

            if val == 1:
                customer.objects.filter(c_email=e).update(otp_used=1, c_pass=T_pass)
                return redirect("/Client/log/")
            else:
                messages.error(request, "Invalid OTP")
                return render(request, "client_forgot.html")

        else:
            messages.error(request, "New password and Confirm password does not match ")
            return render(request, "client_setpass.html")

    else:
        return redirect("/Client/forgot/")




def forgot(request):
    return render(request, 'client_forgot.html')


def otp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['email']
    request.session['temail'] = e
    obj = customer.objects.filter(c_email=e).count()

    if obj == 1:
        val = customer.objects.filter(c_email=e).update(otp=otp1, otp_used=0)
        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'client_otp.html')

def verify_otp(request):
    if request.method == "POST":
        T_otp = request.POST['otpv']
        var = customer.objects.filter(otp=T_otp, otp_used=0).count()
        if var == 1:
            return render(request, 'client_setpass.html')
        else:
            messages.error(request, "Invalid OTP")
            return render(request, "client_forgot.html")
    else:
        return render(request, "client_otp.html")
