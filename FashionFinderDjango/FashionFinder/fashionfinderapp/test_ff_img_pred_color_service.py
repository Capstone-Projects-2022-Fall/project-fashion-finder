import ImgPredMicroservice.color_predict as ImgPredColorPredictHandler
from django.conf import settings as DjangoSettings
from django.test import Client, TestCase
import numpy as np


class TestImgPredMicroserviceColorService(TestCase):
    def setUp(self):
        print("Setup")
        self.images_test_dir = DjangoSettings.USER_UPLOAD_ROOT + 'images/test/'
        filepath = '6372c4146a17ad72dc478018.jpg'
        self.filepath = self.images_test_dir + filepath

    def test_get_gaussian_kernel(self):
        g = ImgPredColorPredictHandler.gaussian_kernel(224,224, 0.1)
        self.assertEqual(type(g),np.ndarray)
        self.assertEqual(np.shape(g), (224,224))
    def test_get_flattneed_gaussian_kernel(self):
        g = ImgPredColorPredictHandler.gaussian_kernel(224,224, 0.1)
        self.assertEqual(type(g),np.ndarray)
        self.assertEqual(np.shape(g), (224,224))

        g_flat = ImgPredColorPredictHandler.get_flatted_normalized_gaussian_kernel(g)
        self.assertEqual(np.shape(g_flat), (50176,))
        self.assertEqual(np.sum(g_flat), 1)
    
    def test_get_draw(self):
        g = ImgPredColorPredictHandler.gaussian_kernel(224,224, 0.1)
        self.assertEqual(type(g),np.ndarray)
        self.assertEqual(np.shape(g), (224,224))

        g_flat = ImgPredColorPredictHandler.get_flatted_normalized_gaussian_kernel(g)
        self.assertEqual(np.shape(g_flat), (50176,))
        self.assertEqual(np.sum(g_flat), 1)
        test_pixel_idxs = np.arange(50176)
        draw =  ImgPredColorPredictHandler.get_draw(test_pixel_idxs, normed_kernel=g_flat, sample_size=100)
        self.assertEqual(len(draw), 100)

        draw =  ImgPredColorPredictHandler.get_draw(test_pixel_idxs, normed_kernel=g_flat, sample_size=500)
        self.assertEqual(len(draw), 500)

        draw =  ImgPredColorPredictHandler.get_draw(test_pixel_idxs, normed_kernel=g_flat, sample_size=1000)
        self.assertEqual(len(draw), 1000)

    def test_rgb_to_hex_red(self):
        rgb = [255, 0, 0]
        hex = ImgPredColorPredictHandler.rgb_to_hex(rgb[0], rgb[1], rgb[2])
        self.assertEqual(hex, 'FF0000')
    def test_rgb_to_hex_red(self):
        rgb = [0, 255, 0]
        hex = ImgPredColorPredictHandler.rgb_to_hex(rgb[0], rgb[1], rgb[2])
        self.assertEqual(hex, '00FF00')
    def test_rgb_to_hex_red(self):
        rgb = [0, 255, 0]
        hex = ImgPredColorPredictHandler.rgb_to_hex(rgb[0], rgb[1], rgb[2])
        self.assertEqual(hex, '00FF00')

    def test_knn_for_color_list(self):
        test_color_list = [
            [255, 0, 0],
            [0, 255, 0],
            [255, 0, 0],
            [244, 0 , 0],
            [0, 244, 0],
            [0, 0, 244],
        ]
        cluster_centers = ImgPredColorPredictHandler.get_knn_for_colors_list(test_color_list)
        self.assertEqual(len(cluster_centers), 3)

    def test_get_dominant_colors(self):
        img = ImgPredColorPredictHandler.readImg(self.filepath)

        g = ImgPredColorPredictHandler.gaussian_kernel(224,224, 0.1)
        self.assertEqual(type(g),np.ndarray)
        self.assertEqual(np.shape(g), (224,224))

        g_flat = ImgPredColorPredictHandler.get_flatted_normalized_gaussian_kernel(g)
        self.assertEqual(np.shape(g_flat), (50176,))
        self.assertEqual(np.sum(g_flat), 1)

        hex_vals = ImgPredColorPredictHandler.get_dominant_colors(img, g_flat)
        self.assertEqual(len(hex_vals), 3)
    