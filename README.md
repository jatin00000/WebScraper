# <center>WebScraper</center>
## Information
+ Web Scraper is a python script to read off articles published daily at [theverge.com](https://www.theverge.com/). <br/>
+ It extract about headline, get the link of the article, the author, and the date of each of the articles. <br/>
+ The data of each day, stored in a CSV file titled `ddmmyyy_verge.csv`, with the following header `id, URL, headline, author, date` and in a SQL Database.<br/>
- - -
&nbsp;

## Python Script and Assumptions
+ The Python scripts require following some modules to run. Below is code to install them <br/>
```
pip install requests bs4 pyodbc csv
```
&nbsp;
+ The Articles for each date are available separately on theverge.com. To get articles for any date, below is the URL format, just replace `{year}`, `{month}` and `{date}` in the url.
```
https://www.theverge.com/archives/{year}/{month}/{date}
https://www.theverge.com/archives/2023/3/30
```
&nbsp;
+ For SQL Database, i had used the [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database). So for running the script
  - Sign up and create a [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database).
  - Replace your <b>Server name, Database name, username and password </b> in class Webscraper _init_ in [main.py](https://github.com/jatin00000/WebScraper/blob/main/main.py).
  - ![image](https://user-images.githubusercontent.com/94428262/228786859-608b5d4d-1f8e-4ba8-929b-ec86f2eddc6f.png)
- - -
&nbsp;

## My Working
- I am using a VM with Linux to run this script.
&nbsp;
- The Day, I am writing this Readme file, the script has already ran for 3 days 27th, 28th and 29th March 2023.
&nbsp;
- Using a [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database) for database storing.
&nbsp;
- Database Photo as a proof for that: 
![image](https://user-images.githubusercontent.com/94428262/228813912-95c741d6-9373-4052-a5a4-ac399e50d6d8.png)
&nbsp;
- For automatically running the script every day, I used [`cron`](https://en.wikipedia.org/wiki/Cron) command of Linux, &nbsp;
  It runs the script everyday at 07:05 PM at UTC. &nbsp;
  ```
  crontab -e
  ```
  ![image](https://user-images.githubusercontent.com/94428262/228818363-34d4a3e9-2376-41e4-9104-ffecb5c95017.png) &nbsp;
 &nbsp;
- Now, Showing proof of the three csv files of 27, 28, 29 March 2023 &nbsp;
  ![image](https://user-images.githubusercontent.com/94428262/228816615-60604761-92c3-4940-a935-24f5ccb1a7aa.png) &nbsp;
  _Name is hidden due to privacy issue._ &nbsp;
 &nbsp;
- This is csv file of 27th March, 2023.
  ![image](https://user-images.githubusercontent.com/94428262/228817422-ad34ac07-72a0-40f7-ba78-7eaa4bf74bbd.png)





