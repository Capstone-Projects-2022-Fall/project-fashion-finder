from django.test import Client, TestCase
from django.urls import reverse
from .models import User
from django.conf import settings as DjangoSettings
import ImgPredMicroservice.upload_piece_to_mongo as MongoHandler 
import ImgPredMicroservice.class_predict as ImgPredClassPredictHandler
import ImgPredMicroservice.color_predict as ImgPredColorPredictHandler
import PIL
import io
class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        u = User.objects.create_user('foobar', 'foo@bar.com', 'password')
        u.first_name = "Foo"
        u.last_name = "Bar"
        u.save()
        self.User = u

    # Test that fashion finder responds to 
    def test_FF(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    
    def test_get_user(self):
        us = User.objects.filter(id=self.User.id).first()
        self.assertNotEqual(us, None)
        self.assertEqual(us.id, self.User.id)


    # def test_home_page(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code, 200)

    
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
