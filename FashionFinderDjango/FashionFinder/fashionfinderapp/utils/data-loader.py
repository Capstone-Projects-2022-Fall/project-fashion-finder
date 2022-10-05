import pymongo
import pandas as pd
from PIL import Image
import io
def get_db_handle(db_name, host, port, username, password):

    client = pymongo.MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password)
    db_handle = client['db_name']
    return db_handle, client


def get_db_default_handle():
    db_handle, client = get_db_handle(db_name='fashion_finder_db',
                                      host='mongodb+srv://cluster0.quth27s.mongodb.net/test',
                                      username='django_db_user',
                                      password='Ko4mNy6A5JEaST', # TODO: make secret
                                      port=27017)
    return db_handle, client

# db_handle, client = get_db_default_handle() 


data_abs_path = "/mnt/c/Users/mdc20/Downloads/"
lookup_path = data_abs_path + "input/"


val_attr_df: pd.DataFrame = pd.read_csv(lookup_path + "val_attr.txt", sep=' ', index_col=False)
val_img_path_df: pd.DataFrame = pd.read_csv(lookup_path + "val.txt") # Expect Series
val_cate_df: pd.DataFrame = pd.read_csv(lookup_path + "val_cate.txt") # Expect Series

lookup_cate_df: pd.DataFrame = pd.read_csv(lookup_path + 'lookup_cate.txt')
lookup_attr_df: pd.DataFrame = pd.read_csv(lookup_path + 'lookup_attr.txt')

print(len(val_attr_df))
print(val_attr_df.head())
print(val_img_path_df.head())
print(val_cate_df.head())
print(lookup_cate_df.head())
print(lookup_attr_df.head())


def create_mongo_document(client, row, collection):
    filepath = data_abs_path + row['filepath']
    im = Image.open(filepath)
    img_bytes = io.BytesIO()
    im.save(img_bytes, format='JPEG')

    fashion_piece_doc = {
        'data': img_bytes.getvalue(),
        'attrs': row['attrs']
    }

    image_id = collection.insert_one(fashion_piece_doc)
    if(image_id):
        return image_id
    else:
        return 'Failed to upload'

def label_attr(row):
    attrs = list()
    for key in row.keys():
        if(row[key] == 1):
            attrs.append(key)

    return attrs
print(val_attr_df)

val_attr_df = val_attr_df.reset_index()

print(val_attr_df)

val_attr_df['attrs'] = val_attr_df.apply(lambda row : label_attr(row), axis=1)

print(val_attr_df)

val_attr_df = pd.merge(left = val_attr_df, right = val_img_path_df, left_index = True, right_index = True)

print(val_attr_df)


db_handle, client = get_db_default_handle()

db = client.fashion_finder_db
fashion_piece_collection = db.FashionPiece





val_attr_df['MongoID'] = val_attr_df.apply(lambda row : create_mongo_document(client, row, fashion_piece_collection), axis=1)
client.close()
print(val_attr_df)
# for idx, row in val_attr_df.iterrows():
#     if (idx > MAX_ITERS):
#         break
#     attributes = list()

#     for elem_idx, elem in enumerate(row):
#         if elem == 1:
#             attr_name = lookup_attr_df[elem]
#     print(attributes)
#     print(val_img_path_df[idx])
