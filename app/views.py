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
def auth():
    return render_template('auth.html')


@app.route('/auth/add')
def auth_add():
    return render_template('auth_add.html')

@app.route('/auth/edit')
def auth_edit():
    return render_template('auth_edit.html')
