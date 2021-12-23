from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask !!</p>
        <a href="/first">Go First</a>
        <a href="/second">Go Second</a>

    '''

@app.route("/first")
def firstPage():
    return '''
        <p>First Page</p>
        <a href="../">Go home</a>
    '''

@app.route("/second")
def secondPage():
    return '''
        <p>Second Page</p>
        <a href="../">Go home</a>
    '''


if __name__ == "__main__":
    app.run(host="0.0.0.0")