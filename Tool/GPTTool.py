import os
from Tool.BaseTool import BaseTool
import requests
import openai


class GPTTool(BaseTool):
    def __init__(self):
        super(GPTTool, self).__init__("chatbot")
        self.client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def reply(self, message):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
