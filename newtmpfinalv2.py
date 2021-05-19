xfrom sys import stderr,exit
from time import sleep

def toggle(hled,value,seconds):
    hled.write(value)
    hled.flush()
    hled.seek(0,0)
    sleep(seconds)

def playseq(led, times, secon, secoff):
    hled = open(LED[led],'w')
    while (times > 0):
        toggle(hled, '1', secon)
        toggle(hled,'0',secoff)
        times -= 1
    hled.close()

GREEN = 0
RED = 1
LED = {0: 'sys/class/leds/led0/brightness', 1: '/sys/class/leds/led1/brightness'}
playseq(GREEN, 5, 0.1, 0.2)
sleep(1)
