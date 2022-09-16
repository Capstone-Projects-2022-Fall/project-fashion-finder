# from http.client import HTTPResponse
# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import fashionfinderapp.utils.utils
# Create your views here.


def index(request):
    # Default Page
    return HttpResponse("Hello, world. Welcome to fashion finder")


def home(request):
    # Home Page
    template = loader.get_template('index.html')
    context = {'foo': 'bar'}
    return HttpResponse(
        template.render(context, request),
        content_type='text/html')


def pieces(request):
    # Page for showing the current pieces in the database

    _, client = fashionfinderapp.utils.get_db_default_handle()
    fashion_collection = client['fashion_finder_db']['FashionPiece']
    
    pieces_cursor = fashion_collection.find()
    context = {'pieces': pieces_cursor}

    template = loader.get_template('pieces.html')

    return HttpResponse(
        template.render(context, request),
        content_type='text/html')
