from Tool.BaseTool import BaseTool
import requests


class PlanTool(BaseTool):
    def __init__(self, server_url):
        super(PlanTool, self).__init__("plan")
        self.server_url = server_url

    def reply(self, message):
        if "周" in message:
            return self.get_week_plan()
        if "月" in message:
            return self.get_month_plan()
        if "年" in message:
            return self.get_year_plan()
        return "不知你要问什么计划"

    def get_week_plan(self):
        week_plan = self.get_json(self.get_url("weekly"))["data"][0]["data"]
        content = "这周生活计划" + week_plan["next_week_life_plan"]
        content += "\n工作计划" + week_plan["next_week_work_plan"]
        content += "\n学习计划" + week_plan["next_week_study_plan"]
        return content

    def get_month_plan(self):
        month_plan = self.get_json(self.get_url("monthly"))["data"][0]["data"]
        content = "月计划" + month_plan["nextweekaim"]

        return content

    def get_year_plan(self):
        year_plan = self.get_json(
            f"{self.server_url}/backend/file?name=2023%E5%B9%B4%E8%AE%A1%E5%88%92.md&list=must"
        )
        content = "年计划" + year_plan["data"][0]["content"]

        return content

    def get_url(self, list_type):
        return f"{self.server_url}/backend/json?date=latest&list={list_type}"

    def get_json(self, url):
        response = requests.get(url)
        return response.json()
