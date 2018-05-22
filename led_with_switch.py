import RPi.GPIO as GPIO
import time

# refer to pins by the Broadcom SOC channel
GPIO.setmode(GPIO.BCM)

# Pin 19 will sense for button pushing
button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# The LED
led = 21
GPIO.setup(led, GPIO.OUT)

while True:
    input_state = GPIO.input(button) # sense the button
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
        # switch on LED
        GPIO.output(led, 1)
    else:
        # switch off LED
        GPIO.output(led, 0)

GPIO.cleanup()

