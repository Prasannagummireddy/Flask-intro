from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app4.html', message="Enter your name below:")

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello, {name}!"


if __name__ == '__main__':
    app.run(debug=True)
