# from http.client import HTTPResponse
# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
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

#@login_required
def login(request):
    #page for logging in user

    username = request.Post['username']
    password = request.Post['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
            #return home page
    else:   
        return #login page, invalid login message

def logout_view(request):
    logout(request)
    #return login page, logout message
