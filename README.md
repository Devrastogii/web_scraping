
# Web Scraping App

It has three urls - one containing movies, second containing hockey teams and third containing normal data. From the first two, I have scraped all the details of movies and teams and stored the data in Mongo Db Database.
## Tech Stack

Stack Used: Python and Mongo DB


## How To Run

- Clone this git repository
- Write below code in terminal

### For First URL
#### cd url1 -> python csvv.py 

- After that, a csv file is created in that directory

#### python main.py

- Now the database and collection will be created in the Mongo DB Project and data will be stored in the collection

### For Second URL
#### cd url2 -> python csvv.py 

- After that, data will be stored in the database

### For Third URL
#### cd url3 -> python main.py 

- Four different files will be created

For Database - Create a project on Mongo DB Atlas and save the username and password. Then connect using the connect string of your project. Replace the env URL with your connection string
## Author

- Dev Rastogi

