from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/Request/<int:postID>')
def show_blog(postID):
   return 'Request Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
    app.run(debug=True)
