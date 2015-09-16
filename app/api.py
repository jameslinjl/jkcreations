from flask import jsonify, json, request
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
    data = request.form

    tmp_post = models.Post(title=data['title'],
        body=data['body'], thumbnail_index=data['thumbnailIndex'])
    db.session.add(tmp_post)

    pictures = data.getlist('pictures[]')
    for picture in pictures:
        tmp_pic = models.Picture(source=picture, post=tmp_post)
        db.session.add(tmp_pic)

    db.session.commit()
    return 'HTTP 1.1 200 OK\r\n'


@app.route('/api/post/delete', methods=['DELETE'])
def api_post_delete():
    id = request.args.get('id')
    post_to_delete = models.Post.query.get(id)

    db.session.delete(post_to_delete)
    db.session.commit()
    return 'HTTP 1.1 200 OK\r\n'



# needs specific route for pictures, upload module?
