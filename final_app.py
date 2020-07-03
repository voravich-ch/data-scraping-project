import bs4
import requests
import pymongo
import os
import json
import datetime

def connect_to_database():
    # ใช้ os.environ แทน ไม่ควร hardcode อะไรที่เป็น credential
    # MONGODB_URI = os.environ['MONGODB_URI']
    MONGODB_URI = 'mongodb://heroku_0bjqvfwj:36ccu7pktksfa9i0efttheusuo@ds263707.mlab.com:63707/heroku_0bjqvfwj'
    client = pymongo.MongoClient(MONGODB_URI, retryWrites = False)
    db = client['heroku_0bjqvfwj']
    collection_name = 'news_data'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    collection = db[collection_name]
    return collection


def scrape_and_insert_data(collection):
    response = requests.get('https://www.thairath.co.th/news/royal')
    html_page = bs4.BeautifulSoup(response.content, 'html.parser')
    data = html_page.find(id = '__NEXT_DATA__')
    json_file = json.loads(str(data)[51:-9])
    target_news = json_file['props']['initialState']['common']['data']['items']['lastestNews']

    for news in target_news:
        content = bs4.BeautifulSoup(requests.get(news['canonical']).content, 'html.parser').select('div.css-n5piny.evs3ejl1 p')
        desc = ''
        for p in content:
            desc = desc + p.text + '\n'
        document = {
        'title': news['title'],
        'publish_date': datetime.datetime.strptime(news['publishTime'][0:10] + ' ' + news['publishTime'][11:19], '%Y-%m-%d %H:%M:%S'),
        'desc': desc,
        'tags': news['tags'],
        'cover_img': news['image'],
        'news_url': news['canonical'],
        'category': news['topic'],
                }
        collection.insert_one(document)
        print(document)
        print('Document inserted!')
        print(document['title'])
    return document

def main():
    collection = connect_to_database()
    scrape_and_insert_data(collection)


if __name__ == "__main__":
    main()
