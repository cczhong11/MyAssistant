from Tool.GPTTool import GPTTool
from Tool.PlanTool import PlanTool
from Tool.NewsTool import NewsTool


class Assistant:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        for config_key in ["server_url"]:
            if config_key not in config:
                raise ValueError(f"config key {config_key} not found")

    def reply(self, message):
        if "计划" in message:
            if server_url := self.config.get("server_url"):
                return PlanTool(server_url).reply(message)
        if "新闻" in message:
            if rss_url := self.config.get("rss_url"):
                return NewsTool(rss_url).reply(message)
        return GPTTool().reply(message)
