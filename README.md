# <center>WebScraper</center>
## Information
+ Web Scraper is a python script to read off articles published daily at [theverge.com](https://www.theverge.com/). <br/>
+ It extract about headline, get the link of the article, the author, and the date of each of the articles. <br/>
+ The data of each day, stored in a CSV file titled `ddmmyyy_verge.csv`, with the following header `id, URL, headline, author, date` and in a SQLite Database.<br/>
- - -
## Python Script and Assumptions
+ The Python scripts require following some modules to run. Below is code to install them
  ```pip install requests, bs4, pyodbc, csv```
