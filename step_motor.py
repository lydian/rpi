# coding: utf-8
import RPi.GPIO as GPIO
    
    
def run(pins=[5, 6, 13, 19], wait_time):
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)
    seq = [
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 1, 0, 0], 
        [0, 1, 0, 0], 
        [0, 1, 1, 0], 
        [0, 0, 1, 0], 
        [0, 0, 1, 1], 
        [0, 0, 0, 1]
    ]

    step_counter = 0
    while True:
        print step_counter
        print seq[step_counter]
        for pin, output in zip(pins, seq[step_counter]):
            print pin, output,
            GPIO.output(pin, bool(output))
        print ' '
        step_counter = (step_counter + 1) % len(seq)
        time.sleep(wait_time)
        
    
