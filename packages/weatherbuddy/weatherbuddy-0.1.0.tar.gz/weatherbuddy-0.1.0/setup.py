from setuptools import setup, find_packages

setup(
    name="weatherbuddy",
    version="0.1.0",
    description="A simple Python package to fetch and process weather data from OpenWeatherMap API.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="AdrianaGRO",
    url="https://github.com/AdrianaGRO/intermediate-python-projects",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
