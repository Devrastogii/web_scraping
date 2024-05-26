import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

base_url = 'https://www.scrapethissite.com/pages/forms/'
mongo_uri = os.getenv('MONGO_URL')

try:
    client = MongoClient(mongo_uri)
    db = client['Internship-Task']
    collection = db["teamsUrl"]

    names, years, wins, losses, win_percentage, goals, against, plus, ot = [],[],[],[],[],[],[],[],[]
    soups = ["td.name", "td.year", "td.wins", "td.losses", "td.ot-losses", "td.pct", "td.gf", "td.ga", "td.diff"]
    columns = [names, years, wins, losses, ot, win_percentage, goals, against, plus]

    def scrape():
        for page_num in range(1, 100 + 1):
            page_url = f"{base_url}?page_num={page_num}"
            if not scrape_page(page_url): break    

    def scrape_page(page_url):
        response = requests.get(page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            if not soup.select('td.name'): return False
            k = 0

            for i in range(len(columns)):
                for soup_object in soup.select(f'{soups[i]}'):                
                    columns[k].append(soup_object.get_text(strip=True))
                k+=1

            return True
    
    scrape()

    for i in range(len(names)):
        doc = {
            "Name": names[i],
            "Year": years[i],
            "Wins": wins[i],
            "Losses": losses[i],
            "OT Losses": ot[i],
            "Win %": win_percentage[i],
            "Goals For": goals[i],
            "Goals Against": against[i],
            "+/-": plus[i]
        }

        collection.insert_one(doc)

except Exception as e:
    print(f"Connection failed: {e}")