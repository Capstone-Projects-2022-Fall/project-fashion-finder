# from http.client import HTTPResponse
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string, get_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import fashionfinderapp.utils.utils
from django.shortcuts import render
from django.http import HttpResponseRedirect
import json

from fashionfinderapp.models import *
from fashionfinderapp.forms import *
# Create your views here.


def index(request):
    # Default Page
    return HttpResponse(render_to_string('html/index.html'))


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

def user(request, user_id=None):
    u = User.objects.filter(id=user_id).first()
    return HttpResponse(render_to_string('user.html',{
        "json": json.dumps({
            "current_user_id": json.dumps(request.user.id),
            "user_id": json.dumps(u.id),
            "user_name": json.dumps(u.username)
            })
    }))

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

def register(request):
    response_data = {}

    context_dict = { 'form': None }
    form = RegistrationForm()

    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    elif request.method == "GET":
        context_dict['form'] = form
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            response_data['error'] = json.dumps(form.errors)

    return HttpResponse(render_to_string('registration/register.html', {
        "json": json.dumps(response_data)
    }))
