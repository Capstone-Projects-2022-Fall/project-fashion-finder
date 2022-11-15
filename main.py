##mongodb voting app with pywebio
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





myclient = pymongo.MongoClient("mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test:27017")
connection = MongoClient("mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test", 27017)

database = connection['fashion_finder_db']

file = "unkown.png"
fs = gridfs.GridFS(database)

def get_pic():
    image = fs.get_last_version("file")
    with open(file, 'wb') as f:
        f.write(image.read())
    return image


def vote():
    get_pic()
    img = open(file, 'rb').read()
    put_image(img, width='500px')
    put_markdown("# Vote now")
    voting = ["YES", "NO", "PASS"]
    lang = radio("Select your vote now", options=voting)
    put_text("You selected", lang)
    put_text("Thank you for voting!")

    #connect to mongodb
    myclient = pymongo.MongoClient("mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test")
    mydb = myclient["fashion_finder_db"]
    mycol = mydb["votes"]

    #insert vote into mongodb
    mydict = { "": lang }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    for x in mycol.find():
        print(x)

def save_pic():
    connection = MongoClient("mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test", 27017)
    database = connection['fashion_finder_db']
    #Create an object of GridFs for the above database.
    grid_fs = gridfs.GridFS(database)

    #Insert the image into GridFS
    with open(file, 'rb') as image:
        grid_fs.put(image.read(), filename=file)




    #Get the image from GridFS
    image = grid_fs.get_last_version(file)
    #Write the image to a file
    with open(file, 'wb') as image_write:
        image_write.write(image.read())

#get image from mongodb database
def get_image():
    grid_fs = gridfs.GridFS(database)
    image = grid_fs.get_last_version(file)
    with open(file, 'wb') as image_write:
        image_write.write(image.read())
    return image
start_server(vote, port=8080, debug=True)
#
# /save_pic()
# get_image()
# vote()






#Now store/put the image via GridFs object.




