import time
from machine import Pin

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

# response = urequests.post("http://000.000.000.000/iot", data = "test mesage")
   # print(response.json())
