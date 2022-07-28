from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World! trying debug mode</h1>"

@app.route('/about/')
def about_page():
    return f'<h1>About Pagee of !!</h1>'

# Dynamic Routes!!!  ==> <username>
@app.route('/about/<username>')
def about_page_username(username):
    return f'<h1>About Pagee of {username}!!!</h1>'
