import requests
import csv

csv_file = 'url1/films_data.csv'
url = 'https://www.scrapethissite.com/pages/ajax-javascript'

with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Nominations', 'Awards', 'Year', 'Best Picture'])

years = [2010,2011,2012,2013,2014,2015]

params = {
    'ajax': 'true',
    'year': 2015
}

def scrape():
    for i in years:
        params = {'ajax': 'true',
    'year': {i}}
        scrapePage(params, i)

def scrapePage(params, year):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        films = response.json()
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)   
        
            for film in films:
                title = film.get('title')
                nominations = film.get('nominations')
                awards = film.get('awards')
                best_picture = film.get('best_picture')
                writer.writerow([title, nominations, awards, year, best_picture])
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

scrape()