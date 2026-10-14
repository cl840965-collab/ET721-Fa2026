"""
Claudio Lopez
Oct 13, 2026
lab 10: intro to flask 
"""
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    name = "Claudio Lopez"
    fruits = ['apple', 'pineapple', 'orange']
    return render_template("index.html", username=name, listfruits=fruits)

@app.route('/about')
def about():
    images = [
        "static/img/photo(1).png",
        "static/img/photo(2).png",
        "static/img/photo(3).jpg"
    ]
    return render_template("about.html", images=images)
@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)