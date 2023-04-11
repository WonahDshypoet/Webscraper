#Webscraper to get my image from my personal website(All these are just local for now) Using BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re

html = urlopen("file:///C:/Users/hp/Documents/Sound%20recordings/wonah/index.html")
my_url = (html.read())
print(my_url)

bs = soup(my_url, 'html.parser')

image = bs.find('img', {"id":"image"})

#Accessing Attributes of the image tag in my website

print(image.attrs['src'])
print(image.attrs['height'])
print(image.attrs['width'])

#Using Lambda functions in webscraping

only2 = bs.find_all(lambda  tag: len(tag.attrs) == 5)

print(only2)