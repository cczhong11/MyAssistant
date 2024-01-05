from Tool.BaseTool import BaseTool
import requests
import feedparser


class MemoTool(BaseTool):
    def __init__(self, memo_url):
        super(MemoTool, self).__init__("memo")
        self.memo_url = memo_url

    def reply_exp(self, message):
        if "#exp" not in message:
            message = message + " #exp"
        return self.reply_inner(message)

    def reply_book(self, message):
        if "#book" not in message:
            message = message + " #book"
        return self.reply_inner(message)

    def reply_inner(self, message):
        headers = {
            "Content-Type": "application/json",
        }
        data = {"content": message}
        response = requests.post(self.memo_url, headers=headers, json=data)
        return "你的反思已经记录下来了"
