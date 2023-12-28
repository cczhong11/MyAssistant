from Tool.BaseTool import BaseTool
import requests
import feedparser


class NewsTool(BaseTool):
    def __init__(self, rss_url):
        super(NewsTool, self).__init__("news")
        self.rss_url = rss_url

    def reply(self, message):
        return self.get_news()

    def get_news(self):
        news = self.get_feed()
        return news["id"]

    def get_feed(self):
        feed = feedparser.parse(self.rss_url)
        for item in feed.entries:
            return item
