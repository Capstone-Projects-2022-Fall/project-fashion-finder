import io
import numpy as np
from PIL import Image 
from fashionfinderapp.utils import get_db_default_handle
from bson.objectid import ObjectId
BANNED_TONES = [
[60, 46, 40],
[75, 57, 50],
[90, 69, 60],
[105, 80, 70],
[120, 92, 80],
[135, 103, 90],
[150, 114, 100],
[165, 126, 110],
[180, 138, 120],
[195, 149, 130],
[210, 161, 140],
[225, 172, 150],
[240, 184, 160],
[255, 195, 170],
[255, 206, 180],
[255, 255, 255],
[220, 220, 220],
[200, 200, 200],
[180, 180, 180],
[160, 160, 160],
[140, 140, 140],
[120, 120, 120],
[100, 100, 100],
[80, 80, 80],
[60, 60, 60],
[40, 40, 40],
[20, 20, 20],
[0, 0, 0]

]
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
			'user_django_name': data['user_django_name'],
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

def get_wardrobe(user_id, user_name, n = 10):
	db_handle, client = get_db_default_handle()
	db = client.fashion_finder_db

	user_collection = db.UserFashionPiece
	recs_collection = db.FashionPiece

	user_pieces = user_collection.find(	{"$and": [
			{'user_django_id' : user_id},
			{'user_django_name' : user_name},

		]})
	return user_pieces

def calculate_min_distance_from_skin_tone(rgb, skin_tones=BANNED_TONES):
	def calculate_euclidean_distance(rgb1, rgb2):
		rgb_0_diff = rgb1[0] - rgb2[0]
		rgb_1_diff = rgb1[1] - rgb2[1]
		rgb_2_diff = rgb1[2] - rgb2[2]
		return np.sqrt(rgb_0_diff ** 2 + rgb_1_diff ** 2 + rgb_2_diff ** 2)
	min_diff = 255**3
	for skin_tone in skin_tones:
		diff = calculate_euclidean_distance(rgb, skin_tone)
		if(diff < min_diff):
			min_diff = diff
	if(min_diff == 0):
		min_diff = 1
	return min_diff

def get_recommendations(piece_id = None, user_id = None, user_name = None, n = 10):
	db_handle, client = get_db_default_handle()
	db = client.fashion_finder_db
	user_collection = db.UserFashionPiece
	recs_collection = db.LabeledFashionPiece
	user_piece_rec = None
	if(piece_id is not None):
		user_piece_rec = user_collection.find_one({"_id":ObjectId(piece_id)})
		print('Piece found')
		print(user_piece_rec['_id'])
	else:
		print("no piece id")
		user_pieces = user_collection.find(
			{"$and": [
				{'user_django_id' : user_id},
				{'user_django_name' : user_name},
			]}
		)
		user_piece_rec = user_pieces[0]
		# user_pieces = user
	# if(piece_id is not None){
	# 	# user_pieces = user_collection.find({"_id":piece_id})
	# 	print("huh")
	# } else {
	# }
	
	rgb_0_weight =  1 / calculate_min_distance_from_skin_tone(user_piece_rec['rgb_0'])
	rgb_1_weight = 1 / calculate_min_distance_from_skin_tone(user_piece_rec['rgb_1'])
	rgb_2_weight = 1 / calculate_min_distance_from_skin_tone(user_piece_rec['rgb_2'])

	print(rgb_0_weight, rgb_1_weight, rgb_2_weight)
	agg_results = recs_collection.aggregate([
		{
			"$project": {
				"_id": 1,
				"img_data": 1,
				"labels": 1,
				"hex_codes": 1,
				"rgb_0": 1,
				"rgb_1": 1,
				"rgb_2": 1,
				"descriptor": 1,

				# RGB_SOURCE_TARGET_RGB_INDEX_diff
				# 0 0
				"rgb_0_0_0_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_0", 0]}, user_piece_rec["rgb_0"][0] ] },
				"rgb_0_0_1_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_0", 1]}, user_piece_rec["rgb_0"][1] ] },
				"rgb_0_0_2_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_0", 2]}, user_piece_rec["rgb_0"][2] ] },
				
				# 0 1
				"rgb_0_1_0_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_0", 0]}, user_piece_rec["rgb_1"][0] ] },
				"rgb_0_1_1_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_0", 1]}, user_piece_rec["rgb_1"][1] ] },
				"rgb_0_1_2_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_0", 2]}, user_piece_rec["rgb_1"][2] ] },

				# 0 2
				"rgb_0_2_0_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_0", 0]}, user_piece_rec["rgb_2"][0] ] },
				"rgb_0_2_1_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_0", 1]}, user_piece_rec["rgb_2"][1] ] },
				"rgb_0_2_2_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_0", 2]}, user_piece_rec["rgb_2"][2] ] },

				# 1 0
				"rgb_1_0_0_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_1", 0]}, user_piece_rec["rgb_0"][0] ] },
				"rgb_1_0_1_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_1", 1]}, user_piece_rec["rgb_0"][1] ] },
				"rgb_1_0_2_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_1", 2]}, user_piece_rec["rgb_0"][2] ] },

				# 1 1
				"rgb_1_1_0_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_1", 0]}, user_piece_rec["rgb_1"][0] ] },
				"rgb_1_1_1_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_1", 1]}, user_piece_rec["rgb_1"][1] ] },
				"rgb_1_1_2_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_1", 2]}, user_piece_rec["rgb_1"][2] ] },

				# 1 2
				"rgb_1_2_0_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_1", 0]}, user_piece_rec["rgb_2"][0] ] },
				"rgb_1_2_1_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_1", 1]}, user_piece_rec["rgb_2"][1] ] },
				"rgb_1_2_2_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_1", 2]}, user_piece_rec["rgb_2"][2] ] },
				
				# 2 0
				"rgb_2_0_0_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_2", 0]}, user_piece_rec["rgb_0"][0] ] },
				"rgb_2_0_1_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_2", 1]}, user_piece_rec["rgb_0"][1] ] },
				"rgb_2_0_2_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_2", 2]}, user_piece_rec["rgb_0"][2] ] },

				# 2 1
				"rgb_2_1_0_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_2", 0]}, user_piece_rec["rgb_1"][0] ] },
				"rgb_2_1_1_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_2", 1]}, user_piece_rec["rgb_1"][1] ] },
				"rgb_2_1_2_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_2", 2]}, user_piece_rec["rgb_1"][2] ] },

				# 2 2
				"rgb_2_2_0_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_2", 0]}, user_piece_rec["rgb_2"][0] ] },
				"rgb_2_2_1_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_2", 1]}, user_piece_rec["rgb_2"][1] ] },
				"rgb_2_2_2_diff": {"$subtract": [{"$arrayElemAt": ["$rgb_2", 2]}, user_piece_rec["rgb_2"][2] ] },


			},
		},
		{
			"$project": {
				"_id": 1,
				"img_data": 1,
				"labels": 1,
				"hex_codes": 1,
				"rgb_0": 1,
				"rgb_1": 1,
				"rgb_2": 1,
				"descriptor": 1,

				# Calculate the euclidean distance for each pairing of hex codes 
				"rgb_0_0_euclid": {"$sum": [
					{"$multiply": ["$rgb_0_0_0_diff", "$rgb_0_0_0_diff"]},
					{"$multiply": ["$rgb_0_0_1_diff", "$rgb_0_0_1_diff"]},
					{"$multiply": ["$rgb_0_0_2_diff", "$rgb_0_0_2_diff"]},
				]},

				"rgb_0_1_euclid": {"$sum": [
					{"$multiply": ["$rgb_0_1_0_diff", "$rgb_0_1_0_diff"]},
					{"$multiply": ["$rgb_0_1_1_diff", "$rgb_0_1_1_diff"]},
					{"$multiply": ["$rgb_0_1_2_diff", "$rgb_0_1_2_diff"]},
				]},

				"rgb_0_2_euclid": {"$sum": [
					{"$multiply": ["$rgb_0_2_0_diff", "$rgb_0_2_0_diff"]},
					{"$multiply": ["$rgb_0_2_1_diff", "$rgb_0_2_1_diff"]},
					{"$multiply": ["$rgb_0_2_2_diff", "$rgb_0_2_2_diff"]},
				]},

				"rgb_1_0_euclid": {"$sum": [
					{"$multiply": ["$rgb_1_0_0_diff", "$rgb_1_0_0_diff"]},
					{"$multiply": ["$rgb_1_0_1_diff", "$rgb_1_0_1_diff"]},
					{"$multiply": ["$rgb_1_0_2_diff", "$rgb_1_0_2_diff"]},
				]},

				"rgb_1_1_euclid": {"$sum": [
					{"$multiply": ["$rgb_1_1_0_diff", "$rgb_1_1_0_diff"]},
					{"$multiply": ["$rgb_1_1_1_diff", "$rgb_1_1_1_diff"]},
					{"$multiply": ["$rgb_1_1_2_diff", "$rgb_1_1_2_diff"]},
				]},

				"rgb_1_2_euclid": {"$sum": [
					{"$multiply": ["$rgb_1_1_0_diff", "$rgb_1_1_0_diff"]},
					{"$multiply": ["$rgb_1_1_1_diff", "$rgb_1_1_1_diff"]},
					{"$multiply": ["$rgb_1_1_2_diff", "$rgb_1_1_2_diff"]},
				]},

				"rgb_2_0_euclid": {"$sum": [
					{"$multiply": ["$rgb_2_0_0_diff", "$rgb_2_0_0_diff"]},
					{"$multiply": ["$rgb_2_0_1_diff", "$rgb_2_0_1_diff"]},
					{"$multiply": ["$rgb_2_0_2_diff", "$rgb_2_0_2_diff"]},
				]},

				"rgb_2_1_euclid": {"$sum": [
					{"$multiply": ["$rgb_2_1_0_diff", "$rgb_2_1_0_diff"]},
					{"$multiply": ["$rgb_2_1_1_diff", "$rgb_2_1_1_diff"]},
					{"$multiply": ["$rgb_2_1_2_diff", "$rgb_2_1_2_diff"]},
				]},

				"rgb_2_2_euclid": {"$sum": [
					{"$multiply": ["$rgb_2_2_0_diff", "$rgb_2_2_0_diff"]},
					{"$multiply": ["$rgb_2_2_1_diff", "$rgb_2_2_1_diff"]},
					{"$multiply": ["$rgb_2_2_2_diff", "$rgb_2_2_2_diff"]},
				]},


			}
		},
		{
			"$project": {
				"_id": 1,
				"img_data": 1,
				"labels": 1,
				"hex_codes": 1,
				"rgb_0": 1,
				"rgb_1": 1,
				"rgb_2": 1,
				"descriptor": 1,
				"rgb_0_0_euclid": 1,
				"rgb_0_1_euclid": 1,
				"rgb_0_2_euclid": 1,
				"rgb_1_0_euclid": 1,
				"rgb_1_1_euclid": 1,
				"rgb_1_2_euclid": 1,
				"rgb_2_0_euclid": 1,
				"rgb_2_1_euclid": 1,
				"rgb_2_2_euclid": 1,

				"min_0_distance": {"$min":["$rgb_0_0_euclid", "$rgb_1_0_euclid", "$rgb_2_0_euclid"]},
				"min_1_distance": {"$min":["$rgb_0_1_euclid", "$rgb_1_1_euclid", "$rgb_2_1_euclid"]},
				"min_2_distance": {"$min":["$rgb_0_2_euclid", "$rgb_1_2_euclid", "$rgb_2_2_euclid"]},
			}
		},
		{
			"$project": {
				"_id": 1,
				"img_data": 1,
				"labels": 1,
				"hex_codes": 1,
				"rgb_0": 1,
				"rgb_1": 1,
				"rgb_2": 1,
				"descriptor": 1,
				"img_data": 1,
				"min_0_distance": 1,
				"min_1_distance": 1,
				"min_2_distance": 1,

				"weighted_min_distance": {"$sum": [
					{"$multiply": ["$min_0_distance", rgb_0_weight]},
					{"$multiply": ["$min_1_distance", rgb_1_weight]},
					{"$multiply": ["$min_2_distance", rgb_2_weight]},
				]}

			}
		},

		{
			"$sort": {"weighted_min_distance": 1},
		},

		{
			"$limit": n

		}
	])

	return agg_results, user_piece_rec
