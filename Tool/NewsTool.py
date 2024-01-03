from Tool.BaseTool import BaseTool
import requests
import feedparser


class NewsTool(BaseTool):
    def __init__(self, rss_url):
        super(NewsTool, self).__init__("news")
        self.rss_url = rss_url

    def reply(self, message):
        return self.get_news(message)

    def get_news(self, message):
        news = self.get_feed()
        if "text" in message or "内容" in message:
            return news["description"]
        return news["id"]

    def get_feed(self):
        feed = feedparser.parse(self.rss_url)
        for item in feed.entries:
            return item
