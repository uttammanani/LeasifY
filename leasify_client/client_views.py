import sys
import random
from datetime import date

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from leasify_admin.function import handle_uploaded_file
from leasify_admin.models import customer, tiffin_details, owner, tiffin_owner, area
from django.core.mail import send_mail
from leasify import settings
# from leasify_admin.models import Booking
from leasify_admin.forms import customer_form, house_details, pg_details, owner_form, tiffin_owner_form, \
    house_details_form, pg_details_form, tiffin_details_form


# from leasify_admin.forms import Userform

# Create your views here.
def register(request):
    if request.method == "POST":
        c_form = customer_form(request.POST)
        if c_form.is_valid():
            try:
                c_form.save()
                return redirect('/Client/log/')
            except:
                print("---------------", sys.exc_info())

    else:
        form = customer_form()
    return render(request, 'client_registration.html', {'form': form})


def t_register(request):
    if request.method == "POST":
        t_form = tiffin_owner_form(request.POST)
        if t_form.is_valid():
            try:
                t_form.save()
                return redirect('/Client/log/')
            except:
                print("---------------", sys.exc_info())

    else:
        form = tiffin_owner_form()
    return render(request, 'client_t_registration.html', {'form': form})


def o_register(request):
    if request.method == "POST":
        t_form = owner_form(request.POST)
        if t_form.is_valid():
            try:
                t_form.save()
                return redirect('/Client/log/')
            except:
                print("---------------", sys.exc_info())

    else:
        form = owner_form()
    return render(request, 'client_o_registration.html', {'form': form})



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        radd=request.POST['rad']
        #print(email,password,radd)
        if radd=='c':
            val = customer.objects.filter(c_email=email, c_pass=password).count()

            if val ==1:
                obj = customer.objects.get(c_email=email)
                request.session['cust_id']=email
                request.session['name']=obj.c_name
                print("_____________________________", request.session['cust_id'])
                return redirect('/Client/home')
            else:
                return redirect('/Client/log/')

        elif radd=='h':
            val = owner.objects.filter(o_email=email, o_pass=password).count()
            if val ==1:
                obj = owner.objects.get(o_email=email)
                request.session['owner_id']=email
                request.session['type'] = obj.o_type
                request.session['name'] = obj.o_name


                print("_____________________________", request.session['owner_id'])
                return redirect('/Client/home')
            else:
                return redirect('/Client/log/')

        elif radd=='t':
            val = tiffin_owner.objects.filter(to_email=email, to_pass=password).count()
            if val ==1:
                obj = tiffin_owner.objects.get(to_email=email)
                request.session['tiffin_owner_id']=email
                request.session['name'] = obj.to_name
                request.session['random']="tiffin"
                print("_____________________________", request.session['tiffin_owner_id'])
                return redirect('/Client/home')
            else:
                return redirect('/Client/log/')

    else:
        return render(request, 'client_login.html')


def insertt_house_details(request):
    own = owner.objects.all()
    are = area.objects.all()
    if request.method == "POST":
        form = house_details_form(request.POST, request.FILES)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['h_imgpath'])
                form.save()
                return redirect('/Client/home/')
            except:
                print("________________", sys.exc_info())
    else:
        form = house_details_form()
    return render(request, "add_house.html", {'form': form, 'own': own, 'are': are})



def insert_pg_details(request):
    own = owner.objects.all()
    are = area.objects.all()
    if request.method == "POST":
        form = pg_details_form(request.POST, request.FILES)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['pg_imgpath'])
                form.save()
                return redirect('/Client/home/')
            except:
                print("________________", sys.exc_info())
    else:
        form = house_details_form()
    return render(request, "add_pg.html", {'form': form, 'own': own, 'are': are})



def insertt_tiffin_details(request):
    own = tiffin_owner.objects.all()

    if request.method == "POST":
        form = tiffin_details_form(request.POST, request.FILES)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['tiff_imgpath'])
                form.save()
                return redirect('/Client/home/')
            except:
                print("________________", sys.exc_info())
    else:
        form = tiffin_details_form()
    return render(request, "add_tiffin.html", {'form': form, 'own': own})




# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['pass']
#         val = customer.objects.filter(c_email=email, c_pass=password).count()
#         print("-------------------", email, "-----------------", password, val)
#         if val == 1:
#             print("=====INSIDE IFFFFF")
#             udata = customer.objects.filter(c_email=email, c_pass=password)
#             for item in udata:
#                 request.session['client_email'] = item.c_email
#                 request.session['client_pass'] = item.c_pass
#                 request.session['client_id'] = item.c_id
#                 if request.POST.get("remember"):
#                     print("==INSIDE COOKIEEEEEE=", )
#                     response = redirect("/Client/deshbored/")
#                     response.set_cookie('cookie_client_email', request.POST["email"], 3600 * 24 * 365 * 2)
#                     response.set_cookie('cookie_client_password', request.POST["pass"], 3600 * 24 * 365 * 2)
#                     return response
#             return redirect('/Client/home/')
#
#         else:
#             messages.error("invalid password")
#             return redirect('/cust_table/')
#     else:
#         if request.COOKIES.get("cookie_client_email"):
#             return render(request, "client_login.html",
#                           {'client_email': request.COOKIES['cookie_client_email'],
#                            'client_password': request.COOKIES[
#                                'cookie_client_password']})
#         else:
#             return render(request, 'client_login.html')

def logout(request):
    request.session.clear()
    return redirect('/Client/home')

def home(request):
    h_details = house_details.objects.all()
    pg = pg_details.objects.all()
    tiff = tiffin_details.objects.all()
    data = {'h_details': h_details, 'pg': pg, 'tiff': tiff}
    return render(request, 'client_home.html', data)


def checkout(request):
    return render(request, 'client_checkout.html')


def user_profile(request):
    return render(request, 'client_user-profile.html')


def about_us(request):
    return render(request, 'client_about.html')


def blog(request):
    book = customer.objects.all()
    # print("-----------",booking.bk_date)
    return render(request, 'client_blog.html', {'book': book})


def contact_us(request):
    return render(request, 'client_contact-us.html')


def properties_grid(request):
    pg = pg_details.objects.all()
    # print("==============", pg.pg_name)
    return render(request, 'client_properties_full_grid.html', {"pg": pg})


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


def home_details(request):
    home = house_details.objects.all()

    return render(request, "client_home_details.html", {'home': home})


def pg1_details(request):
    pg1 = pg_details.objects.all()
    return render(request, "client_pg_details.html", {'pg1': pg1})


def home_desc(request, id):
    home1 = house_details.objects.filter(h_id=id)
    page = request.GET.get('page', 1)
    print("page---------------", page)
    return render(request, "client_home_description.html", {'home1': home1})


def pg_desc(request, id):
    p = pg_details.objects.filter(pg_id=id)
    page = request.GET.get('page', 1)
    print("page---------------", page)
    return render(request, "client_pg_description.html", {"p": p})


def tiff_desc(request, id):
    p = tiffin_details.objects.filter(tiff_id=id)
    page = request.GET.get('page', 1)
    print("page---------------", page)
    return render(request, "client_tiff_description.html", {"p": p})


def mybookings(request):
    return render(request, "client_mybookings.html")
