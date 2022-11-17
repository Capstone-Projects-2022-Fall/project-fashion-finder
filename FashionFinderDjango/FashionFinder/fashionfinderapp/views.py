# from http.client import HTTPResponse
# from django.shortcuts import render
import io
import json
import os

from PIL import Image
from django.conf import settings as django_settings
from django.contrib.auth import authenticate as django_authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie

import fashionfinderapp.utils.utils
from ImgPredMicroservice.upload_piece_to_mongo import get_wardrobe, get_recommendations
from fashionfinderapp.forms import RegistrationForm, UploadImgForPredMicroserviceForm, SignInForm
from fashionfinderapp.models import *


# Create your views here.

@ensure_csrf_cookie
def index(request):
    # Default Page
    return HttpResponse(render_to_string('html/index.html', {
        "json": json.dumps({
            "user_id": json.dumps(request.user.id)
        })
    }))


# #page to vote on pieces
# def vote(request):
#     # Page for voting on pieces
#     template = loader.get_template('vote.html')
#     # return HttpResponse(template.render({}, request))
#     return HttpResponse(render_to_string('vote.html', {
#         "json": json.dumps({
#             "user_id": json.dumps(request.user.id)
#         })
#     }))
#
# def vote(request):
#     # Page for voting on pieces
#     template = loader.get_template('vote.html')
#     # return HttpResponse(template.render({}, request))
#     return HttpResponse(render_to_string('vote.html', {
#         "json": json.dumps({
#             "user_id": json.dumps(request.user.id)
#         })
#     }))

def upload(request):
    # Page for uploading pieces
    template = loader.get_template('upload.html')
    # return HttpResponse(template.render({}, request))
    return HttpResponse(render_to_string('upload.html', {
        "json": json.dumps({
            "user_id": json.dumps(request.user.id)
        })
    }))


def vote(request):
    if request.method == "POST":
        print("Vote called")
        print(request.body)
        data = json.loads(request.body)
        print(data)
        user_id = data['user_id']
        piece_id = data['piece_id']
        vote = data['vote']
        print(user_id, piece_id, vote)
        _, client = fashionfinderapp.utils.get_db_default_handle()
        fashion_collection = client['fashion_finder_db']['FashionPiece']
        fashion_collection.update_one({"_id": (piece_id)}, {"$push": {"votes": {"user_id": user_id, "vote": vote}}})
        return HttpResponse("")
        return HttpResponse("OK")
    else:
        return HttpResponse("Method not supported")


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
    return HttpResponse(render_to_string('user.html', {
        "json": json.dumps({
            "current_user_id": json.dumps(request.user.id),
            "user_id": json.dumps(u.id),
            "user_name": json.dumps(u.username)
        })
    }))


# @login_required
def login(request):
    # page for logging in user

    print("Login view called")
    print(request.user)
    print(request.body)
    response_data = {}

    context_dict = {'form': None}
    # form = LoginForm()

    if request.user.is_authenticated:
        print("User is already logged in")
        return HttpResponseRedirect('/')
    elif request.method == "GET":
        # context_dict['form'] = form
        return HttpResponse(render_to_string('registration/login.html', {
            "json": json.dumps(response_data)
        }))
    elif request.method == "POST":
        form = SignInForm(request.POST)
        context_dict['form'] = form
        user = None
        if form.is_valid():
            print("User found")
            user = django_authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            django_login(request, user)
            return HttpResponseRedirect('/')
        else:
            print("User not found")
            print(form.errors)
            return HttpResponseRedirect('/accounts/login')
    else:
        print("Method not supported")
        return HttpResponseRedirect('/accounts/login')


def logout_view(request):
    django_logout(request)
    return HttpResponse(render_to_string('registration/register.html', {
    }))


def register(request):
    response_data = {}
    context_dict = {'form': None}
    if request.user.is_authenticated:
        print("User is already authenticated")
        return HttpResponseRedirect('/')
    elif request.method == "GET":
        return HttpResponse(render_to_string('registration/register.html', {
            "json": json.dumps(response_data)
        }))
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = django_authenticate(username=username, password=password)
            django_login(request, user)
            return HttpResponseRedirect('/')
        else:
            print("Form is not valid")
            print(form.errors)
            response_data['error'] = json.dumps(form.errors)
            return HttpResponse(response_data)


@login_required
def predict(request):
    template = loader.get_template('predict.html')
    context = {}
    form = UploadImgForPredMicroserviceForm()
    return render(request, 'predict.html', {'form': form})


@login_required
def colors(request):
    form = UploadImgForPredMicroserviceForm()
    return render(request, 'color.html', {'form': form})


# Save the mongo record to 
def save_mongo_img_data_to_static_dir(rec):
    img = Image.open(io.BytesIO(rec['img_data']))
    f_name = "%s.jpg" % rec['_id']
    f_path = os.path.join(django_settings.STATIC_ROOT, f_name)
    img.save(f_path)
    print("saved")
    del rec['img_data']
    rec['id'] = rec['_id']
    del rec['_id']
    return rec


# def get_record_id(rec):
# return rec['_id']

@login_required
def wardrobe(request):
    if (request.method == 'GET'):
        recs = get_wardrobe(request.user.id, request.user.username, n=10)
        for rec in recs:
            # print(rec)
            break
        print(type(recs))
        recs = [save_mongo_img_data_to_static_dir(rec) for rec in recs]
        # ids = [get_record_id(rec) for rec in recs]
        # print(thinned_ids)

        context = {'recs': recs}
        template = loader.get_template('recs.html')
        return HttpResponse(
            template.render(context, request),
            content_type='text/html')

    else:
        return HttpResponse(400)


@login_required
def rec(request):
    if (request.method == 'GET'):
        recs, user_piece_rec = get_recommendations(request.user.id, request.user.username, n=10)

        # print(type(recs))
        user_piece_rec = save_mongo_img_data_to_static_dir(user_piece_rec)
        recs = [save_mongo_img_data_to_static_dir(rec) for rec in recs]
        # ids = [get_record_id(rec) for rec in recs]
        # print(thinned_ids)

        context = {'recs': recs, 'user_piece_rec': user_piece_rec}
        template = loader.get_template('vote.html')
        return HttpResponse(
            template.render(context, request),
            content_type='text/html')
    else:
        return HttpResponse(400)
