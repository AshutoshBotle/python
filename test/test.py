import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_home(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Deployed python app using the jenkins pipelineeeeee")


if __name__ == "__main__":
    unittest.main()
