import datetime
import requests
from bs4 import BeautifulSoup
import pyodbc
import csv

class CurrentDate:
    def __init__(self):
        self.today = datetime.datetime.now()

    def get_date(self):
        return self.today.day

    def get_month(self):
        return self.today.month

    def get_year(self):
        return self.today.year


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.article_data = []
        self.server = '<server>.database.windows.net'
        self.database = '<database>'
        self.username = '<username>'
        self.password = '<password>'
        self.driver = '{ODBC Driver 17 for SQL Server}'

    def get_page_content(self):
        response = requests.get(self.url)
        return response.content

    def scrape_data(self):
        soup = BeautifulSoup(self.get_page_content(), 'html.parser')
        articles = soup.find_all('div', class_='c-entry-box--compact__body')

        for article in articles:
            headline = article.h2.a.text
            link = article.h2.a['href']
            authors = article.find_all('span', class_='c-byline__author-name')
            author_list = []
            for author in authors:
                author_list.append(author.text.strip())
            date = datetime.date.today()
            self.article_data.append({'headline': headline, 'link': link, 'author': ','.join(author_list), 'date': date})

    def save_csv(self):
        filename = datetime.datetime.today().strftime('%d%m%Y') + '_verge.csv'
        with open(filename, mode='w',newline='') as csv_file:
            fieldnames = ['id', 'URL', 'headline', 'author', 'date']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for i, article in enumerate(self.article_data):
                writer.writerow({'id': i, 'URL': article['link'], 'headline': article['headline'],
                                 'author': article['author'], 'date': article['date']})

    def create_db(self):
        conn = pyodbc.connect('DRIVER='+self.driver+';SERVER=tcp:'+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'articles'")
        if not cursor.fetchone():
             cursor.execute('''CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, url TEXT, headline TEXT, author TEXT, date DATE)''')

        for i, article in enumerate(self.article_data):
            cursor.execute(
                           "MERGE INTO articles AS target "
                          "USING (SELECT ?, ?, ?, ?, ?) AS source (id, url, headline, author, date) "
                          "ON (target.id = source.id) "
                          "WHEN NOT MATCHED THEN "
                           "INSERT (id, url, headline, author, date) "
                           "VALUES (source.id, source.url, source.headline, source.author, source.date);",(i, article['link'], article['headline'], article['author'], article['date']))

        cursor.commit()
        cursor.close()




if __name__ == '__main__':
    current_date = CurrentDate()
    day = current_date.get_date()
    month = current_date.get_month()
    year = current_date.get_year()
    today = str(datetime.date.today())
    scraper = WebScraper(f'https://www.theverge.com/archives/{year}/{month}/{day}')
    scraper.scrape_data()
    scraper.save_csv()
    scraper.create_db()