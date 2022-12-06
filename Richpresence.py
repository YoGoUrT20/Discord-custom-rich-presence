from pypresence import Presence 
import time

start = int(time.time())
client_id = "" #your application's client id
DSRPC = Presence(client_id)
DSRPC.connect()

while True: #infinite loop
    DSRPC.update(
        large_image = "", #link to image
#        small_image = "", 
#        large_text = "Dancin'",
#        small_text = "verified!",
        start = start,
        buttons = [{"label": "Me on YouTube", "url": "https://google.com"}, {"label": "Me on Discord!", "url": "https://google.com"}] #up to 2 buttons
    )
    time.sleep(60) #updating time 