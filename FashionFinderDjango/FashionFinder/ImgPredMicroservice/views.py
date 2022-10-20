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
CLASS_LIST = ["Tee", "Tank", "Dress", "Shorts", "Skirt", "Jumpsuit", "Sweater", "Blazer", "Striped", "Cardigan", "Blouse", "Romper", "Sweatpants", "Jacket"]
MODEL_PATH = os.path.join(settings.BASE_DIR, 'ImgPredMicroservice/artifacts/best_model_14_class_lr@0.0001-1665971573.2646348.hdf5')
# This gets run when the app is started
model = load_model(MODEL_PATH)

# Create your views here.


def index(request):
    return HttpResponse("Valid routes is /predict")


TARGET_SIZE = (512, 512)


@csrf_exempt
def predict(request):
    def binarizeOutput(y_pred, threshold=0.5):
        y_pred_bin = np.where(y_pred > threshold, 1, 0)
        return y_pred_bin
    if (request.method == 'POST'):

        response_data = {}
        keys = request.FILES.keys()
        files = request.FILES.values()
        for key, f in zip(keys, files):
            buffer = io.BytesIO()
            im = Image.open(f)
            im.save(fp=buffer, format='JPEG')

            img = keras.utils.load_img(buffer, target_size=TARGET_SIZE)
            img = keras.utils.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img = img/255
            y_pred = model.predict(img)
            y_pred_bin = binarizeOutput(y_pred, threshold=0.2)
            y_pred_classes = [[CLASS_LIST[i]
                                    for i, x in enumerate(row) if x == 1]
                                    for row in y_pred_bin]

            if (len(y_pred_classes) == 0):
                y_pred_classes = [CLASS_LIST[np.argmax(y_pred_bin)]]
            response_data[key] = y_pred_classes
        return HttpResponse(json.dumps(response_data),
                            content_type='application/json')
    else:
        return HttpResponse('Ensure that you are sending a POST request with Body of type "form-data" where the form data is key-value pairs of names of files and files')
