
# Flask Framework Introduction

## 1. What is Flask?

Flask is a lightweight and easy-to-use web framework for Python that allows developers to build web applications quickly and with minimal code. It is often referred to as a "micro-framework" because it doesn't include many built-in features that more extensive frameworks, like Django, offer. Instead, Flask provides the essentials, allowing developers to add the features they need via extensions.

- Flask is highly flexible, which makes it a great choice for smaller projects or APIs.
- It follows the WSGI (Web Server Gateway Interface) and Jinja2 template engine for rendering HTML.

## 2. Pros and Cons Compared to Django

| **Flask**                             | **Django**                           |
|---------------------------------------|--------------------------------------|
| **Pros**                              |                                      |
| - Lightweight, minimalistic, and flexible | - Full-featured framework with built-in components (e.g., ORM, authentication, admin) |
| - Easy to learn for beginners         | - Provides a lot of built-in functionality that accelerates development |
| - Great for small to medium-sized apps | - Suitable for large, complex applications |
| - High control over architecture and features | - Comes with an admin interface for managing content |
| **Cons**                              |                                      |
| - Lacks built-in features (you need to add extensions) | - More complex, steep learning curve due to its size |
| - May require more manual work for things like authentication, database integration | - Less flexibility when you want to deviate from Django's structure |

## 3. Use-Cases for Django and Flask

- **Flask**: Ideal for building small to medium-sized applications, microservices, and REST APIs. It's suitable for projects where simplicity, flexibility, and control are essential.
- **Django**: Better suited for large-scale, complex applications that require many built-in features like user authentication, admin interfaces, and a tightly integrated ORM.

**Examples:**
- **Flask**: Single-page applications, small web APIs, lightweight prototypes.
- **Django**: Full-fledged web applications with authentication, content management systems (CMS), e-commerce platforms.

## 4. Features of Flask

- **Minimalism**: Provides basic routing and view rendering out of the box but allows flexibility in adding components as needed.
- **Built-in development server**: For local testing and debugging.
- **WSGI compliant**: Works with most web servers.
- **Jinja2 templating**: Allows for dynamic HTML rendering.
- **URL routing**: Maps URLs to Python functions.
- **Extension support**: Allows you to add functionality like database access, authentication, and more.

---

# Step-by-Step Procedure to Create a Simple Python Flask App

## 1. Step 1: Install Flask
```bash
pip install Flask
```

This command installs Flask using Python's package manager, `pip`.

## 2. Step 2: Create a Flask Application
Create a new file, say `app.py`, with the following content:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

Explanation:
- `Flask(__name__)`: This line creates a new Flask app instance.
- `@app.route('/')`: This decorator defines the URL route. In this case, the root URL (`/`) will trigger the `home()` function.
- `app.run(debug=True)`: Runs the Flask application in debug mode, which means it will automatically reload when changes are made.

## 3. Step 3: Run the Flask Application
```bash
python app.py
```

Running this command will start the Flask development server locally. The default port is `5000`, so you can access the app by visiting `http://localhost:5000/` in your browser.

---

# Step-by-Step Procedure to Add More Features to the Flask App

## 1. Adding Dynamic Routes with URL Parameters

Modify the existing `app.py` file to include dynamic routing.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
```
#### Explanation:

- @app.route('/greet/<name>'): This route will accept a dynamic URL parameter name. For example, if you visit /greet/John, the response will be "Hello, John!"
- This demonstrates how you can use Flask to create more dynamic web pages that change based on user input or parameters.
### Step 2: Run the application again.

```bash
python app.py
```

---

## 2. Adding HTML Templates with Jinja2
Flask uses the Jinja2 template engine to render HTML. Let’s add a simple HTML template.
Create a new directory called `templates` in the same folder as your `app.py` file. Inside this `templates` folder, create a new file called `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
```
#### Explanation:

- This is a basic HTML file that uses the Jinja2 template syntax to insert dynamic data. The {{ message }} is a placeholder for content passed from the Flask application.
### Step 2: Modify app.py to render this template.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message="Welcome to the Flask App!")

if __name__ == '__main__':
    app.run(debug=True)
```
#### Explanation:

- render_template(): This function renders the index.html file and passes the message variable, which will be injected into the template.

### Step 3: Run the app and visit http://localhost:5000/ to see your message in the HTML template.

---

## 3. Handling POST Requests and Forms
Next, let’s create a simple form where users can input their name, and the app will greet them personally.
Add a new HTML form in the `index.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
</head>
<body>
    <h1>{{ message }}</h1>
    <form method="POST" action="/greet">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>

```
#### Explanation:

- This form will send a POST request to the /greet route with the user's input.

### Step 2: Modify app.py to handle POST requests.

```python
from flask import Flask, render_template, request

@app.route('/')
def home():
    return render_template('index.html', message="Enter your name below:")

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
```
#### Explanation:

- request.form: Retrieves the form data submitted in a POST request.
- methods=['POST']: Specifies that this route will accept POST requests.

### Step 3: Run the application and enter a name into the form at http://localhost:5000/. The app will respond with a personalized greeting based on the input.
---

## 4. Adding Error Handling (404 Page Not Found)
Flask makes it easy to customize error pages like "404 Page Not Found."
Create a `404.html` file inside the `templates` folder:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>Oops! This page doesn't exist.</h1>
    <p>Go back to <a href="/">home</a>.</p>
</body>
</html>
```

Add the error handler in `app.py`:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message="Enter your name below:")

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello, {name}!"

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

```
#### Explanation:

- @app.errorhandler(404): This decorator handles 404 errors and renders the 404.html template when a page is not found.

### Step 3: Run the app and visit a non-existent page like http://localhost:5000/invalid. It will show the custom 404 page.
---

## 5. Serving Static Files (CSS/Images)

Create a `static` folder in your project directory. Inside this folder, create a `style.css` file:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    text-align: center;
}
```

Modify your `index.html` to include this stylesheet:

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>{{ message }}</h1>
    <form method="POST" action="/greet">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>

```
#### Explanation:

- {{ url_for('static', filename='style.css') }}: Flask uses url_for to generate the URL for static files.

Run the app and see how the CSS is applied.
