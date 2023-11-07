from .database import db

class User(db.Model):
  __tablename__ = 'User'
  id = db.Column(db.String(36), primary_key=True)
  nome = db.Column(db.String(80), unique=False, nullable=False)

  def get_id(self):
      return str(self.id)
  
  def to_dict(self):
    return {
        'id': self.id,
        'nome': self.nome,
    }
  
  def __init__(self, id, nome):
      self.id = id
      self.nome = nome
