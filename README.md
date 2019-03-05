# web-scrapping-by-python
**Required libraries:**

1.Requests
> import requests

2.BeautifulSoup
> from bs4 import BeautifulSoup

3.Time
> import time

4.Multiprocessing
> import multiprocessing


Here the task is to get the data of top 1000  software developer jobs in Bangalore, Karnataka location from 
[indeed](https://www.indeed.co.in/) website.

Based on the requirements,i set the url like(https://www.indeed.co.in/jobs?q=software+developer&l=Bengaluru%2C+Karnataka&start=).

Access the each page url by using **request** library.

**Beautiful Soup** is a Python library for pulling data out of HTML.

Getting the data from HTML text by using the *div* and *class* .

After that, basic text processing for the retrieved data and store the data in dictionary.

Sort the dictionary data

Finally write this dictionary data to a JSON file.
