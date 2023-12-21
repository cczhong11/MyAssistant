# def a base tool class with reply function


class BaseTool(object):
    def __init__(self, name):
        self.name = name

    def reply(self, message):
        raise NotImplementedError("This is a base tool class.")

    def get_name(self):
        return self.name

    def get_description(self):
        return "This is a base tool class."

    def get_usage(self):
        return "This is a base tool class."

    def get_help(self):
        return "This is a base tool class."
