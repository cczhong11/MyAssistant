from Tool.BaseTool import BaseTool
import requests
import feedparser


class MemoTool(BaseTool):
    def __init__(self, memo_url):
        super(MemoTool, self).__init__("memo")
        self.memo_url = memo_url

    def reply(self, message):
        import requests

        headers = {
            "Content-Type": "application/json",
        }
        data = {"content": message}
        if "#exp" not in message:
            message = message + " #exp"
        response = requests.post(self.memo_url, headers=headers, json=data)
        return "你的反思已经记录下来了"
