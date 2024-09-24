import unittest
from app import app, db
from models import Post, Author

class PostTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            db.create_all()
            author = Author(name="Test Author")
            db.session.add(author)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_post(self):
        response = self.app.post('/api/posts', json={
            'title': 'New Post',
            'content': 'Content of the post',
            'author_id': 1
        }, headers={'Authorization': 'Bearer mysecrettoken'})
        self.assertEqual(response.status_code, 201)

    def test_get_posts(self):
        response = self.app.get('/api/posts', headers={'Authorization': 'Bearer mysecrettoken'})
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        post = Post(title='Test Post', content='Test Content', author_id=1)
        with app.app_context():
            db.session.add(post)
            db.session.commit()

        response = self.app.put(f'/api/posts/{post.id}', json={
            'title': 'Updated Post',
            'content': 'Updated Content'
        }, headers={'Authorization': 'Bearer mysecrettoken'})
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        post = Post(title='Test Post', content='Test Content', author_id=1)
        with app.app_context():
            db.session.add(post)
            db.session.commit()

        response = self.app.delete(f'/api/posts/{post.id}', headers={'Authorization': 'Bearer mysecrettoken'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
