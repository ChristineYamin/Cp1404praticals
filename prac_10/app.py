from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    #return 'Hello World!'
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name="Yamin"):
    return f"Hello {name}"

@app.route('/100.2')
def convert_fahrenheit(celsius=22):
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"Result: {fahrenheit:.2f} F"



if __name__ == '__main__':
    app.run()

