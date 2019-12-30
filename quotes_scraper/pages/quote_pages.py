from bs4 import BeautifulSoup

from locators.quote_page_locators import QuotesPageLocators
from parsers.quotes import Quote

class QuotePage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')
    
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [Quote(e) for e in quote_tags]