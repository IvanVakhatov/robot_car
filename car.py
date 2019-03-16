import RPi.GPIO as gpio
from flask import Flask, render_template, request
import time
from gpiozero import LED, PWMOutputDevice

app = Flask(__name__)

FORWARD_RIGHT_PWM = 10
FORWARD_LEFT_PWM = 4
fwd_left = 17
backwd_left = 27
fwd_right = 22
backwd_right = 9
l_leds = 5
r_leds = 6

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(fwd_left, gpio.OUT)
gpio.setup(backwd_left, gpio.OUT)
gpio.setup(fwd_right, gpio.OUT)
gpio.setup(backwd_right, gpio.OUT)

forwardRight = PWMOutputDevice(FORWARD_RIGHT_PWM, True, 0, 1000)
forwardLeft = PWMOutputDevice(FORWARD_LEFT_PWM, True, 0, 1000)
left_leds = LED(l_leds)
right_leds = LED(r_leds)

left_leds.on()
right_leds.on()

@app.route("/")
def index():
    return render_template('car.html')

@app.route('/forward')
def forward():
    data1="FORWARD"
    gpio.output(fwd_left, True)
    gpio.output(backwd_left, False)
    gpio.output(fwd_right, True)
    gpio.output(backwd_right, False)
    forwardRight.value = 1.0
    forwardLeft.value = 1.0
    left_leds.off()
    right_leds.off()
    return "True"

@app.route('/backward')
def backward():
    data1="BACK"
    gpio.output(fwd_left, False)
    gpio.output(backwd_left, True)
    gpio.output(fwd_right, False)
    gpio.output(backwd_right, True)
    forwardRight.value = 1.0
    forwardLeft.value = 1.0
    left_leds.off()
    right_leds.off()
    return "True"

@app.route('/left')
def left():
    data1="LEFT"
    gpio.output(fwd_left, True)
    gpio.output(backwd_left, False)
    gpio.output(fwd_right, False)
    gpio.output(backwd_right, False)
    forwardLeft.value = 0.75
    forwardRight.value = 0
    left_leds.off()
    right_leds.on()
    return "True"

@app.route('/right')
def right():
    data1="RIGHT"
    gpio.output(fwd_left, False)
    gpio.output(backwd_left, False)
    gpio.output(fwd_right, True)
    gpio.output(backwd_right, False)
    forwardRight.value = 0.65
    forwardLeft.value = 0    
    left_leds.on()
    right_leds.off()
    return "True"

@app.route('/stop')
def stop():
    data1="STOP"
    gpio.output(fwd_left, False)
    gpio.output(backwd_left, False)
    gpio.output(fwd_right, False)
    gpio.output(backwd_right, False)
    forwardRight.value = 0
    forwardLeft.value = 0
    left_leds.on()
    right_leds.on()
    return "True"

@app.route('/led_on')
def led_on():
    data1="LED_ON"
    left_leds.off()
    right_leds.off()
    return "True"

@app.route('/led_off')
def led_off():
    data1="LED_OFF"
    left_leds.on()
    right_leds.on()
    return "True"

if __name__ == "__main__":
    print("Start")
    app.run(host='192.168.0.59', port=5010)
