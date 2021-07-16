from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock 

from application import app, db
from application.models import Players

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Players(name="Stokes", team="England", runs="century scored"))
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        db.session.remove()

class TestResponse(TestBase):
    def test_index(self):
        with requests_mock.mock() as m:
            m.get("http://cricket_project_player_backend:5001/player", text='Stokes')
            m.get("http://cricket_project_team_backend:5002/team", text='England')
            m.post("http://cricket_project_runs_backend:5003/runs", text='century scored')
            response = self.client.get(url_for('index'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'century scored', response.data)
