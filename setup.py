from setuptools import setup, find_packages

setup(
    name="MyAssistant",
    version="0.2",
    packages=find_packages(),
    description="helper for your life",
    author="TC",
    author_email="me@tczhong.com",
    url="http://github.com/cczhong11/MyAssistant",
    install_requires=["openai", "requests", "feedparser"],
)
