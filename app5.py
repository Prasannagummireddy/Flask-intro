from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app4.html', message="Enter your name below:")

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello, {name}!"

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('app5.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
