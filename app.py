from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Hello, Flask!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
