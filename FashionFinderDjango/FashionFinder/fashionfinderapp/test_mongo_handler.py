from django.test import Client, TestCase
from django.urls import reverse
from .models import User
from django.conf import settings as DjangoSettings
import fashionfinderapp.utils as FFUtils
import fashionfinderapp.views as FFViewHandler
import fashionfinderapp.urls as FFURLHandler
import ImgPredMicroservice.upload_piece_to_mongo as MongoHandler 
import ImgPredMicroservice.class_predict as ImgPredClassPredictHandler
import ImgPredMicroservice.color_predict as ImgPredColorPredictHandler
import PIL
import io

REF_DICT = {
    'Tee': ['Shorts', 'Hoodie', 'Jacket', 'Jeans','Sweatshorts'] ,
    'Tank': ['Shorts', 'Hoodie', 'Jacket', 'Jeans','Sweatshorts'] ,
    'Dress': ['Blazer','Leggings','Coat', 'Jacket', 'Cardigan'] ,
    'Shorts': ['Tee', 'Tank', 'T-Shirt', 'Shirt', 'Button-Down', 'V-Neck', 'Blouse'],
    'Skirt': ['Tee', 'Blazer', 'Blouse'] ,
    'Hoodie': ['Leggings', 'Pants', 'Jeans', 'T-Shirt', 'Joggers', 'V-Neck', 'Sweatpants'] ,
    'Jumpsuit': ['Jacket', 'Blazer', 'Cardigan'],
    'Sweater': ['Jeans', 'Pants', 'Joggers', 'Sweatpants', 'Leggings'],
    'Blazer': ['Dress', 'Skirt', 'Jumpsuit', 'V-Neck', 'T-Shirt', 'Shirt', 'Button-Down', 'Romper'],
    'Striped': ['Cardigan', 'Blazer', 'Jacket'],
    'Cardigan': ['Jumpsuit', 'Jeans', 'Blouse', 'Tank','Turtleneck', 'V-Neck'],
    'Blouse': ['Cardigan', 'Skirt', 'Shorts', 'Jacket', 'Jeans', 'Dress'],
    'Jacket': ['Tee', 'Tank', 'Dress', 'Blouse', 'Jumpsuit', 'T-Shirt', 'Shirt', 'Button-Down', 'Romper', 'Jeans'],
    'Jeans': ['Tee', 'Tank', 'Hoodie','Sweater', 'Cardigan', 'Button-Down', 'Blazer', 'Jacket'],
    'Maxi': ['Blazer','Coat', 'Jacket', 'Cardigan'],
    'Floral': ['Blazer','Coat', 'Jacket', 'Cardigan'],
    'Denim': ['Blazer','Coat', 'Jacket', 'Cardigan'],
    'Sweatshorts': ['Tee', 'Sweater', 'T-Shirt'] ,
    'Polka': ['Cardigan', 'Blazer', 'Jacket'],
    'Shawl': ['Cardigan', 'Blazer', 'Jacket'],
    'Bodycon': ['Cardigan', 'Sweater', 'Jacket'],
}
class MongoDocumentCreationTests(TestCase):
    def setUp(self):
        self.db_handle, self.client = FFUtils.get_db_default_handle()
        self.UserFashionPiecesCollection = self.client['fashion_finder_db']['FashionPiece']
        self.MongoHandler = MongoHandler
        self.test_images_dir = DjangoSettings.USER_UPLOAD_ROOT + 'images/test/'
        data = {}
        data['labels'] = ['Tee', 'Tank']
        data['descriptor'] = 'FullSize_White_Tank_Top'
        data['hex_codes'] = ["6C645F","EFEDEC","B6AEAA"]
        data["rgb_0"] = [108, 100, 95]
        data["rgb_1"] = [239, 237, 236]
        data["rgb_2"] = [182, 174, 170]
        data['user_django_id'] = 10000
        data['user_django_name'] = 'TestUser'
        self.data = data
        self.piece_id = '6372c4146a17ad72dc478018' 
        filepath = '6372c4146a17ad72dc478018.jpg'
        im = PIL.Image.open(self.test_images_dir + filepath)
        self.img_bytes = io.BytesIO()
        im.save(self.img_bytes, format='JPEG')
    def test_create_user_piece(self):
        mongo_doc = MongoHandler.create_user_fashion_piece(self.data, self.img_bytes)
        self.assertNotEqual(mongo_doc, None)

    def test_create_and_insert_user_piece(self):
        mongo_doc = MongoHandler.create_user_fashion_piece(self.data, self.img_bytes)
        self.assertNotEqual(mongo_doc, None)

        inserted_id = MongoHandler.insert_user_fashion_piece(mongo_doc)
        self.assertNotEqual(inserted_id, None)
    
    def test_create_insert_and_get_user_piece(self):
        mongo_doc = MongoHandler.create_user_fashion_piece(self.data, self.img_bytes)
        self.assertNotEqual(mongo_doc, None)
        
        inserted_id = MongoHandler.insert_user_fashion_piece(mongo_doc)
        self.assertNotEqual(inserted_id, None)

        retrieved_doc = MongoHandler.get_user_fashion_piece(piece_id=inserted_id)

        for key in self.data.keys():
            self.assertEqual(self.data[key], retrieved_doc[key])
   
    def test_get_complementary_clothing_types(self):

        for (key,value) in REF_DICT.items():
            print(key)
            class_list = MongoHandler.get_complementary_clothing_types([key])
            class_list.sort()
            value.sort()
            self.assertListEqual(class_list, value)

    def test_get_dominant_color(self):
        test_data = {'rgb_0': [0,0,0], 'rgb_1': [255, 255, 255], 'rgb_2':[255, 0, 0]}
        dominant_color = MongoHandler.get_dominant_color(test_data)
        self.assertEqual(test_data['rgb_2'], dominant_color)

    def test_get_wardrobe(self):
        mongo_doc = MongoHandler.create_user_fashion_piece(self.data, self.img_bytes)
        self.assertNotEqual(mongo_doc, None)

        inserted_id = MongoHandler.insert_user_fashion_piece(mongo_doc)
        self.assertNotEqual(inserted_id, None)

        user_pieces = MongoHandler.get_wardrobe(user_id=10000, user_name='TestUser')
        self.assertNotEqual(len(list(user_pieces)), 0)

    def test_get_matching_color_list(self):
        test_hsv = (180, 50, 50)
        expected_result = [(150, 50, 50), (210, 50, 50), (135, 50, 50), (0, 50, 50), (225, 50, 50), (180, 10, 50), (180, 30, 50), (180, 70, 50), (180, 90, 50), (180, 50, 10), (180, 50, 30), (180, 50, 70), (180, 50, 90) ]
        matching_colors = MongoHandler.get_matching_color_list(test_hsv[0], test_hsv[1], test_hsv[2])
        self.assertEqual(len(expected_result), len(matching_colors))
        for color in matching_colors:
            self.assertIn(color, expected_result)
    
    def test_get_complementary_recommendations(self):
        mongo_doc = MongoHandler.create_user_fashion_piece(self.data, self.img_bytes)
        self.assertNotEqual(mongo_doc, None)

        inserted_id = MongoHandler.insert_user_fashion_piece(mongo_doc)
        self.assertNotEqual(inserted_id, None)
        agg_result, user_piece_rec = MongoHandler.get_complementary_recommendation(piece_id = inserted_id)

        self.assertNotEqual(agg_result, None)
        self.assertNotEqual(user_piece_rec, None)
        for key in self.data.keys():
            self.assertEqual(self.data[key], user_piece_rec[key])

    def test_get_recommendations(self):
        mongo_doc = MongoHandler.create_user_fashion_piece(self.data, self.img_bytes)
        self.assertNotEqual(mongo_doc, None)

        inserted_id = MongoHandler.insert_user_fashion_piece(mongo_doc)
        self.assertNotEqual(inserted_id, None)
        agg_result, user_piece_rec = MongoHandler.get_recommendations(piece_id = inserted_id)

        self.assertNotEqual(agg_result, None)
        self.assertNotEqual(user_piece_rec, None)
        for key in self.data.keys():
            self.assertEqual(self.data[key], user_piece_rec[key])