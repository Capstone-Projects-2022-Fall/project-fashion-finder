import io
import os

import numpy as np
import tensorflow.keras as keras
from PIL import Image
from django.conf import settings

TARGET_SIZE = (224, 224)

from ImgPredMicroservice.color_predict import get_dominant_colors

CLASS_LIST_21 = ["Tee", "Tank", "Dress", "Shorts", "Skirt", "Hoodie", "Jumpsuit", "Sweater", "Blazer", "Striped",
                 "Cardigan", "Blouse", "Jacket", "Jeans", "Maxi", "Floral", "Denim", "Sweatshorts", "Polka", "Shawl",
                 "Bodycon"]
CLASS_LIST = CLASS_LIST_21

from keras.models import load_model

MODEL_PATH = os.path.join(settings.BASE_DIR,
                          'ImgPredMicroservice/artifacts/best_model_21_class_lr@0.002-1666761586.9275644.hdf5')

model = load_model(MODEL_PATH, custom_objects={'weighted_binary_crossentropy': lambda x: 0})


def binarizeOutput(y_pred, threshold=0.5):
    y_pred_bin = np.where(y_pred > threshold, 1, 0)
    return y_pred_bin


def hex_to_rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def predict_class(filepath):
    response_data = {}
    buffer = io.BytesIO()
    im = Image.open(filepath)
    im.save(fp=buffer, format='JPEG')

    img = keras.utils.load_img(buffer, target_size=TARGET_SIZE)
    img = keras.utils.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    color_img = img.copy()
    hexes = get_dominant_colors(color_img)
    img = img / 255
    y_pred = model.predict(img)
    y_pred_bin = binarizeOutput(y_pred, threshold=0.2)
    y_pred_classes = [[CLASS_LIST[i]
                       for i, x in enumerate(row) if x == 1]
                      for row in y_pred_bin]

    if (len(y_pred_classes) == 0):
        y_pred_classes = [CLASS_LIST[np.argmax(y_pred_bin)]]
    # response_data[key] = dict()
    y_pred_classes_flat = [cls for sub_list in y_pred_classes for cls in sub_list]

    response_data['labels'] = y_pred_classes_flat
    response_data['hex_codes'] = hexes
    response_data['rgb_0'] = hex_to_rgb(hexes[0])
    response_data['rgb_1'] = hex_to_rgb(hexes[1])
    response_data['rgb_2'] = hex_to_rgb(hexes[2])

    return response_data
