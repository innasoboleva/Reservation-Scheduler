import server
import unittest


class MelonTastingIntegrationTestCase(unittest.TestCase):
    """Testing Flask server."""

    def test_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn(b'<h1>Login</h1>', result.data)

    def test_favorite_color_form(self):
        client = server.app.test_client()
        result = client.post('/login', data={'email': 'inna@inna.com', 'password': 'inna'})
        self.assertIn(b'<h1>Welcome</h1>', result.data)


if __name__ == '__main__':
    unittest.main()