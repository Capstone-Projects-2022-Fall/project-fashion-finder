from django.test import Client, TestCase
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from .models import User
from django.conf import settings as DjangoSettings
import fashionfinderapp.utils as FFUtils
import fashionfinderapp.views as FFViewHandler
import fashionfinderapp.urls as FFURLHandler
import ImgPredMicroservice.upload_piece_to_mongo as MongoHandler 
# import ImgPredMicroservice.class_predict as ImgPredClassPredictHandler
# import ImgPredMicroservice.color_predict as ImgPredColorPredictHandler
from urllib.parse import urlencode

class FFViewsIntegrationAuthenticatedTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        u = User.objects.create_user('foobar', 'foo@bar.com', 'password')
        u.first_name = "Foo"
        u.last_name = "Bar"
        u.save()
        self.User = u
        
        self.pieces = ["63811be6cce90e10a18c413f", "6372e101e5d5ba5ced4ada91", "6372e101e5d5ba5ced4ada95"]

        # Gain user cookie
        http_res = self.client.get('/')
        self.client.cookies['csrftoken']=http_res.cookies['csrftoken']
        csrftoken = http_res.cookies['csrftoken']

        # Authenticate with username and password
        data = urlencode({'username':u.username, 'password':'password','csrfmiddlewaretoken':csrftoken})
        http_res = self.client.post('/accounts/login/',data,content_type="application/x-www-form-urlencoded")
    
    def test_authenticated_user_can_access_home_page(self):
        http_res = self.client.get('/')
        self.assertEqual(http_res.status_code, 200)
        self.assertEqual(type(http_res), HttpResponse)

    def test_authenticated_user_can_access_upload_page(self):
        http_res = self.client.get('/upload/')
        self.assertEqual(http_res.status_code, 200)
        self.assertEqual(type(http_res), HttpResponse)

    def test_authenticated_user_can_access_async_wardrobe_routine(self):
        http_res = self.client.get('/async/wardrobe/')
        self.assertEqual(http_res.status_code, 200)
        self.assertEqual(type(http_res), JsonResponse)
    
    def test_authenticated_user_can_access_async_recommendations_routine(self):
        piece_id = self.pieces[0]

        http_res = self.client.get('/async/recommendations/' + piece_id)
        self.assertEqual(http_res.status_code, 200)
        self.assertEqual(type(http_res), JsonResponse)

    def test_authenticated_user_can_access_async_complementary_recommendations_routine(self):
        piece_id = self.pieces[0]

        http_res = self.client.get('/async/recommendations/complementary/' + piece_id)
        self.assertEqual(http_res.status_code, 200)
        self.assertEqual(type(http_res), JsonResponse)