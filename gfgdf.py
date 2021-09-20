
import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BOARD)                     #Set GPIO pin numbering 
GPIO.setwarnings(False)
a=0
led = 32
GPIO.setup(led,GPIO.OUT)
p = GPIO.PWM(led,50)
p.start(0)
p.ChangeDutyCycle(a)
time.sleep(100)
