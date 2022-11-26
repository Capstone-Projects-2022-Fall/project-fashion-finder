# from http.client import HTTPResponse
# from django.shortcuts import render
import imp
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate as django_authenticate, login as django_login, logout as django_logout 
from django.template.loader import render_to_string, get_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import fashionfinderapp.utils.utils
from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
from PIL import Image
import io
from django.conf import settings as django_settings
import os
from django.views.decorators.csrf import ensure_csrf_cookie
from bson.objectid import ObjectId


from fashionfinderapp.models import *
from fashionfinderapp.forms import RegistrationForm, UploadImgForPredMicroserviceForm, SignInForm
from ImgPredMicroservice.upload_piece_to_mongo import get_wardrobe, get_recommendations, get_complementary_recommendation
# Create your views here.

@ensure_csrf_cookie
def index(request):
    """
    Default Page, serves as home page for application.

    :return: Index.html page.
    :rtype: An Http response.
    """
    return HttpResponse(render_to_string('html/index.html', {
        "json": json.dumps({
            "user_id": json.dumps(request.user.id)
        })
    }))


def pieces(request):
    """
    A page for showing the current pieces in the database
    """

    _, client = fashionfinderapp.utils.get_db_default_handle()
    fashion_collection = client['fashion_finder_db']['FashionPiece']
    
    pieces_cursor = fashion_collection.find()
    context = {'pieces': pieces_cursor}

    template = loader.get_template('pieces.html')

    return HttpResponse(
        template.render(context, request),
        content_type='text/html')

def user(request, user_id=None):
    """
    A view of the user's id and name information.

    :return: user.html page.
    :rtype: An Http response.
    """
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
    """
    A Page for logging in user.

    If user is logged in, redirects to home page.
    
    Otherwise, loads the Login html page and Login Form.

    Checks if form is complete and user is found. If user is found and password is correct, redirects to home page.

    If login form is incomplete or user is not found, reloads login form and page.

    :return: login.html page.
    :rtype: An Http response.
    """

    print("Login view called")
    print(request.user)
    print(request.body)
    response_data = {}

    context_dict = { 'form': None }
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
    """
    Completes user logout and redirects to Sign In form.

    :return: login.html page.
    :rtype: An Http response.
    """
    django_logout(request)
    return HttpResponse(render_to_string('registration/login.html', {
    }))

def register(request):
    """
    New user sign-up. 

    If user is logged in, redirects to home page.
    
    Otherwise, loads the Registration html page and Register Form.

    Checks if registration form is complete. Adds user to user database and redirects to homepage.

    If registration form is incomplete or user is not found, reloads registration form and page.

    :return: index.html page.
    :rtype: An Http response.

    """

    response_data = {}
    context_dict = { 'form': None }
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
    """
    
    """

    template = loader.get_template('predict.html')
    context = {}
    form = UploadImgForPredMicroserviceForm()
    return render(request, 'predict.html', {'form': form} )

@login_required
def colors(request):
    """
    """
    form = UploadImgForPredMicroserviceForm()
    return render(request, 'color.html', {'form': form} )


# Save the mongo record to 
def save_mongo_img_data_to_static_dir(rec):
    """
    Saves the Mongo Image data to the static directory.

    :return: image_data
    """
    print("saving image....")
    img = Image.open(io.BytesIO(rec['img_data']))
    f_name = "%s.jpg" % rec['_id']
    f_path = os.path.join(django_settings.USER_UPLOAD_ROOT, f_name)
    img.save(f_path)
    print("saved")
    del rec['img_data']
    rec['filepath'] = '/static/' + str(rec['_id']) + '.jpg'
    rec['_id'] = str(rec['_id'])
    rec['id'] = str(rec['_id'])
    return rec

# def get_record_id(rec):
    # return rec['_id']

@login_required
def wardrobe(request):
    """
    Displays the image of each fashion item uploaded by a user.

    :return: recs.html page.
    :rtype: An Http response.
    """
    if(request.method == 'GET'):
        recs = get_wardrobe(request.user.id, request.user.username, n=10)
        recs = [save_mongo_img_data_to_static_dir(rec) for rec in recs]
        # ids = [get_record_id(rec) for rec in recs]
        # print(thinned_ids)
        
        context = {'recs':recs}
        template = loader.get_template('recs.html')
        return HttpResponse(
            template.render(context, request),
            content_type='text/html')
    else:
        return HttpResponse(400)

@login_required
def wardrobe_json(request):
    if(request.method == 'GET'):
        print(request.user.id)
        print(request.user.username)
        recs = get_wardrobe(request.user.id, request.user.username, n=10)
        recs = [save_mongo_img_data_to_static_dir(rec) for rec in recs]
        context = {'recs':recs}
        template = loader.get_template('recs.html')
        return JsonResponse({'recs':recs})
    else:
        return HttpResponse(400)
@login_required
def rec(request):
    """
    A page that displays images of fashion pieces

    :return: recs.html page.
    :rtype: An Http response.
    """
    if(request.method == 'GET'):
        recs, user_piece_rec = get_recommendations(request.user.id,request.user.username, n=10)

        # print(type(recs))
        user_piece_rec = save_mongo_img_data_to_static_dir(user_piece_rec)
        recs = [save_mongo_img_data_to_static_dir(rec) for rec in recs]
        # ids = [get_record_id(rec) for rec in recs]
        # print(thinned_ids)
        
        context = {'recs':recs, 'user_piece_rec':user_piece_rec}
        template = loader.get_template('recs.html')
        return HttpResponse(
            template.render(context, request),
            content_type='text/html')
    else:
        return HttpResponse(400)

def rec_async(request, piece_id):
    if(request.method == 'GET'):
        recs, user_piece_rec = get_recommendations(piece_id, n=10)
        user_piece_rec = save_mongo_img_data_to_static_dir(user_piece_rec)
        recs = [save_mongo_img_data_to_static_dir(rec) for rec in recs]
        print(recs)
        for rec in recs:
            rec['id'] = rec['_id']
            print(rec['_id'])
        # ids = [get_record_id(rec) for rec in recs]
        # print(thinned_ids)
        
        context = {'recs':recs, 'user_piece_rec':user_piece_rec}
        template = loader.get_template('recs.html')
        return HttpResponse(
            template.render(context, request),
            content_type='text/html')
    else:
        return HttpResponse(400)

def rec_comp(request, piece_id):

    if(request.method == 'GET'):
        recs, user_piece_rec = get_complementary_recommendation(piece_id, n = 10)
        user_piece_rec = save_mongo_img_data_to_static_dir(user_piece_rec)
        recs = [save_mongo_img_data_to_static_dir(rec) for rec in recs]
        for rec in recs:
            rec['id'] = rec['_id']
            print(rec['_id'])
        context = {'recs':recs, 'user_piece_rec':user_piece_rec}
        template = loader.get_template('recs.html')
        return HttpResponse(
            template.render(context, request),
            content_type='text/html')
    else:
        return HttpResponse(400)

@login_required
def async_recommendations_json(request, piece_id):
    if(request.method == 'GET'):
        recs, user_piece_rec = get_recommendations(piece_id, n=10)
        user_piece_rec = save_mongo_img_data_to_static_dir(user_piece_rec)
        recs = [save_mongo_img_data_to_static_dir(rec) for rec in recs]
        # recs = get_wardrobe(request.user.id, request.user.username, n=10)
        # recs = [save_mongo_img_data_to_static_dir(rec) for rec in recs]
        context = {'recs':recs}
        template = loader.get_template('recs.html')
        return JsonResponse({'recs':recs})
    else:
        return HttpResponse(400)