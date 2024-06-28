import os
from Tool.GPTTool import GPTTool
from Tool.MemoTool import MemoTool
from Tool.PlanTool import PlanTool
from Tool.NewsTool import NewsTool
from Tool.ReminderTool import ReminderTool
from Tool.Social import SocialTool


class Assistant:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        for config_key in ["server_url", "rss_url", "memo_url"]:
            if config_key not in config:
                raise ValueError(f"config key {config_key} not found")

    def reply(self, message):
        token = self.config.get("openai") or os.environ.get("OPENAI_API_KEY")
        if "计划" in message:
            if server_url := self.config.get("server_url"):
                return PlanTool(server_url).reply(message)
        if "新闻" in message:
            if rss_url := self.config.get("rss_url"):
                return NewsTool(rss_url).reply(message)
        if "反思" in message or "#exp" in message:
            if memo_url := self.config.get("memo_url"):
                return MemoTool(memo_url).reply_exp(message)
        if "读书心得" in message or "#book" in message:
            if memo_url := self.config.get("memo_url"):
                return MemoTool(memo_url).reply_book(message)
        if "memo:" in message:
            if memo_url := self.config.get("memo_url"):
                return MemoTool(memo_url).reply_memo(message)
        if "提醒" in message:
            if server_url := self.config.get("server_url"):
                return ReminderTool(token, server_url).reply(message)
        if "小红书" in message:
            if server_url := self.config.get("server_url"):
                return SocialTool(token, server_url).reply(message)
        keywords = self.config.get("keywords")
        for k, prompt in keywords.items():
            if k in message:
                return GPTTool(token).reply(prompt + ". context: " + message)
        return GPTTool(token).reply(message)
