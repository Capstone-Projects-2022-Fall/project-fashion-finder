from pymongo import MongoClient
import pymongo
import pymongo as pm
import pywebio
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
from pywebio import start_server, output, config


def login():
  # credentials = input_group("Please Login", [
  #   input("Username", name="username"),
  #   input("Password",
  #         name="password",
  #         type=PASSWORD,
  #         placeholder="Enter your password",
  #         help_text="If you have issues",
  #         required=True),
  # ])

  # with put_loading(shape="border", color="dark"):

  #   username = credentials.get("username")
  #   password = credentials.get("password")
  client = pm.MongoClient(
      "mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test",
      27017)
  # db = client.imagebank
  # getin = db.votingperson
  # getin.insert_one({
  #     "voter_id": username,
  #     "pass": password,
  #   })

    # client = pm.MongoClient(
    #   "mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test",
    #   27017)
  db = client.imagebank
  posts = db.LabeledFashionPiece

  x = 2
  total = 15
  #print database data for image_id
  # print(posts.find_one({"image_id":x}))
  # #print only thr image_data
  while x <= total:
    client = pm.MongoClient(
      "mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test",
      27017)
    db = client.imagebank
    posts = db.LabeledFashionPiece
    put_image(posts.find_one({"image_id": x})["image_data"])
    picked = (posts.find_one({"image_id": x})["image_data"])

    put_markdown("# Vote now")
    voting = ["YES", "NO", "PASS"]
    lang = radio("Select your vote now", options=voting)
    put_text("You selected", lang)
    put_text("Thank you for voting!")
   # username = credentials.get("username")

    mydict = {picked: lang, "voter_id": "null"}

    myclient = pymongo.MongoClient(
      "mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.glnjpi9.mongodb.net/test"
    )
    mydb = myclient["fashion_finder_db"]
    mycol = mydb["votes"]
    y = mycol.insert_one(mydict)
    print(y.inserted_id)
    for y in mycol.find():
      print(y)
    pywebio.output.clear(scope=None)
    x = x + 1

  else:
    print("no more images")

start_server(login, port=8080, debug=True, cdn=False)