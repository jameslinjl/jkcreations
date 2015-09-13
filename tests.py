#!/usr/bin/env python
import os
import unittest

from config import basedir
from app import app, db, api, models


class TestCaseApi(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def test_posts_api_post(self):
        api.api_post_post()
        pic_source = {'source': 'https://pbs.twimg.com/profile_images/458794430200152064/XdQULww6.png'}
        expected = {'body': unicode('test body'), 'id': 1, 'pictures': [pic_source], 'thumbnailIndex': 0, 'title': unicode('test title')}
        actual = models.Post.query.get(1)
        assert expected['body'] == actual.body
        assert expected['id'] == actual.id
        assert expected['thumbnailIndex'] == actual.thumbnail_index
        assert expected['title'] == actual.title
        assert expected['pictures'][0]['source'] == actual.pictures.all()[0].source

    def test_posts_api_get(self):
        tmp = models.Post(title='test title', body='test body', thumbnail_index=0)
        db.session.add(tmp)
        db.session.commit()
        expected = {'body': 'test body', 'id': 1, 'pictures': [], 'thumbnailIndex': 0, 'title': 'test title'}
        actual = eval(api.api_post_get())[0]
        assert expected == actual

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCaseModels(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def test_post_serialize(self):
        tmp = models.Post(title='test title', body='test body', thumbnail_index=0)
        actual = tmp.serialize()
        expected = {'body': 'test body', 'id': None, 'pictures': [], 'thumbnailIndex': 0, 'title': 'test title'}
        assert expected == actual

    def test_picture_serialize(self):
        tmp = models.Picture(source='https://pbs.twimg.com/profile_images/458794430200152064/XdQULww6.png')
        actual = tmp.serialize()
        expected = {'source': 'https://pbs.twimg.com/profile_images/458794430200152064/XdQULww6.png'}
        assert expected['source'] == actual['source']

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
