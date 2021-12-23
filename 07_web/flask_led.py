import RPI.GPIO as GPIO

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask !!</p>
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
    '''

@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        return '''
            <p>LED ON</p>
            <a href="/">Go home</a>
        '''
    elif op == "off":
        return '''
            <p>LED OFF</p>
            <a href="/">Go home</a>
        '''


if __name__ == "__main__":
    app.run(host="0.0.0.0")