from setuptools import setup, find_packages

setup(
    name="zns-discord-bot",
    version="1.0.9",
    description="A Discord bot library that integrates many functionalities for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Zennisch",
    author_email="zennisch@gmail.com",
    url="https://github.com/Zennisch/zns-discord-bot",
    packages=find_packages(),
    install_requires=[
        "discord.py",
        "zns-logging",
    ],
    python_requires=">=3.10",
)
