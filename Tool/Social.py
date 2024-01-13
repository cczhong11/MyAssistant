import os
import random
from Tool.BaseTool import BaseTool
import requests
import openai
import json
import re


class SocialTool(BaseTool):
    def __init__(self, token, server_url):
        super(SocialTool, self).__init__("chatbot")
        self.client = openai.OpenAI(api_key=token)
        self.server_url = server_url

    def openai_result(self, message, max_tokens=30):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    def reply(self, message):
        if "小红书" not in message:
            return "只支持小红书搜索"
        day = 1
        if "一周" in message:
            day = 7
        # find tag in message
        tags = re.findall(r"#([\w\d]+)", message)
        if len(tags) == 0:
            return "请输入tag"

        return self.get_social("xiaohongshu", ",".join(tags), day, message)

    def get_social(self, app, keyword, recent_days, message):
        print(
            f"{self.server_url}/backend/social_media?name={app}&keyword={keyword}&day={recent_days}"
        )
        response = requests.get(
            f"{self.server_url}/backend/social_media?name={app}&keyword={keyword}&day={recent_days}"
        )
        result = response.json()["data"]
        titles = {i: result[i]["title"] for i in range(len(result))}
        contents = {i: result[i]["content"] for i in range(len(result))}
        idx_results = []
        if len(contents.keys()) > 8:
            idx_results = random.sample(contents.keys(), 8)
        else:
            idx_results = contents.keys()
        final_prompt = "下面是我找到的内容：\n"
        reply_content = ""
        for idx in idx_results:
            if idx in titles:
                final_prompt += titles[idx] + "\n"
                final_prompt += contents[idx] + "\n"
                reply_content += titles[idx] + "\n" + contents[idx] + "\n"
        final_prompt += "总结回答：\n" + message

        return (
            self.openai_result(final_prompt, 1000)
            + "\n"
            + "-" * 20
            + "\n"
            + reply_content
        )
