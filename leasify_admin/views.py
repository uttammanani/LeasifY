
import sys
import random




from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from leasify_admin.function import handle_uploaded_file
from leasify_admin.models import customer, owner, house_details, area, house_gallery, pg_details, pg_gallery, \
    tiffin_owner, tiffin_details, status, notification, feedback, admin

from leasify_admin.forms import house_details_form, owner_form, area_form, pg_details_form, tiffin_owner_form, \
    tiffin_details_form, house_gallery_form, pg_gallery_form, admin_form


def show(request):
    show1 = customer.objects.all()
    return render(request, "show.html", {'show1': show1})


def loadadmin(request):
    return render(request, "admin_header.html")


def admin_login(request):
    if request.method == 'POST':
        uname = request.POST['admin_name']
        passsword = request.POST['admin_pass']
        val = admin.objects.filter(admin_name=uname, admin_pass=passsword).count()
        print("__________" + uname + "_______________" + passsword)
        if val == 1:
            return redirect('/index/')
        else:
            messages.error(request, "Invalid Username and password")
            return redirect('/admin_login/')
    else:
        return render(request,"admin_login.html")


def forgot_pass(request):
    return render(request, "forgot_pass.html")


def index(request):
    tiff = tiffin_owner.objects.filter().count()
    house = owner.objects.filter(o_type='House Owner').count()
    pg = owner.objects.filter(o_type='PG Owner').count()
    cust = customer.objects.filter().count()
    return render(request, "index.html", {'tiff': tiff, 'house': house, 'pg': pg, 'cust': cust})


def send_otp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['admin_email']

    request.session['temail'] = e

    obj = admin.objects.filter(admin_email=e).count()

    if obj == 1:

        val = admin.objects.filter(admin_email=e).update(otp=otp1, otp_used=0)

        subject = 'OTP FOR RESETING YOUR PASSWORD'
        message = "Your OTP for Reseting Your Password is " + str(
            otp1) + ".Please Dont Send of Forward To Anyone in order to Protect Your Account."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'set_password.html')
    else:
        messages.error(request, "Invalid Email.Please Try Again")
        return redirect('/forgot_password/')


def set_password(request):
    if request.method == "POST":

        T_otp = request.POST['otp']
        T_pass = request.POST['admin_pass']
        T_cpass = request.POST['cpass']

        if T_pass == T_cpass:

            e = request.session['temail']
            val = admin.objects.filter(admin_email=e, otp=T_otp, otp_used=0).count()

            if val == 1:
                admin.objects.filter(admin_email=e).update(otp_used=1, admin_pass=T_pass)
                return redirect("/admin_login")
            else:
                messages.error(request, "Invalid OTP")
                return render(request, "forgot_password.html")

        else:
            messages.error(request, "New password and Confirm password does not match ")
            return render(request, "set_password.html")

    else:
        return redirect("/forgot_password")


def cust_table(request):
    cust_data = customer.objects.all()
    return render(request, "customer_table.html", {'cust_data': cust_data})


def owner_table(request):
    owner_data = owner.objects.all()
    return render(request, "owner_table.html", {'owner_data': owner_data})


def house_details_table(request):
    house_details_data = house_details.objects.all()
    return render(request, "house_details_table.html", {'house_details_data': house_details_data})


def area_table(request):
    area_data = area.objects.all()
    return render(request, "area_table.html", {'area_data': area_data})


def house_gallery_table(request):
    h_gallery_data = house_gallery.objects.all()
    return render(request, "house_gallery_table.html", {'h_gallery_data': h_gallery_data})


def pg_details_table(request):
    pg_details_data = pg_details.objects.all()
    return render(request, "pg_details_table.html", {'pg_details_data': pg_details_data})


def pg_gallery_table(request):
    pg_gallery_data = pg_gallery.objects.all()
    return render(request, "pg_gallery_table.html", {'pg_gallery_data': pg_gallery_data})


def tiffi_owner_table(request):
    tiffin_owner_data = tiffin_owner.objects.all()
    return render(request, "tiffin_owner_table.html", {'tiffin_owner_data': tiffin_owner_data})


def tiffin_details_table(request):
    tiffin_details_data = tiffin_details.objects.all()
    return render(request, "tiffin_details_table.html", {'tiffin_details_data': tiffin_details_data})


def status_table(request):
    status_data = status.objects.all()
    return render(request, "status_table.html", {'status_data': status_data})


def notification_table(request):
    noti_data = notification.objects.all()
    return render(request, "notification_table.html", {'noti_data': noti_data})


def feedback_table(request):
    feedback_data = feedback.objects.all()
    return render(request, "feedback_table.html", {'feedback_data': feedback_data})


def insert_house_details(request):
    own = owner.objects.all()
    are = area.objects.all()
    if request.method == "POST":
        form = house_details_form(request.POST, request.FILES)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['h_imgpath'])
                form.save()
                return redirect('/house_details_table')
            except:
                print("________________", sys.exc_info())
    else:
        form = house_details_form()
    return render(request, "house_details_insertform.html", {'form': form, 'own': own, 'are': are})


def insert_owner_details(request):
    if request.method == "POST":
        form = owner_form(request.POST)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/owner_table')
            except:
                print("________________", sys.exc_info())
    else:
        form = owner_form()
    return render(request, "owner_insertform.html", {'form': form})


def insert_area(request):
    if request.method == "POST":
        form = area_form(request.POST)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/area_table')
            except:
                print("________________", sys.exc_info())
    else:
        form = area_form()
    return render(request, "area_insertform.html", {'form': form})


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
                return redirect('/pg_details_table')
            except:
                print("________________", sys.exc_info())
    else:
        form = house_details_form()
    return render(request, "pg_details_insertform.html", {'form': form, 'own': own, 'are': are})


def insert_tiffin_owner_details(request):
    if request.method == "POST":
        form = tiffin_owner_form(request.POST)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/tiffin_owner_table')
            except:
                print("________________", sys.exc_info())
    else:
        form = tiffin_owner_form()
    return render(request, "tiffin_owner_insertform.html", {'form': form})


def insert_tiffin_details(request):
    own = tiffin_owner.objects.all()

    if request.method == "POST":
        form = tiffin_details_form(request.POST, request.FILES)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['tiff_imgpath'])
                form.save()
                return redirect('/tiffin_details_table')
            except:
                print("________________", sys.exc_info())
    else:
        form = tiffin_details_form()
    return render(request, "tiffin_details_insertform.html", {'form': form, 'own': own})


def insert_house_gallery(request):
    own = house_details.objects.all()

    if request.method == "POST":
        form = house_gallery_form(request.POST, request.FILES)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['hg_imgpath'])
                form.save()
                return redirect('/house_gallery_table')
            except:
                print("________________", sys.exc_info())
    else:
        form = tiffin_details_form()
    return render(request, "house_gallery_insertform.html", {'form': form, 'own': own})


def insert_pg_gallery(request):
    own = pg_details.objects.all()

    if request.method == "POST":
        form = pg_gallery_form(request.POST, request.FILES)
        print("__________________", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['pgg_imgpath'])
                form.save()
                return redirect('/pg_gallery_table')
            except:
                print("________________", sys.exc_info())
    else:
        form = tiffin_details_form()
    return render(request, "pg_gallery_insertform.html", {'form': form, 'own': own})


def update_area(request, id):
    are = area.objects.get(a_id=id)
    form = area_form(request.POST, instance=are)

    if form.is_valid():
        form.save()
        return redirect("/area_table")
    return render(request, 'area_update.html', {'are': are})


def update_house_details(request, id):
    own = owner.objects.all()
    are = area.objects.all()
    temp = house_details.objects.get(h_id=id)
    form = house_details_form(request.POST, instance=temp)
    if form.is_valid():
        form.save()
        return redirect("/house_details_table")
    return render(request, 'house_details_update.html', {'temp': temp, 'own': own, 'are': are})


def update_owner(request, id):
    temp = owner.objects.get(o_id=id)
    form = owner_form(request.POST, instance=temp)

    if form.is_valid():
        form.save()
        return redirect("/owner_table")
    return render(request, 'owner_update.html', {'temp': temp})

def update_admin(request):

    admin_data= admin.objects.all()
    temp = admin.objects.get(admin_id=id)
    form = admin_form(request.POST, instance=temp)

    if form.is_valid():
        form.save()
        return redirect("/index")
    return render(request, 'edit_profile.html', {'temp': temp,'admin_data':admin_data})


def update_tiffin_owner(request, id):
    temp = tiffin_owner.objects.get(to_id=id)
    form = tiffin_owner_form(request.POST, instance=temp)

    if form.is_valid():
        form.save()
        return redirect("/tiffin_owner_table")
    return render(request, 'tiffin_owner_update.html', {'temp': temp})


def update_house_gallery(request, id):
    temp1 = house_details.objects.all()
    temp = house_gallery.objects.get(gallery_id=id)
    form = house_gallery_form(request.POST, instance=temp)

    if form.is_valid():
        form.save()
        return redirect("/house_gallery_table")
    return render(request, 'house_gallery_update.html', {'temp': temp,'temp1': temp1})


def update_pg_gallery(request, id):
    own = pg_details.objects.all()
    temp = pg_gallery.objects.get(pg_gallery_id=id)
    form = pg_gallery_form(request.POST, instance=temp)

    if form.is_valid():
        form.save()
        return redirect("/pg_gallery_table")
    return render(request, 'pg_gallery_update.html', {'temp': temp,'own':own})


def update_pg_details(request, id):
    own = owner.objects.all()
    are = area.objects.all()
    temp = pg_details.objects.get(pg_id=id)
    form = pg_details_form(request.POST, instance=temp)

    if form.is_valid():
        form.save()
        return redirect("/pg_details_table")
    return render(request, 'pg_details_update.html', {'temp': temp,'own': own, 'are': are})


def update_tiffin_details(request, id):
    own= tiffin_owner.objects.all()
    temp = tiffin_details.objects.get(tiff_id=id)
    form = tiffin_details_form(request.POST, instance=temp)

    if form.is_valid():
        form.save()
        return redirect("/tiffin_details_table")
    return render(request, 'tiffin_details_update.html', {'temp': temp,'own':own})


def del_area(request, id):
    temp = area.objects.get(a_id=id)
    temp.delete()
    return redirect("/area_table")


def del_house_details(request, id):
    temp = house_details.objects.get(h_id=id)
    temp.delete()
    return redirect("/house_details_table")


def del_house_gallery(request, id):
    temp = house_gallery.objects.get(gallery_id=id)
    temp.delete()
    return redirect("/house_gallery_table")


def del_owner(request, id):
    temp = owner.objects.get(o_id=id)
    temp.delete()
    return redirect("/owner_table")


def del_pg_details(request, id):
    temp = pg_details.objects.get(pg_id=id)
    temp.delete()
    return redirect("/pg_details_table")


def del_pg_gallery(request, id):
    temp = pg_gallery.objects.get(pg_gallery_id=id)
    temp.delete()
    return redirect("/pg_gallery_table")


def del_tiffin_details(request, id):
    temp = tiffin_details.objects.get(tiff_id=id)
    temp.delete()
    return redirect("/tiffin_details_table")


def del_tiffin_owner(request, id):
    temp = tiffin_owner.objects.get(to_id=id)
    temp.delete()
    return redirect("/tiffin_owner_table")
