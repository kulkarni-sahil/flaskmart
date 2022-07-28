from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home/')  # adding muliple routes to the same method
def home_page():
    return render_template('home.html')

# Dynamic Routes!!!  ==> <username>
@app.route('/about/<username>')
@app.route('/about/')  # adding multiple routes to the same method
def about_page_username(username=None):
    txt = username if username else 'Nobody'
    return f'<h1>About Pagee of {txt}!!!</h1>'
