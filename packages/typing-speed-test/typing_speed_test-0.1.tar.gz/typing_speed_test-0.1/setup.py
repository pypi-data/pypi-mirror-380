from setuptools import setup, find_packages

setup(
    name="typing_speed_test",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "typing-speed-test = typing_speed_test.main:typing_speed_test"
        ]
    },
    author="Doaa",
    description="A simple typing speed test game.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
)

