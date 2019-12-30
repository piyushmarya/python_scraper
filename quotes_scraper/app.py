import requests

from pages.quote_pages import *

page_content = requests.get('https://spidyquotes.herokuapp.com/').content

page = QuotePage(page_content)
for x in page.quotes():
    print(x)



