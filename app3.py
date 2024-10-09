from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app3.html', message="Welcome to the Flask App!")

if __name__ == '__main__':
    app.run(debug=True)
