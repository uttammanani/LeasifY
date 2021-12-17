import sys

from django.http import HttpResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from leasify_admin.function import handle_uploaded_file
from leasify_admin.models import customer, owner, house_details, area, house_gallery, pg_details, pg_gallery, \
    tiffin_owner, tiffin_details, status, notification, feedback

from leasify_admin.forms import house_details_form, owner_form, area_form, pg_details_form, tiffin_owner_form, \
    tiffin_details_form, house_gallery_form, pg_gallery_form


def show(request):
    show1 = customer.objects.all()
    return render(request, "show.html", {'show1': show1})


def loadadmin(request):
    return render(request, "admin_header.html")


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
        form = house_details_form(request.POST,request.FILES)
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
        return render(request, "owner_insertform.html",{'form':form})


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
        form = pg_details_form(request.POST,request.FILES)
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
        form = tiffin_details_form(request.POST,request.FILES)
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
        form = house_gallery_form(request.POST,request.FILES)
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
        form = pg_gallery_form(request.POST,request.FILES)
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

def update_area(request,id):
    are= area.objects.get(a_id=id)
    form=area_form(request.POST,instance=are)

    if form.is_valid():
        form.save()
        return redirect("/area_table")
    return render(request,'area_update.html',{'are':are})


def update_house_details(request,id):
    temp= house_details.objects.get(h_id=id)
    form=house_details_form(request.POST,instance=temp)

    if form.is_valid():
        form.save()
        return redirect("/house_details_table")
    return render(request,'house_details_update.html',{'temp':temp})








