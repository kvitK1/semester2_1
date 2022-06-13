
from geopy.geocoders import Nominatim
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

def name_k(name):
    return f'{name} is ...'



@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('tte.html')

@app.route('/<usr>')
def user(usr):
    return f'<h1>{name_k(usr)}</h1>'




if __name__ == '__main__':
    app.run(debug=True)