from locators.quote_locators import *

class Quote:
    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content},by {self.author} tags = {self.tags} >' 

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [i.string for i in self.parent.select(locator)]
