# Web scraping demo project (quotes)

Hi! I'm **Mahmoud Moussa** and I have created this project to demonstrate the usage of **scrapy**  and **playwright** frameworks to render and scrape **JavaScript dynamic websites** and handling websites that require logging in to view content.

# Requirements

 1. First you need python to be installed on your system. you can download it from the official website **"https://www.python.org/downloads/"**.
 2. Next you need to install **scrapy** and **playwright** using **pip** by entering the following commands in a terminal.
 
    >pip install scrapy
    >pip install scrapy_playwright
    >playwright install

# Usage

> You need to be **inside the project folder** to run a spider.
1. The **first** spider is gonna scrape a website that uses javaScript to render dynamic content that is not visible if we disabled javaScript. 
- We are gonna scrape this site "http://quotes.toscrape.com/js/" for quotes text, author and tags.
 
 - Now all you need to do to run the spider is typing the following command in the terminal from **inside the project folder**.
`scrapy crawl quotes_js -o quotes-js.csv`
 after the spider finishes crawling the site you will find a file has been created in the project folder called **"quotes-js.csv"**

2. The second spider is gonna scrape a website that uses javaScript to render dynamic content that is not visible if we disabled javaScript but there is a second obstacle we will be facing. We have to wait 10 seconds for the dynamic content to be rendered. 
- The website link is: "http://quotes.toscrape.com/delayed/".
 - To run the spider type the following command in the terminal from **inside the project folder**.
`scrapy crawl quotes_delayed -o quotes-delayed.csv`
 after the spider finishes crawling the site you will find a file has been created in the project folder called **"quotes-delayed.csv"**
3. The third website is not using javaScript to render the content **(good news)** but we have to login using post request to view the website content.
- The website link is: "http://quotes.toscrape.com/login/".
 - To run the spider type the following command in the terminal from **inside the project folder**.
`scrapy crawl quotes_login -o quotes-login.csv`
 after the spider finishes crawling the site you will find a file has been created in the project folder called **"quotes-login.csv"**
4. The final variation of this website is the content we want to scrape is formatted in a table and all we want to do is scraping this table for data.
- The website link is: "http://quotes.toscrape.com/tableful/".
 - To run the spider type the following command in the terminal from **inside the project folder**.
`scrapy crawl quotes_table -o quotes-table.csv`
 after the spider finishes crawling the site you will find a file has been created in the project folder called **"quotes-table.csv"**