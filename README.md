# Botnoi Consulting Course: Data scraping project

## **Overview**
The main objective of this project is to deploy a web API to serve news data with filtering parameters date, tags, and limit. Firstly, I developed code to scrape data from a news website and store them as dictionaries in the MongoDB database. Subsequently, I deployed my code to Heroku and set a scheduler to run the scraping hourly. Finally, I developed and deployed a flask API to Heroku, which allows people to access the web application and request news data from the database.

## **Directory Structure**

```
        data_scraping_project
        ├── README.md
        ├── news_scraping
        │   ├── app.py
        │   └── requirements.txt
        └── api_data_request
           ├── api.py
           ├── Procfile
           └── requirements.txt

```

## File Description
-   `app.py` -> Python script for data scraping. It scrapes data from a [news website](https://www.thairath.co.th/news/royal) and stores parameters including: \
  - title, public_date, 
-   `api.py` -> Table containing random sample for testing (Not used: data cleaning is needed)
