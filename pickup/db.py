from pymongo import MongoClient
import json


def load_mongo(db='Restaurant'):
    password = input('\nPassword: \n')
    client = MongoClient("mongodb+srv://aar0npham:<password>@macpickup-izclc.mongodb.net/test?retryWrites=true&w=majority".format(password))
    return client[db]


def write_db(col='Menu', file='pickup.json'):
    dump = load_mongo()
    cur = dump[col].find({})
    count = dump[col].count_document({})
    with open(file, 'w') as f:
        f.write('[')
        for i, doc in enumerate(cur, 1):
            f.write(json.dump(doc))
            if i != count:
                f.write(',')
        f.write(']')
    f.close()

def get_data(col, places, restaurant):
    pass
