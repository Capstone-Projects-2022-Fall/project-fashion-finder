from pymongo import MongoClient


def get_db_default_handle():
    db_handle, client = get_db_handle(db_name='fashion_finder_db',
                                      host='mongodb+srv://cluster0.quth27s.mongodb.net/test',
                                      username='django_db_user',
                                      password='Ko4mNy6A5JEaST', # TODO: make secret
                                      port=27017)
    return db_handle, client


def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password)
    db_handle = client['db_name']
    return db_handle, client


if __name__ == '__main__':
    db_handle, client = get_db_default_handle()
    database_names = client.list_database_names()

    if ('fashion_finder_db' not in database_names):
        print("The Fashion Finder Database was no found ")
    else:
        print("Fashion Finder DB was found")
