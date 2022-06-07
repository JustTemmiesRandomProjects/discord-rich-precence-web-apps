from pypresence import Presence
import time
import requests
from bs4 import BeautifulSoup

client_id = '765222621779853312' #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 

url = 'http://top.gg/bot/765222621779853312'

def update_presence():
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.find_all("p", class_="chakra-text css-mewo4z")#Finds the div with class "_1lwNBHmCQJObvqs1fXKSYR"
    x = div[2].text

    RPC.update(
        state=f"Watching over {x} servers",
        details="An open source discord bot",
        large_image="andro",
        #small_image="NAME OF SMALL IMAGE HERE",
        large_text="baver",
        buttons = [
            {"label": "GitHub", "url": "https://github.com/JustTemmie/space-bot"},
            {"label": "Top.gg", "url": "https://top.gg/bot/765222621779853312"}
        ]
        )  # Set the presence


while True:
    update_presence()
    time.sleep(60)