import ImgPredMicroservice.class_predict as ImgPredClassPredictHandler
from django.test import Client, TestCase
from django.conf import settings as DjangoSettings
import PIL
import io
import numpy as np


class TestFFPredClassService(TestCase):
    def setUp(self):
        print("Setup")
        self.images_test_dir = DjangoSettings.USER_UPLOAD_ROOT + 'images/test/'
        filepath = '6372c4146a17ad72dc478018.jpg'
        self.filepath = self.images_test_dir + filepath
        # im = PIL.Image.open(self.test_images_dir + filepath)
        # self.img_bytes = io.BytesIO()
        # im.save(self.img_bytes, format='JPEG')

    def test_binarizeOutput(self):
        arr = np.array([0.4, 0.6, 0.7])
        output = ImgPredClassPredictHandler.binarizeOutput(arr, threshold=0.5)
        # self.assertTrue(output == np.array([0, 1, 1]))
        self.assertEqual(output[0], 0)
        self.assertEqual(output[1], 1)
        self.assertEqual(output[2], 1)
    def test_binarizeOutputCustomThreshold(self):
        arr = np.array([0.3, 0.7, 0.8])
        output = ImgPredClassPredictHandler.binarizeOutput(arr, threshold=0.75)
        self.assertEqual(output[0], 0)
        self.assertEqual(output[1], 0)
        self.assertEqual(output[2], 1)

    def test_hex_to_rgb_red(self):
        hex = "FF0000"
        rgb = ImgPredClassPredictHandler.hex_to_rgb(hex)
        self.assertEqual(type(rgb), tuple)
        self.assertEqual(rgb[0], 255)
        self.assertEqual(rgb[1], 0)
        self.assertEqual(rgb[2], 0)
    def test_hex_to_rgb_green(self):
        hex = "00FF00"
        rgb = ImgPredClassPredictHandler.hex_to_rgb(hex)
        self.assertEqual(type(rgb), tuple)
        self.assertEqual(rgb[0], 0)
        self.assertEqual(rgb[1], 255)
        self.assertEqual(rgb[2], 0)
    def test_hex_to_rgb_blue(self):
        hex = "0000FF"
        rgb = ImgPredClassPredictHandler.hex_to_rgb(hex)
        self.assertEqual(type(rgb), tuple)
        self.assertEqual(rgb[0], 0)
        self.assertEqual(rgb[1], 0)
        self.assertEqual(rgb[2], 255)

    def test_predict_class(self):
        # f is a picture of a tank top
        f = self.filepath
        response_data = ImgPredClassPredictHandler.predict_class(f)
        self.assertIn('Tee',response_data['labels'])
        self.assertIn('Tank',response_data['labels'])
        