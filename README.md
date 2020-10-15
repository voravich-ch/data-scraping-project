# Botnoi Consulting Training: Data scraping project

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
- `app.py` -> Python script for data scraping. It scrapes data from a [news website](https://www.thairath.co.th/news/royal) and stores parameters as a dictionary in MongoDB database which includes: 
  - **title**: title
  - **public_date**: date of publication
  - **desc**: content
  - **tags**: tags
  - **cover_img**:  cover image
  - **news_url**: URL
  - **category**:  category
  
- `api.py` -> Python script to create an api to request news data from the database to display on the server. There are three arguments used for filtering including: 
  - **date**: date parameter accepts string format `YYYY:MM:DD`
  - **tag**: tag parameter accepts string format
  - **limit**: limit parameter accepts integer less than 20. The default will show 20 results when the parameter is not determined
