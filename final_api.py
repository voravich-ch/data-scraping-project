from flask import Flask, jsonify, request
import json
import datetime
import pymongo
import pandas as pd

def connect_to_database():
    # ใช้ os.environ แทน ไม่ควร hardcode อะไรที่เป็น credential
    # MONGODB_URI = os.environ['MONGODB_URI']
    MONGODB_URI = 'mongodb://heroku_0bjqvfwj:36ccu7pktksfa9i0efttheusuo@ds263707.mlab.com:63707/heroku_0bjqvfwj'
    client = pymongo.MongoClient(MONGODB_URI, retryWrites = False)
    db = client['heroku_0bjqvfwj']
    collection_name = 'news_data'
    collection = db[collection_name]
    return collection

api = Flask(__name__)
collection = connect_to_database()
cursor = collection.find({}, projection = {"_id": 0})
documents = [document for document in cursor]
df = pd.DataFrame(documents)

@api.route('/news')
def serve_data():
    date = request.args.get('date', type = str) #Format = 'YYYY:MM:DD'
    tag = request.args.get('tag', type = str)
    limit = request.args.get('limit', type = int)

    if date is not None:
        datetime_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        DF1 = df[df['publish_date'] == datetime_obj]
    if tag is not None:
        index = []
        for row in df['tags']:
            if any(tag in a for a in row):
                index.append(True)
            else:
                index.append(False)
        tagged_rows = df[index]
        DF2 = tagged_rows

    if date is None and tag is not None:
        query = DF2
    if date is not None and tag is None:
        query = DF1
    if date is not None and tag is not None:
        query = pd.merge(DF1, DF2, on = ['title', 'publish_date', 'desc', 'cover_img', 'news_url', 'category'], how = 'inner')
        query.drop(columns = 'tags_y', inplace =True)
        query.rename(columns = {'tags_x': 'tags'}, inplace = True)
    if date is None and tag is None:
        query = df
    
    if limit is None or limit >= 20:
        query = query[:20]
    else:
        query = query[:limit]

    result_json = json.loads(query.to_json(date_format='iso', orient='records'))
    return jsonify(result_json)


if __name__ == "__main__":
    api.run()