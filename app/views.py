from flask import render_template, jsonify
from app import app, db, models


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/auth')
@app.route('/login')
def auth():
    return render_template('auth.html')
