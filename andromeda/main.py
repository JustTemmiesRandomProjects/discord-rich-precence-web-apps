from pypresence import Presence
import time

client_id = '765222621779853312' #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 

x = 420

print(RPC.update(
    state=f"Watching over {x} users",
    details="An open source discord bot",
    large_image="pride_flag",
    #small_image="NAME OF SMALL IMAGE HERE",
    large_text="baver"
    ))  # Set the presence


while True: 
    time.sleep(15)