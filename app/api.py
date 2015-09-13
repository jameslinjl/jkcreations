from flask import jsonify, json, render_template, request
from app import app, db, models


# post service
@app.route('/api/post/get', methods=['GET'])
def api_post_get():
    posts = models.Post.query.all()
    try:
        return jsonify(results=map(models.Post.serialize, posts))
    except:
        results = map(models.Post.serialize, posts)
        return json.dumps(results)


@app.route('/api/post/post', methods=['POST'])
def api_post_post():
    # not legit yet
    tmp = models.Post(title='test title', body='test body', thumbnail_index=0)
    tmp_picture = models.Picture(source='https://pbs.twimg.com/profile_images/458794430200152064/XdQULww6.png', post=tmp)
    # print request.data
    db.session.add(tmp_picture)
    db.session.add(tmp)
    db.session.commit()
    # return render_template('auth.html')
    return 'HTTP 1.1 200 OK\r\n'


# needs specific route for pictures, upload module
