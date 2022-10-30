from django.shortcuts import render
from django.http import HttpResponse
import tensorflow as tf 
import tensorflow.keras as keras
from keras.applications.vgg16 import VGG16, preprocess_input
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import io
import numpy as np
from keras.models import load_model
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import json
from django.conf import settings
from . import color_predict
from ImgPredMicroservice.color_predict import get_dominant_colors
from ImgPredMicroservice.class_predict import predict_class
# from ImgPredMicroservice.color_predict import 
from fashionfinderapp.utils import get_db_default_handle
from ImgPredMicroservice.upload_piece_to_mongo import create_user_fashion_piece, insert_user_fashion_piece


CLASS_LIST_21 = ["Tee","Tank","Dress","Shorts","Skirt","Hoodie","Jumpsuit","Sweater","Blazer","Striped","Cardigan","Blouse","Jacket","Jeans","Maxi","Floral","Denim","Sweatshorts","Polka","Shawl","Bodycon"]
CLASS_LIST = CLASS_LIST_21
MODEL_PATH = os.path.join(settings.BASE_DIR, 'ImgPredMicroservice/artifacts/best_model_21_class_lr@0.002-1666761586.9275644.hdf5')
# This gets run when the app is started. Provide nonsense loss function
model = load_model(MODEL_PATH, custom_objects={'weighted_binary_crossentropy': lambda x: 0})

# Create your views here.


def index(request):
    return HttpResponse("Valid routes is /predict")


TARGET_SIZE = (224, 224)


@csrf_exempt
def predict(request):

    if (request.method == 'POST'):
        f = list(request.FILES.values())[0]
        mongo_data = predict_class(f)
        mongo_data['user_django_id'] = request.user.id
        mongo_data['descriptor'] = request.POST['title']
        im = Image.open(f)
        img_bytes = io.BytesIO()
        im.save(img_bytes, format='JPEG')
        # mongo_data['img_data'] = img_bytes
        mongo_doc = create_user_fashion_piece(mongo_data, img_bytes)

        if(mongo_doc is not None):
            inserted_id = insert_user_fashion_piece(mongo_doc)

            if(inserted_id is None):
                return HttpResponse(json.dumps({'Status':'Failed to upload'}),
                        content_type='application/json')
            else:
              return HttpResponse(json.dumps({'Status':'Success',"upload_id":str(inserted_id)}),
                            content_type='application/json')  

    else:
        return HttpResponse('Ensure that you are sending a POST request with Body of type "form-data" where the form data is key-value pairs of names of files and files')


@csrf_exempt
def color_predict(request):
    if(request.user.id is None):
        return HttpResponse(400)
    if(request.method == 'POST'):
        print(request.FILES)
        for filepath in request.FILES.values():
            buffer = io.BytesIO()
            im = Image.open(filepath)
            im.save(fp=buffer, format='JPEG')
            img = keras.utils.load_img(buffer, target_size=TARGET_SIZE)
            img = keras.utils.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            hexes = get_dominant_colors(img)
            print(hexes)
            return HttpResponse(hexes)
    else:
        return HttpResponse('Ensure that you are sending a POST request with Body of type "form-data" where the form data is key-value pairs of names of files and files')
    
    return HttpResponse(200)