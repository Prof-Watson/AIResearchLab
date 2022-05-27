import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
session = HTMLSession()
amazon = "https://www.amazon.com/s?k=airpods&crid=2V4D4PKT80CH1&qid=1653430707&sprefix=airpor%2Caps%2C353&ref=sr_pg_1"
while amazon:
    response = session.get(amazon)
    response.html.render()
    page = response.html
    next_page = page.find('a', containing='next')[0]
    amazon = "https://www.amazon.com"+list(next_page.links)[0]
    print(amazon)