import io
from PIL import Image 
from fashionfinderapp.utils import get_db_default_handle

def create_user_fashion_piece(data, img_bytes):
    fashion_piece_doc = {}
    try:
        db_handle, client = get_db_default_handle()
        fashion_piece_doc = {
            'img_data': img_bytes.getvalue(),
            'labels': data['labels'],
            'hex_codes': data['hex_codes'],
            'descriptor': data['descriptor'],
            'rgb_0': data['rgb_0'],
            'rgb_1': data['rgb_1'],
            'rgb_2': data['rgb_2'],
            'user_django_id': data['user_django_id'],
        }
    except:
        return None
    return fashion_piece_doc

def insert_user_fashion_piece(mongo_doc):
    db_handle, client = get_db_default_handle()
    db = client.fashion_finder_db
    collection = db.UserFashionPiece
    mongo_insert_one_result = collection.insert_one(mongo_doc)
    if(mongo_insert_one_result):
        m_id = mongo_insert_one_result.inserted_id
    else:
        m_id = None
    return m_id
	