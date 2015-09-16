#!/usr/bin/env python
import os
import unittest
import json

from config import basedir
from app import app, db, models
from flask import request
from werkzeug.datastructures import ImmutableMultiDict


class TestCaseApi(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def test_posts_api_post(self):
        post_data = ImmutableMultiDict([('body', u'test body'),
            ('title', u'test title'), ('thumbnailIndex', u'0'),
            ('pictures[]', u'www.appnexus.com'),
            ('pictures[]', u'www.google.com'),
            ('pictures[]', u'www.facebook.com')])

        self.app.post('/api/post/post', data=post_data)
        actual = models.Post.query.get(1)
        expected = {
            'body': 'test body',
            'pictures': [
                'www.appnexus.com',
                'www.google.com',
                'www.facebook.com'
            ],
            'id': 1,
            'thumbnailIndex': 0,
            'title': 'test title'
        }

        assert expected['body'] == actual.body
        assert expected['id'] == actual.id
        assert expected['thumbnailIndex'] == actual.thumbnail_index
        assert expected['title'] == actual.title
        assert expected['pictures'][0] == actual.pictures.all()[0].source
        assert expected['pictures'][1] == actual.pictures.all()[1].source
        assert expected['pictures'][2] == actual.pictures.all()[2].source

    def test_posts_api_get(self):
        tmp_post = models.Post(title='test title',
            body='test body', thumbnail_index=0)
        tmp_pic1 = models.Picture(source='www.appnexus.com', post=tmp_post)
        tmp_pic2 = models.Picture(source='www.google.com', post=tmp_post)
        tmp_pic3 = models.Picture(source='www.facebook.com', post=tmp_post)
        db.session.add(tmp_post)
        db.session.add(tmp_pic1)
        db.session.add(tmp_pic2)
        db.session.add(tmp_pic3)
        db.session.commit()

        expected_status = 200
        expected_data = {'results': [{
            'body': 'test body',
            'id': 1,
            'pictures': [
                {'source': 'www.appnexus.com'},
                {'source': 'www.google.com'},
                {'source': 'www.facebook.com'}
            ],
            'thumbnailIndex': 0,
            'title': 'test title'
        }]}

        response = self.app.get('/api/post/get')
        actual_status = response.status_code
        actual_data = json.loads(response.data)

        self.assertEqual(actual_status, expected_status)
        self.assertEqual(actual_data, expected_data)

    def test_posts_delete(self):
        tmp_post = models.Post(title='test title',
            body='test body', thumbnail_index=0)
        tmp_pic1 = models.Picture(source='www.appnexus.com', post=tmp_post)
        tmp_pic2 = models.Picture(source='www.google.com', post=tmp_post)
        tmp_pic3 = models.Picture(source='www.facebook.com', post=tmp_post)
        db.session.add(tmp_post)
        db.session.add(tmp_pic1)
        db.session.add(tmp_pic2)
        db.session.add(tmp_pic3)
        db.session.commit()

        self.app.delete('/api/post/delete?id=1')
        actual = models.Post.query.all()
        expected = []
        assert actual == expected

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
