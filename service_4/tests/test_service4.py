from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_Stokes(self):
        response = self.client.post(url_for('runs'), json=dict(player="Stokes", team="Bangladesh"))
        self.assertIn(b'century scored', response.data)
        
    def test_Flintoff(self):
        response = self.client.post(url_for('runs'), json=dict(player="Flintoff", team="Pakistan"))
        self.assertIn(b'century scored', response.data)

    def test_Shakib(self):
        response = self.client.post(url_for('runs'), json=dict(player="Shakib", team="England"))
        self.assertIn(b'double hundred', response.data)