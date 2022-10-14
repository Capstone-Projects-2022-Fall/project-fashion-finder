import os
import base64
import pymongo

def checkImage(file_name):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        return True
    return False

def checkFile(file_name):
    if(os.path.exists(file_name)):
        return True
    return False

def convert64(file_name):
    image_file = open(file_name, "rb")
    bs64_str = base64.b64encode(image_file.read())
    return bs64_str

conn_str = "mongodb+srv://django_db_user:Ko4mNy6A5JEaST@cluster0.quth27s.mongodb.net/test"

connection = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = connection.test
file_meta = db.file_meta

def main():
    while(True):
        file_name = input("Enter the image name to upload: ")
        # check if the file exists or not in our folder
        if checkFile(file_name):
            # verify that the file is an image file
            if checkImage(file_name):
                # print(convert64(file_name))
                enc_file = convert64(file_name)
                coll = db.testcollection
                coll.insert_one({"filename": file_name, "file": enc_file, "description": "test"})
                break;
        else:
            print("Please enter a valid image file")

main()