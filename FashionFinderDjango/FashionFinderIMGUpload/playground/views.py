import base64
# Create your views here.
import os

import pymongo
from django.shortcuts import render


def convert64(file_name):
    image_file = open(file_name, "rb")
    bs64_str = base64.b64encode(image_file.read())
    return bs64_str


conn_str = "mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.quth27s.mongodb.net/test"

connection = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = connection.test
file_meta = db.file_meta


def say_hello(request):
    return render(request, 'hello.html')


def upload(request):
    if request.method == "POST":
        uploadedfile = request.FILES['ourimage']
        handle_uploaded_file(request.FILES['ourimage'])
        print(uploadedfile.name)
        enc_file = convert64(uploadedfile.name)
        os.remove(uploadedfile.name)
        coll = db.testcollection
        coll.insert_one({"filename": uploadedfile.name, "file": enc_file, "description": "test"})
        # print(uploadedfile.size)
    return render(request, 'upload.html')


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
