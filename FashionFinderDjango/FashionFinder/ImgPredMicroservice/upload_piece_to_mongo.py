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

def get_wardrobe(user_id, n = 10):
	db_handle, client = get_db_default_handle()
	db = client.fashion_finder_db

	user_collection = db.UserFashionPiece
	recs_collection = db.FashionPiece

	user_pieces = user_collection.find({'user_django_id':user_id})
	return user_pieces



def get_recommendations(user_id, n = 10):
	db_handle, client = get_db_default_handle()
	db = client.fashion_finder_db

	user_collection = db.UserFashionPiece
	recs_collection = db.LabeledFashionPiece

	user_pieces = user_collection.find({'user_django_id' : user_id})
	user_piece_rec = user_pieces[0]
	labels = user_piece_rec['labels']
	rgb_0 = user_piece_rec['rgb_0']
	print(rgb_0)
	print(labels)
	# recs_collection.find({'$and': [
	# 	'labels':
	# ]})

	# We want a recommendation algorithm that finds clothing with similar labels and 
	# satisfies the following condition
	#
	#
	#
	#
	# rec_pieces = recs_collection.find({"labels":
	# 									{"$elemMatch": 
	# 										{"$in": labels}
	# 									}
	# 								})
									
	# rec_pieces = recs_collection.find({"rgb_0.0":36})
	
	# rec_pieces = recs_collection.find({"rgb_0.0":{
	# 									"$and":[
	# 										{"$lt":41},
	# 										{"$gt":31},
	# 									]
	# 								}})
	# Final all pieces between 31 and 41 red value for rgb_0
	# rec_pieces = list(recs_collection.find({"$and": [
	# 									{"rgb_0.0": {"$lt":33}},
	# 									{"rgb_0.0": {"$gt":31}},

	# 								]}))

	delta = 20 # Allow for 20 units of variation in each piece

	rgb_0_0_match_query = {"$and": [
		{"rgb_0.0": {"$lt":rgb_0[0] + delta}},
		{"rgb_0.0": {"$gt":rgb_0[0] - delta}},
		{"rgb_0.1": {"$lt":rgb_0[1] + delta}},
		{"rgb_0.1": {"$gt":rgb_0[1] - delta}},
		{"rgb_0.2": {"$gt":rgb_0[2] + delta}},
		{"rgb_0.2": {"$gt":rgb_0[2] - delta}},
	]}
	if "Dress" in labels:
		rec_labels = "Blazer"
	rec_pieces = recs_collection.find({"$and": [
									{"$and": [
										{"rgb_0.0": {"$lt":rgb_0[0] + delta}},
										{"rgb_0.0": {"$gt":rgb_0[0] - delta}},
										{"rgb_0.1": {"$lt":rgb_0[1] + delta}},
										{"rgb_0.1": {"$gt":rgb_0[1] - delta}},
										{"rgb_0.2": {"$gt":rgb_0[2] + delta}},
										{"rgb_0.2": {"$gt":rgb_0[2] - delta}},
									]},
									{"labels":
										{"$elemMatch": 
											{"$in": [rec_labels]}
										}
									}
								]})
	return rec_pieces, user_piece_rec