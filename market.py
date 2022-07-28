from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home/')  # adding muliple routes to the same method
def home_page():
    return render_template('home.html')

@app.route('/market/')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)


# Dynamic Routes!!!  ==> <username>
@app.route('/about/<username>')
@app.route('/about/')  # adding multiple routes to the same method
def about_page_username(username=None):
    txt = username if username else 'Nobody'
    return f'<h1>About Pagee of {txt}!!!</h1>'

