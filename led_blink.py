import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# LED pin number
led = 21
GPIO.setup(led, GPIO.OUT)

# switch on
GPIO.output(led, 1)

# switch off
GPIO.output(led, 0)
