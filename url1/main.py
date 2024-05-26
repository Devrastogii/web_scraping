from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def index():
    mongo_uri = os.getenv('MONGO_URL')
    print(mongo_uri)
    try:
        client = MongoClient(mongo_uri)
        db = client['Internship-Task']
        collection = db["moviesUrl"]

        data = pd.read_csv('url1/films_data.csv')
        total_length = len(data['Title'])

        for i in range(total_length):           
            document = {
                "Title": data['Title'][i],
                "Nominations": int(data['Nominations'][i]),
                "Awards": int(data['Awards'][i]),
                "Year": str(data['Year'][i]),
                "Best Picture": data['Best Picture'][i]                
            }
            collection.insert_one(document)

        print("Connection Successful")
    except Exception as e:
        print(f"Connection failed: {e}")

index()