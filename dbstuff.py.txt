import gridfs
from pymongo import MongoClient
import gridfs
import pymongo
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio import start_server
from pymongo import MongoClient
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List




# Connect to the server with the hostName and portNumber.
connection = MongoClient("mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test", 27017)

# Connect to the Database where the images will be stored.
database = connection['fashion_finder_db']

#Create an object of GridFs for the above database.
fs = gridfs.GridFS(database)

#define an image object with the location.
file = "unknown3.png"

#Open the image in read-only format.
with open(file, 'rb') as f:
    contents = f.read()


#Now store/put the image via GridFs object.
fs.put(contents, filename="file")
#store image in mongodb database
def store_image():
    with open(file, 'rb') as f:
        contents = f.read()
    fs.put(contents, filename="file")
    print(contents)


#fetch the image from the database.
image = fs.get_last_version("file")

#Write the image to a file.
with open("unkown.png", 'wb') as f:
    f.write(image.read())

# #get image from mongodb database
def get_image():
    image = fs.get_last_version("file")
    with open("thisissafwfromdbstill-4.png", 'wb') as f:
        f.write(image.read())
    return image

myclient = pymongo.MongoClient("mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test:27017")

print(myclient.list_database_names())
#store_image()
get_image()


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

# get_image()
