import unittest
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from app import app, db, Registro, calcular_horas_trabalhadas

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_calcular_horas_trabalhadas(self):
        entrada_manha = "09:00"
        saida_noite = "18:00"
        result = calcular_horas_trabalhadas(entrada_manha, saida_noite)
        self.assertEqual(result, 8.0)

    def test_index_route_post(self):
        with self.app as client:
            response = client.post('/', data={'entrada_manha': '09:00', 'saida_noite': '18:00'})
            self.assertEqual(response.status_code, 200)
            # Adicione mais verificações conforme necessário

    def test_index_route_get(self):
        with self.app as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            # Adicione mais verificações conforme necessário

if __name__ == '__main__':
    unittest.main()
