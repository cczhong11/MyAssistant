import os
from Tool.BaseTool import BaseTool
import requests
import openai


class ReminderTool(BaseTool):
    def __init__(self, token, server_url):
        super(ReminderTool, self).__init__("chatbot")
        self.client = openai.OpenAI(api_key=token)
        self.server_url = server_url

    def choose_list(self, message):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": message}],
            max_tokens=30,
        )
        return response.choices[0].message.content

    def get_reminder_list(self):
        response = requests.get(f"{self.server_url}/backend/file?list=reminder_list")
        return [data["name"].replace(".json", "") for data in response.json()["data"]]

    def reply(self, message):
        reminder_list = self.get_reminder_list()
        prompt = (
            "我有以下提醒事项清单：\n"
            + ",".join(reminder_list)
            + "\n 根据我的日程，请从中选择一个提醒事项， 只输出提醒列表名字。"
            + "\n 我的问题："
            + message
        )
        result = self.choose_list(message)
        for reminder in reminder_list:
            if reminder in result:
                return self.get_reminder(reminder)
        return result

    def get_reminder(self, reminder):
        response = requests.get(
            f"{self.server_url}/backend/json?name={reminder}.json&list=reminder_list"
        )

        return (
            response.json()["data"][0]["data"].get("reminder_content") or "无提醒事项"
        )
