from Tool.PlanTool import PlanTool


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
        return "我不能帮助你"
