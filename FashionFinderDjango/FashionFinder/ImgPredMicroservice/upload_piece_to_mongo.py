import io
import numpy as np
from PIL import Image 
from fashionfinderapp.utils import get_db_default_handle
from bson.objectid import ObjectId
CLASS_LIST_21 = ["Tee","Tank","Dress","Shorts","Skirt","Hoodie","Jumpsuit","Sweater","Blazer","Striped","Cardigan","Blouse","Jacket","Jeans","Maxi","Floral","Denim","Sweatshorts","Polka","Shawl","Bodycon"]
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

def get_user_fashion_piece(piece_id = None, user_id = None, user_name = None):
	db_handle, client = get_db_default_handle()
	db = client.fashion_finder_db
	user_collection = db.UserFashionPiece
	recs_collection = db.LabeledFashionPiece
	user_piece = None
	if(piece_id is not None):
		user_piece = user_collection.find_one({"_id":ObjectId(piece_id)})
		print('Piece found')
		print(user_piece['_id'])
	else:
		print("no piece id")
		user_pieces = user_collection.find(
			{"$and": [
				{'user_django_id' : user_id},
				{'user_django_name' : user_name},
			]}
		)
		user_piece = user_pieces[0]
	return user_piece

def get_complementary_clothing_types(class_list=list()):
	if class_list == list():
		return []
	complementary_clothing_type_list = set()
	for target_class in CLASS_LIST_21:
		if(target_class in class_list):
			if target_class == 'Tee':
				for source_class in ['Shorts', 'Hoodie', 'Jacket', 'Jeans','Sweatshorts']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Tank':
				for source_class in ['Shorts', 'Hoodie', 'Jacket', 'Jeans','Sweatshorts']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Dress':
				for source_class in ['Blazer','Leggings','Coat', 'Jacket', 'Cardigan']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Shorts':
				for source_class in ['Tee', 'Tank', 'T-Shirt', 'Shirt', 'Button-Down', 'V-Neck', 'Blouse']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Skirt':
				for source_class in ['Tee', 'Blazer', 'Blouse']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Hoodie':
				for source_class in ['Leggings', 'Pants', 'Jeans', 'T-Shirt', 'Joggers', 'V-Neck', 'Sweatpants']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Jumpsuit':
				for source_class in ['Jacket', 'Blazer', 'Cardigan']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Sweater':
				for source_class in ['Jeans', 'Pants', 'Joggers', 'Sweatpants', 'Leggings']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Blazer':
				for source_class in ['Dress', 'Skirt', 'Jumpsuit', 'V-Neck', 'T-Shirt', 'Shirt', 'Button-Down', 'Romper']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Striped':
				continue # Not a label for determining type of clothing
			if target_class == 'Cardigan':
				for source_class in ['Jumpsuit', 'Jeans', 'Blouse', 'Tank','Turtleneck', 'V-Neck']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Blouse':
				for source_class in ['Cardigan', 'Skirt', 'Shorts', 'Jacket', 'Jeans', 'Dress']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Jacket':
				for source_class in ['Tee', 'Tank', 'Dress', 'Blouse', 'Jumpsuit', 'T-Shirt', 'Shirt', 'Button-Down', 'Romper', 'Jeans']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Jeans':
				for source_class in ['Tee', 'Tank', 'Hoodie','Sweater', 'Cardigan', 'Button-Down', 'Blazer', 'Jacket']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Maxi':
				for source_class in ['Blazer','Coat', 'Jacket', 'Cardigan']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Floral':
				for source_class in ['Blazer','Coat', 'Jacket', 'Cardigan']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Denim':
				for source_class in ['Blazer','Coat', 'Jacket', 'Cardigan']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Sweatshorts':
				for source_class in ['Tee', 'Sweater', 'T-Shirt']:
					complementary_clothing_type_list.add(source_class)
			if target_class == 'Polka':
				continue
			if target_class == 'Shawl':
				continue
			if target_class == 'Bodycon':
				for source_class in ['Jacket', 'Cardigan', 'Jacket', 'Sweater']:
					complementary_clothing_type_list.add(source_class)
	if len(complementary_clothing_type_list) == 0:
		# Safeguard unlabeled clothes
		complementary_clothing_type_list = ['Cardigan', 'Blazer', 'Jacket']
	return list(complementary_clothing_type_list)

			# match target_class:
				# case 'Tee':
					# class_list.append('Shorts')

def get_dominant_color(user_piece_rec):
	# For a given piece, we want to determine which color needs matching.
	# print(user_piece_rec)
	rgb_0 = user_piece_rec['rgb_0']
	rgb_1 = user_piece_rec['rgb_1']
	rgb_2 = user_piece_rec['rgb_2']
	dists = np.array([calculate_min_distance_from_banned_tones(rgb) for rgb in [rgb_0, rgb_1, rgb_2]])
	index = dists.argmax()
	return [rgb_0, rgb_1, rgb_2][index]



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

def calculate_min_distance_from_banned_tones(rgb, tones=BANNED_TONES):
	def calculate_euclidean_distance(rgb1, rgb2):
		rgb_0_diff = rgb1[0] - rgb2[0]
		rgb_1_diff = rgb1[1] - rgb2[1]
		rgb_2_diff = rgb1[2] - rgb2[2]
		return np.sqrt(rgb_0_diff ** 2 + rgb_1_diff ** 2 + rgb_2_diff ** 2)
	min_diff = 255**3
	for tone in tones:
		diff = calculate_euclidean_distance(rgb, tone)
		if(diff < min_diff):
			min_diff = diff
	if(min_diff == 0):
		min_diff = 1
	return min_diff




def get_matching_color_list(h, s, v):
	# Returns 13 colors that "match" the input color, based on the mathematical definitions of analagous, monochrome values
	print("Get matching color list called with values (", h, s, v , ")")

	matching_colors = list()
	# Analagous colors
	analagous_colors = [((h - 30) % 360, s, v), ((h + 30 ) % 360, s, v)]
	matching_colors.extend(analagous_colors)
	complementary_colors = [((h - 180) % 360, s, v)]
	matching_colors.extend(complementary_colors)
	# split_complementary_colors = [((h - 150) % 360, s, v), ((h - 210) % 360, s, v) ]
	# matching_colors.extend(split_complementary_colors)
	saturation_complementary_colors = [(h,(s - diff) % 100,v) for diff in range (-40, 41, 20)]
	matching_colors.extend(saturation_complementary_colors)
	value_complementary_colors = [(h, s, (v-diff) % 100) for diff in range (-40, 41, 20) ]
	matching_colors.extend(value_complementary_colors)
	print(matching_colors)
	return matching_colors



import colorsys


def get_complementary_recommendation(piece_id = None, user_id = None, user_name = None, n = 10):
	user_piece_rec = get_user_fashion_piece(piece_id, user_id, user_name)
	dominant_rgb = get_dominant_color(user_piece_rec)
	print("Dominant RGB ", dominant_rgb)
	print(dominant_rgb)
	labels = get_complementary_clothing_types(user_piece_rec['labels'])
	dom_red = dominant_rgb[0] / 255
	dom_green = dominant_rgb[1] / 255
	dom_blue = dominant_rgb[2] / 255
	dominant_hsv = colorsys.rgb_to_hsv(dom_red, dom_green , dom_blue)
	print("Dominant HSV", dominant_hsv)
	recommended_colors_hsv = get_matching_color_list(dominant_hsv[0] * 360, dominant_hsv[1] * 100, dominant_hsv[2] * 100)
	
	rec_rgb_raw = [colorsys.hsv_to_rgb(c[0] / 360,c[1] / 100 ,c[2] / 100) for c in recommended_colors_hsv]
	rec_rgb = [[rgb[0] * 179, rgb[1] * 255, rgb[2] * 255] for rgb in rec_rgb_raw]
	print("RGB tone recommendations")
	for rec_rgb_item in rec_rgb:
		print (rec_rgb_item)
	# rec_rgb = rec_rgb_raw
	db_handle, client = get_db_default_handle()
	db = client.fashion_finder_db
	recs_collection = db.LabeledFashionPiece

	agg_result = recs_collection.aggregate([
		{
			'$project': {
				# Source = recommended color. Target = DB piece
				'_id': 1,
				'img_data': 1,
				'labels': 1,
				'source_0_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[0][0]]},
				'source_1_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[1][0]]},
				'source_2_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[2][0]]},
				'source_3_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[3][0]]},
				'source_4_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[4][0]]},
				'source_5_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[5][0]]},
				'source_6_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[6][0]]},
				'source_7_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[7][0]]},
				'source_8_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[8][0]]},
				'source_9_red_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[9][0]]},
				'source_10_red_target_0_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[10][0]]},
				'source_11_red_target_0_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[11][0]]},
				'source_12_red_target_0_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_0", 0]}, rec_rgb[12][0]]},

				'source_0_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[0][1]]},
				'source_1_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[1][1]]},
				'source_2_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[2][1]]},
				'source_3_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[3][1]]},
				'source_4_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[4][1]]},
				'source_5_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[5][1]]},
				'source_6_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[6][1]]},
				'source_7_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[7][1]]},
				'source_8_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[8][1]]},
				'source_9_green_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[9][1]]},
				'source_10_green_target_0_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[10][1]]},
				'source_11_green_target_0_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[11][1]]},
				'source_12_green_target_0_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_0", 1]}, rec_rgb[12][1]]},

				'source_0_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[0][2]]},
				'source_1_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[1][2]]},
				'source_2_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[2][2]]},
				'source_3_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[3][2]]},
				'source_4_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[4][2]]},
				'source_5_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[5][2]]},
				'source_6_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[6][2]]},
				'source_7_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[7][2]]},
				'source_8_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[8][2]]},
				'source_9_blue_target_0_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[9][2]]},
				'source_10_blue_target_0_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[10][2]]},
				'source_11_blue_target_0_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[11][2]]},
				'source_12_blue_target_0_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_0", 2]}, rec_rgb[12][2]]},

				# TARGET 1
				'source_0_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[0][0]]},
				'source_1_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[1][0]]},
				'source_2_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[2][0]]},
				'source_3_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[3][0]]},
				'source_4_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[4][0]]},
				'source_5_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[5][0]]},
				'source_6_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[6][0]]},
				'source_7_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[7][0]]},
				'source_8_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[8][0]]},
				'source_9_red_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[9][0]]},
				'source_10_red_target_1_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[10][0]]},
				'source_11_red_target_1_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[11][0]]},
				'source_12_red_target_1_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_1", 0]}, rec_rgb[12][0]]},

				'source_0_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[0][1]]},
				'source_1_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[1][1]]},
				'source_2_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[2][1]]},
				'source_3_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[3][1]]},
				'source_4_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[4][1]]},
				'source_5_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[5][1]]},
				'source_6_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[6][1]]},
				'source_7_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[7][1]]},
				'source_8_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[8][1]]},
				'source_9_green_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[9][1]]},
				'source_10_green_target_1_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[10][1]]},
				'source_11_green_target_1_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[11][1]]},
				'source_12_green_target_1_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_1", 1]}, rec_rgb[12][1]]},

				'source_0_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[0][2]]},
				'source_1_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[1][2]]},
				'source_2_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[2][2]]},
				'source_3_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[3][2]]},
				'source_4_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[4][2]]},
				'source_5_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[5][2]]},
				'source_6_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[6][2]]},
				'source_7_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[7][2]]},
				'source_8_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[8][2]]},
				'source_9_blue_target_1_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[9][2]]},
				'source_10_blue_target_1_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[10][2]]},
				'source_11_blue_target_1_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[11][2]]},
				'source_12_blue_target_1_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_1", 2]}, rec_rgb[12][2]]},
				
				# TARGET 2
				'source_0_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[0][0]]},
				'source_1_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[1][0]]},
				'source_2_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[2][0]]},
				'source_3_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[3][0]]},
				'source_4_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[4][0]]},
				'source_5_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[5][0]]},
				'source_6_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[6][0]]},
				'source_7_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[7][0]]},
				'source_8_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[8][0]]},
				'source_9_red_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[9][0]]},
				'source_10_red_target_2_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[10][0]]},
				'source_11_red_target_2_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[11][0]]},
				'source_12_red_target_2_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_2", 0]}, rec_rgb[12][0]]},

				'source_0_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[0][1]]},
				'source_1_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[1][1]]},
				'source_2_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[2][1]]},
				'source_3_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[3][1]]},
				'source_4_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[4][1]]},
				'source_5_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[5][1]]},
				'source_6_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[6][1]]},
				'source_7_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[7][1]]},
				'source_8_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[8][1]]},
				'source_9_green_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[9][1]]},
				'source_10_green_target_2_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[10][1]]},
				'source_11_green_target_2_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[11][1]]},
				'source_12_green_target_2_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_2", 1]}, rec_rgb[12][1]]},

				'source_0_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[0][2]]},
				'source_1_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[1][2]]},
				'source_2_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[2][2]]},
				'source_3_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[3][2]]},
				'source_4_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[4][2]]},
				'source_5_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[5][2]]},
				'source_6_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[6][2]]},
				'source_7_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[7][2]]},
				'source_8_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[8][2]]},
				'source_9_blue_target_2_diff':  {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[9][2]]},
				'source_10_blue_target_2_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[10][2]]},
				'source_11_blue_target_2_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[11][2]]},
				'source_12_blue_target_2_diff': {'$subtract': [{"$arrayElemAt": ["$rgb_2", 2]}, rec_rgb[12][2]]},
			},
		},
		{
			'$project': {
				'_id': 1,
				'img_data': 1,
				'labels': 1,
				'source_0_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_0_red_target_0_diff','$source_0_red_target_0_diff']},
					{'$multiply': ['$source_0_green_target_0_diff','$source_0_green_target_0_diff']},
					{'$multiply': ['$source_0_blue_target_0_diff','$source_0_blue_target_0_diff']},
				]}},
				'source_0_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_0_red_target_1_diff','$source_0_red_target_1_diff']},
					{'$multiply': ['$source_0_green_target_1_diff','$source_0_green_target_1_diff']},
					{'$multiply': ['$source_0_blue_target_1_diff','$source_0_blue_target_1_diff']},
				]}},
				'source_0_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_0_red_target_2_diff','$source_0_red_target_2_diff']},
					{'$multiply': ['$source_0_green_target_2_diff','$source_0_green_target_2_diff']},
					{'$multiply': ['$source_0_blue_target_2_diff','$source_0_blue_target_2_diff']},
				]}},

				## Source 1
				'source_1_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_1_red_target_0_diff','$source_1_red_target_0_diff']},
					{'$multiply': ['$source_1_green_target_0_diff','$source_1_green_target_0_diff']},
					{'$multiply': ['$source_1_blue_target_0_diff','$source_1_blue_target_0_diff']},
				]}},
				'source_1_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_1_red_target_1_diff','$source_1_red_target_1_diff']},
					{'$multiply': ['$source_1_green_target_1_diff','$source_1_green_target_1_diff']},
					{'$multiply': ['$source_1_blue_target_1_diff','$source_1_blue_target_1_diff']},
				]}},
				'source_1_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_1_red_target_2_diff','$source_1_red_target_2_diff']},
					{'$multiply': ['$source_1_green_target_2_diff','$source_1_green_target_2_diff']},
					{'$multiply': ['$source_1_blue_target_2_diff','$source_1_blue_target_2_diff']},
				]}},
				## Source 2
				'source_2_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_2_red_target_0_diff','$source_2_red_target_0_diff']},
					{'$multiply': ['$source_2_green_target_0_diff','$source_2_green_target_0_diff']},
					{'$multiply': ['$source_2_blue_target_0_diff','$source_2_blue_target_0_diff']},
				]}},
				'source_2_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_2_red_target_1_diff','$source_2_red_target_1_diff']},
					{'$multiply': ['$source_2_green_target_1_diff','$source_2_green_target_1_diff']},
					{'$multiply': ['$source_2_blue_target_1_diff','$source_2_blue_target_1_diff']},
				]}},
				'source_2_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_2_red_target_2_diff','$source_2_red_target_2_diff']},
					{'$multiply': ['$source_2_green_target_2_diff','$source_2_green_target_2_diff']},
					{'$multiply': ['$source_2_blue_target_2_diff','$source_2_blue_target_2_diff']},
				]}},
				## Source 3
				'source_3_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_3_red_target_0_diff','$source_3_red_target_0_diff']},
					{'$multiply': ['$source_3_green_target_0_diff','$source_3_green_target_0_diff']},
					{'$multiply': ['$source_3_blue_target_0_diff','$source_3_blue_target_0_diff']},
				]}},
				'source_3_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_3_red_target_1_diff','$source_3_red_target_1_diff']},
					{'$multiply': ['$source_3_green_target_1_diff','$source_3_green_target_1_diff']},
					{'$multiply': ['$source_3_blue_target_1_diff','$source_3_blue_target_1_diff']},
				]}},
				'source_3_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_3_red_target_2_diff','$source_3_red_target_2_diff']},
					{'$multiply': ['$source_3_green_target_2_diff','$source_3_green_target_2_diff']},
					{'$multiply': ['$source_3_blue_target_2_diff','$source_3_blue_target_2_diff']},
				]}},
				## Source 4
				'source_4_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_4_red_target_0_diff','$source_4_red_target_0_diff']},
					{'$multiply': ['$source_4_green_target_0_diff','$source_4_green_target_0_diff']},
					{'$multiply': ['$source_4_blue_target_0_diff','$source_4_blue_target_0_diff']},
				]}},
				'source_0_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_4_red_target_1_diff','$source_4_red_target_1_diff']},
					{'$multiply': ['$source_4_green_target_1_diff','$source_4_green_target_1_diff']},
					{'$multiply': ['$source_4_blue_target_1_diff','$source_4_blue_target_1_diff']},
				]}},
				'source_4_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_4_red_target_2_diff','$source_4_red_target_2_diff']},
					{'$multiply': ['$source_4_green_target_2_diff','$source_4_green_target_2_diff']},
					{'$multiply': ['$source_4_blue_target_2_diff','$source_4_blue_target_2_diff']},
				]}},
				## Source 5
				'source_5_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_5_red_target_0_diff','$source_5_red_target_0_diff']},
					{'$multiply': ['$source_5_green_target_0_diff','$source_5_green_target_0_diff']},
					{'$multiply': ['$source_5_blue_target_0_diff','$source_5_blue_target_0_diff']},
				]}},
				'source_5_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_5_red_target_1_diff','$source_5_red_target_1_diff']},
					{'$multiply': ['$source_5_green_target_1_diff','$source_5_green_target_1_diff']},
					{'$multiply': ['$source_5_blue_target_1_diff','$source_5_blue_target_1_diff']},
				]}},
				'source_5_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_5_red_target_2_diff','$source_5_red_target_2_diff']},
					{'$multiply': ['$source_5_green_target_2_diff','$source_5_green_target_2_diff']},
					{'$multiply': ['$source_5_blue_target_2_diff','$source_5_blue_target_2_diff']},
				]}},
				## Source 6
				'source_6_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_6_red_target_0_diff','$source_6_red_target_0_diff']},
					{'$multiply': ['$source_6_green_target_0_diff','$source_6_green_target_0_diff']},
					{'$multiply': ['$source_6_blue_target_0_diff','$source_6_blue_target_0_diff']},
				]}},
				'source_6_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_6_red_target_1_diff','$source_6_red_target_1_diff']},
					{'$multiply': ['$source_6_green_target_1_diff','$source_6_green_target_1_diff']},
					{'$multiply': ['$source_6_blue_target_1_diff','$source_6_blue_target_1_diff']},
				]}},
				'source_6_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_6_red_target_2_diff','$source_6_red_target_2_diff']},
					{'$multiply': ['$source_6_green_target_2_diff','$source_6_green_target_2_diff']},
					{'$multiply': ['$source_6_blue_target_2_diff','$source_6_blue_target_2_diff']},
				]}},

				## Source 7
				'source_7_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_7_red_target_0_diff','$source_7_red_target_0_diff']},
					{'$multiply': ['$source_7_green_target_0_diff','$source_7_green_target_0_diff']},
					{'$multiply': ['$source_7_blue_target_0_diff','$source_7_blue_target_0_diff']},
				]}},
				'source_7_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_7_red_target_1_diff','$source_7_red_target_1_diff']},
					{'$multiply': ['$source_7_green_target_1_diff','$source_7_green_target_1_diff']},
					{'$multiply': ['$source_7_blue_target_1_diff','$source_7_blue_target_1_diff']},
				]}},
				'source_7_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_7_red_target_2_diff','$source_7_red_target_2_diff']},
					{'$multiply': ['$source_7_green_target_2_diff','$source_7_green_target_2_diff']},
					{'$multiply': ['$source_7_blue_target_2_diff','$source_7_blue_target_2_diff']},
				]}},
				## Source 8 
				'source_8_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_8_red_target_0_diff','$source_8_red_target_0_diff']},
					{'$multiply': ['$source_8_green_target_0_diff','$source_8_green_target_0_diff']},
					{'$multiply': ['$source_8_blue_target_0_diff','$source_8_blue_target_0_diff']},
				]}},
				'source_8_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_8_red_target_1_diff','$source_8_red_target_1_diff']},
					{'$multiply': ['$source_8_green_target_1_diff','$source_8_green_target_1_diff']},
					{'$multiply': ['$source_8_blue_target_1_diff','$source_8_blue_target_1_diff']},
				]}},
				'source_8_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_8_red_target_2_diff','$source_8_red_target_2_diff']},
					{'$multiply': ['$source_8_green_target_2_diff','$source_8_green_target_2_diff']},
					{'$multiply': ['$source_8_blue_target_2_diff','$source_8_blue_target_2_diff']},
				]}},

				## Source 9
				'source_9_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_9_red_target_0_diff','$source_9_red_target_0_diff']},
					{'$multiply': ['$source_9_green_target_0_diff','$source_9_green_target_0_diff']},
					{'$multiply': ['$source_9_blue_target_0_diff','$source_9_blue_target_0_diff']},
				]}},
				'source_9_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_9_red_target_1_diff','$source_9_red_target_1_diff']},
					{'$multiply': ['$source_9_green_target_1_diff','$source_9_green_target_1_diff']},
					{'$multiply': ['$source_9_blue_target_1_diff','$source_9_blue_target_1_diff']},
				]}},
				'source_9_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_9_red_target_2_diff','$source_9_red_target_2_diff']},
					{'$multiply': ['$source_9_green_target_2_diff','$source_9_green_target_2_diff']},
					{'$multiply': ['$source_9_blue_target_2_diff','$source_9_blue_target_2_diff']},
				]}},
				## Source 10
				'source_10_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_10_red_target_0_diff','$source_10_red_target_0_diff']},
					{'$multiply': ['$source_10_green_target_0_diff','$source_10_green_target_0_diff']},
					{'$multiply': ['$source_10_blue_target_0_diff','$source_10_blue_target_0_diff']},
				]}},
				'source_10_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_10_red_target_1_diff','$source_10_red_target_1_diff']},
					{'$multiply': ['$source_10_green_target_1_diff','$source_10_green_target_1_diff']},
					{'$multiply': ['$source_10_blue_target_1_diff','$source_10_blue_target_1_diff']},
				]}},
				'source_10_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_10_red_target_2_diff','$source_10_red_target_2_diff']},
					{'$multiply': ['$source_10_green_target_2_diff','$source_10_green_target_2_diff']},
					{'$multiply': ['$source_10_blue_target_2_diff','$source_10_blue_target_2_diff']},
				]}},
				## Source 11
				'source_11_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_11_red_target_0_diff','$source_11_red_target_0_diff']},
					{'$multiply': ['$source_11_green_target_0_diff','$source_11_green_target_0_diff']},
					{'$multiply': ['$source_11_blue_target_0_diff','$source_11_blue_target_0_diff']},
				]}},
				'source_11_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_11_red_target_1_diff','$source_11_red_target_1_diff']},
					{'$multiply': ['$source_11_green_target_1_diff','$source_11_green_target_1_diff']},
					{'$multiply': ['$source_11_blue_target_1_diff','$source_11_blue_target_1_diff']},
				]}},
				'source_11_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_11_red_target_2_diff','$source_11_red_target_2_diff']},
					{'$multiply': ['$source_11_green_target_2_diff','$source_11_green_target_2_diff']},
					{'$multiply': ['$source_11_blue_target_2_diff','$source_11_blue_target_2_diff']},
				]}},
				## Source 12
				'source_12_target_0_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_12_red_target_0_diff','$source_12_red_target_0_diff']},
					{'$multiply': ['$source_12_green_target_0_diff','$source_12_green_target_0_diff']},
					{'$multiply': ['$source_12_blue_target_0_diff','$source_12_blue_target_0_diff']},
				]}},
				'source_12_target_1_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_12_red_target_1_diff','$source_12_red_target_1_diff']},
					{'$multiply': ['$source_12_green_target_1_diff','$source_12_green_target_1_diff']},
					{'$multiply': ['$source_12_blue_target_1_diff','$source_12_blue_target_1_diff']},
				]}},
				'source_12_target_2_dist': {'$sqrt':{'$sum': [
					{'$multiply': ['$source_12_red_target_2_diff','$source_12_red_target_2_diff']},
					{'$multiply': ['$source_12_green_target_2_diff','$source_12_green_target_2_diff']},
					{'$multiply': ['$source_12_blue_target_2_diff','$source_12_blue_target_2_diff']},
				]}},
			},

		},
		{
			'$project': {
				'_id': 1,
				'img_data': 1,
				'labels': 1,
				'source_0_min_dist': {'$min':['$source_0_target_0_dist','$source_0_target_1_dist','$source_0_target_2_dist']},
				'source_1_min_dist': {'$min':['$source_1_target_0_dist','$source_1_target_1_dist','$source_1_target_2_dist']},
				'source_2_min_dist': {'$min':['$source_2_target_0_dist','$source_2_target_1_dist','$source_2_target_2_dist']},
				'source_3_min_dist': {'$min':['$source_3_target_0_dist','$source_3_target_1_dist','$source_3_target_2_dist']},
				# 'source_4_min_dist': {'$min':['$source_4_target_0_dist','$source_4_target_1_dist','$source_4_target_2_dist']},
				# 'source_5_min_dist': {'$min':['$source_5_target_0_dist','$source_5_target_1_dist','$source_5_target_2_dist']},
				# 'source_6_min_dist': {'$min':['$source_6_target_0_dist','$source_6_target_1_dist','$source_6_target_2_dist']},
				# 'source_7_min_dist': {'$min':['$source_7_target_0_dist','$source_7_target_1_dist','$source_7_target_2_dist']},
				# 'source_8_min_dist': {'$min':['$source_8_target_0_dist','$source_8_target_1_dist','$source_8_target_2_dist']},
				# 'source_9_min_dist': {'$min':['$source_9_target_0_dist','$source_9_target_1_dist','$source_9_target_2_dist']},
				# 'source_10_min_dist': {'$min':['$source_10_target_0_dist','$source_10_target_1_dist','$source_10_target_2_dist']},
				# 'source_11_min_dist': {'$min':['$source_11_target_0_dist','$source_11_target_1_dist','$source_11_target_2_dist']},
				# 'source_12_min_dist': {'$min':['$source_12_target_0_dist','$source_12_target_1_dist','$source_12_target_2_dist']},
			},

		},
		{
			'$project': {
				'_id': 1,
				'img_data': 1,
				'labels': 1,
				'min_dist': {"$min": ['$source_0_min_dist','$source_1_min_dist','$source_2_min_dist','$source_3_min_dist']}
				# 'min_dist': {"$min": ['$source_0_min_dist','$source_1_min_dist','$source_2_min_dist','$source_3_min_dist','$source_4_min_dist','$source_5_min_dist','$source_6_min_dist','$source_7_min_dist','$source_8_min_dist','$source_9_min_dist','$source_10_min_dist','$source_11_min_dist','$source_12_min_dist']}
			},
		},
		{
			'$match': {
				"labels": {"$elemMatch": {"$in":labels} } 
			},
		},
		{
			'$sort': {'min_dist': 1},
		},
		{
			'$limit': 10
		},
			
	])
	return agg_result, user_piece_rec
	# return get_recommendations(piece_id, user_id, user_name , n)

def get_recommendations(piece_id = None, user_id = None, user_name = None, n = 10):
	user_piece_rec = get_user_fashion_piece(piece_id, user_id, user_name)
		# user_pieces = user
	# if(piece_id is not None){
	# 	# user_pieces = user_collection.find({"_id":piece_id})
	# 	print("huh")
	# } else {
	# }
	db_handle, client = get_db_default_handle()
	db = client.fashion_finder_db
	recs_collection = db.LabeledFashionPiece
	
	rgb_0_weight =  1 / calculate_min_distance_from_banned_tones(user_piece_rec['rgb_0'])
	rgb_1_weight = 1 / calculate_min_distance_from_banned_tones(user_piece_rec['rgb_1'])
	rgb_2_weight = 1 / calculate_min_distance_from_banned_tones(user_piece_rec['rgb_2'])

	labels = user_piece_rec['labels']

	if 'Jeans' in labels:
		labels.append('Chino')

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
				"labels": 1,
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
				"labels": 1,
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
				"labels": 1,
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
		{	# Calculate the Weighted Min distance
			"$project": {
				"_id": 1,
				"img_data": 1,
				"labels": 1,
				"hex_codes": 1,
				"rgb_0": 1,
				"rgb_1": 1,
				"rgb_2": 1,
				"labels": 1,
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
			"$match": {
				"labels": {"$elemMatch": {"$in":labels} } 
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
