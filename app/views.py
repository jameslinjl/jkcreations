from flask import render_template, jsonify, request
from app import app


posts = [
    {
        'author': {'nickname': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'nickname': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
]


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


@app.route('/api', methods=['GET'])
def api_call():
    return jsonify(results=posts)
