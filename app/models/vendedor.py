from app import db
from app import manager

class Vendedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    sexo = db.Column(db.String(50))

db.create_all()
manager.create_api(Vendedor, methods=['POST','DELETE','PUT','GET'])


