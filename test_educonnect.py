import unittest
from flask import Flask, jsonify
from app import app

class EduConnectTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_user_authentication(self):
        response = self.app.post('/login', data=dict(
            username="testuser",
            password="testpassword"
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login successful", response.data)

    def test_project_submission(self):
        self.app.post('/login', data=dict(
            username="testuser",
            password="testpassword"
        ))
        response = self.app.post('/submit_project', data=dict(
            project_name="Sample Project",
            description="This is a test project.",
            repository_link="https://github.com/varadraj6055/sample-project"
        ))
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Project submitted successfully", response.data)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
