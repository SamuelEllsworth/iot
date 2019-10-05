import network
import time
import urequests
import ujson
from machine import Pin

with open('config.py') as filepointer:
    secrets = ujson.loads(filepointer.read())

server_url = "http://" + secrets['server_address'] + ":8000"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['wifi_network'], secrets['wifi_password'])

p32 = Pin(32, Pin.IN)
p33 = Pin(33, Pin.OUT)
p33.value(1)

def wait_pin_change(pin):
    counter = 0
    while counter < 2:
        if pin.value() != 0:
            counter += 1
        else:
            counter = 0
        time.sleep(1)

while True:
    wait_pin_change(p32)
    print(p32.value())
    response = urequests.post(server_url, data = "button pressed")
    print(response.text)
