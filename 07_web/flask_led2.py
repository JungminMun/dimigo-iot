from flask import Flask
from flask.templating import render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

LED_PIN1 = 4
LED_PIN2 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def main():
    return render_template("led.html")

@app.route("/led/<color>/<op>")
def led(color, op):
    if color == "green" and op == "on":
        GPIO.output(LED_PIN1, GPIO.HIGH)
        return '''
            <p>green LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif color == "green" and op == "off":
        GPIO.output(LED_PIN1, GPIO.LOW)
        return '''
            <p>green LED OFF</p>
            <a href="/">Go Home</a>
        '''

    elif color == "blue" and op == "on":
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return '''
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
        '''

    elif color == "blue" and op == "off":
        GPIO.output(LED_PIN2, GPIO.LOW)
        return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
        '''

if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0")
    finally:
        GPIO.cleanup()