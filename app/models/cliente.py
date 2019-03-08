from app import db
from app import manager
from app.models import vendedor


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    sexo = db.Column(db.String(10))

    vendendor_id = db.Column(db.Integer, db.ForeignKey('vendedor.id'))
  	#vendedor = db.relationship('Vendedor')

db.create_all()
manager.create_api(Cliente, methods=['POST','GET','PUT','DELETE'])
