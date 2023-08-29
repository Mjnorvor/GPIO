from gpiozero import LED, Button
from signal import pause
import requests

led = LED(17)
button = Button(2)
url = "https://maker.ifttt.com/trigger/{button.when_pressed}/json/with/key/dLQ7tvFeMcZXdfrUwoRfgS"

# button.when_pressed = led.on
# button.when_released = led.off

from subprocess import call
def print_thing():
    print ("button pressed")

def send_requests(url):
    print("Hello")
    r = requests.get(url)
    if r.status_code == "200":
        return 
    
    

button.when_pressed = print_thing

pause()
