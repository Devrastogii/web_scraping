import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.scrapethissite.com/pages/advanced/')

with open('url3/file.txt', 'w') as f:
    f.write(response.text)
    soup = BeautifulSoup(response.content, 'html.parser')
    ptags = soup.select('p')
    
    with open('url3/p.txt', 'w') as p:
        for i in ptags:
            p.writelines(i.get_text(strip=True))
    
    h3 = soup.select('h3')
    
    with open('url3/h3.txt', 'w') as h:
        for i in h3:
            h.writelines(i.get_text(strip=True))

    h4 = soup.select('h4')
    
    with open('url3/h4.txt', 'w') as hi:
        for i in h4:
            hi.writelines(i.get_text(strip=True))