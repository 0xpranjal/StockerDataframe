from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="StockerDataframe", 
    version="1.2", 
    description="A unique tool for better analysis of Stock Market", license='GPL-3.0 License', 
    long_description=long_description, long_description_content_type='text/markdown', author="Pranjal", packages=['StockerDataframe'], url = 'https://github.com/Bhard27/StockerDataframe', author_email='pranjal27bhardwaj@gmail.com')