def handle_uploaded_file(f):
    with open('leasify_admin/static/assets/images/project/'+f.name,"wb+") as destination:
        for data in f.chunks():
            destination.write(data)