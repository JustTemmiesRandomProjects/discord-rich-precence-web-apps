# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://top.gg/bot/765222621779853312'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

div = soup.find('p', {"class":"chakra-text css-o3nsz6"}) #Finds the div with class "_1lwNBHmCQJObvqs1fXKSYR"
text = div.text #Identifies text of the div tag
print(text)


#To download the whole data set, let's do a for loop through all a tags
# line_count = 1 #variable to track what line you are on
# for one_a_tag in soup.findAll('a'):  #'a' tags are for links
    # link = one_a_tag['53'] #get the link
    # print(link)
    # time.sleep(0.1) #pause the code for a sec