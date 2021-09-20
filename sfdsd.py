
import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BOARD)                     #Set GPIO pin numbering 
GPIO.setwarnings(False)
red =11
blue=15
green =13
def fun():
        r=100
        b=50
        g=100

        print("clicked")
        GPIO.setup(red,GPIO.OUT)                  #Set pin as GPIO out
        GPIO.setup(green,GPIO.OUT)                   #Set pin as GPIO in
        GPIO.setup(blue,GPIO.OUT)
        p1 = GPIO.PWM(red,50)
        p1.start(0)
        p1.ChangeDutyCycle(r)
        time.sleep(100)
        p12 = GPIO.PWM(green,50)
        p12.start(0)
        p12.ChangeDutyCycle(g)
        time.sleep(100)
        p13 = GPIO.PWM(blue,50)
        p13.start(0)
        p13.ChangeDutyCycle(b)
        time.sleep(100)


while True:
    fun()
    time.sleep(100)
        