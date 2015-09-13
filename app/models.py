from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    pictures = db.relationship('Picture', backref='post', lazy='dynamic')
    thumbnail_index = db.Column(db.Integer)

    def serialize(self):
        picture_list = []
        pictures = self.pictures.all()
        for picture in pictures:
            picture_list.append(picture.serialize())

        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'pictures': picture_list,
            'thumbnailIndex': self.thumbnail_index
        }


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def serialize(self):
        return {
            'source': self.source
        }
