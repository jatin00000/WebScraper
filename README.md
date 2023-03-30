# <center>WebScraper</center>
## Information
+ Web Scraper is a python script to read off articles published daily at [theverge.com](https://www.theverge.com/). <br/>
+ It extract about headline, get the link of the article, the author, and the date of each of the articles. <br/>
+ The data of each day, stored in a CSV file titled `ddmmyyy_verge.csv`, with the following header `id, URL, headline, author, date` and in a SQLite Database.<br/>
- - -
## Python Script and Assumptions
+ The Python scripts require following some modules to run. Below is code to install them <br/>
```
pip install requests bs4 pyodbc csv
```
+ The Articles for each date are available separately on theverge.com. To get articles for any date, below is the URL format, just replace `{year}`, `{month}` and `{date}` in the url.
```
https://www.theverge.com/archives/{year}/{month}/{date}
https://www.theverge.com/archives/2023/3/30
```
+ For SQLite Database, i had used the [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database). So for running the script
+ - Sign up and create a [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database).
+ - Replace your <b>Server name, Database name, username and password </b> in class Webscraper _init_ in [main.py]()
