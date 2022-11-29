from django.test import Client, TestCase
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect, HttpResponsePermanentRedirect
from .models import User
from django.conf import settings as DjangoSettings
import fashionfinderapp.utils as FFUtils
import fashionfinderapp.views as FFViewHandler
import fashionfinderapp.urls as FFURLHandler
import ImgPredMicroservice.upload_piece_to_mongo as MongoHandler 
# import ImgPredMicroservice.class_predict as ImgPredClassPredictHandler
# import ImgPredMicroservice.color_predict as ImgPredColorPredictHandler

class FFViewsIntegrationTests(TestCase):
    def setUp(self):        
        self.client = Client()
        u = User.objects.create_user('foobar', 'foo@bar.com', 'password')
        u.first_name = "Foo"
        u.last_name = "Bar"
        u.save()
        self.User = u
        
        # Gain user cookie
        http_res = self.client.get('/')
        self.client.cookies['csrftoken']=http_res.cookies['csrftoken']

    def test_unauthenticated_user_index(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code , 200)

    def test_unauthenticated_user_index_receives_cookie(self):
        local_client = Client()
        http_res = local_client.get('/')
        cookie_keys = http_res.cookies.keys()
        self.assertIn('csrftoken', cookie_keys)
    
    def test_unauthenticated_user_login_user_does_not_exist(self):
        http_res = self.client.post('/accounts/login',data={'username':'IDontExist', 'password':''})
        self.assertEqual(type(http_res), HttpResponsePermanentRedirect)
        self.assertEqual(http_res.status_code, 301)
        self.assertEqual(http_res.url, '/accounts/login/')

    def test_unauthenticated_user_login_wrong_password(self):
        http_res = self.client.post('/accounts/login',data={'username':'foobar', 'password':'wrong_password'})
        self.assertEqual(type(http_res), HttpResponsePermanentRedirect)
        self.assertEqual(http_res.status_code, 301)
        self.assertEqual(http_res.url, '/accounts/login/')
    
    def test_unauthenticated_user_login_wrong_password_with_email(self):
        http_res = self.client.post('/accounts/login',data={'username':'foo@bar.com', 'password':'wrong_password'})
        self.assertEqual(type(http_res), HttpResponsePermanentRedirect)
        self.assertEqual(http_res.status_code, 301)
        self.assertEqual(http_res.url, '/accounts/login/')


    def test_unauthenticated_user_login_correct_password(self):
        from urllib.parse import urlencode
        local_client = Client()
        http_res = local_client.get('/')
        csrftoken = http_res.cookies['csrftoken']
        data = urlencode({'username':'foobar', 'password':'password','csrfmiddlewaretoken':csrftoken})
        http_res = self.client.post('/accounts/login/',data,content_type="application/x-www-form-urlencoded")
        self.assertEqual(type(http_res), HttpResponseRedirect)
        self.assertEqual(http_res.status_code, 302)
        http_res_2 = self.client.get('/wardrobe/')
        self.assertEqual(http_res_2.status_code, 200)