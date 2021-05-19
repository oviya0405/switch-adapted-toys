import os
from time import sleep

while True:
    os.system('sudo sh -c "echo 0 > /sys/class/leds/led1/brightness"')
    sleep(1)
    os.system('sudo sh -c "echo 1 > /sys/class/leds/led1/brightness"')
    sleep(1)

