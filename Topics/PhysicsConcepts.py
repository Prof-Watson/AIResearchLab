import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
session = HTMLSession()
TopicsWiki = "https://en.wikipedia.org/wiki/Glossary_of_physics"
import pandas as pd

"""

This code is pulling out multiple physics concepts from Wikipedia

"""

response = session.get(TopicsWiki)
response.html.render()
page = response.html
j = 0
topics = list()
for i in page.find('a'):
    try:
        if i.attrs['title'] and len(i.text) > 1:
            j = j + 1
            print(i.text)
            topics.append(i.text)
    except:
        continue
df = pd.DataFrame({'Topics': topics})
df.to_csv('PhysicsTopics.csv',index=False)
