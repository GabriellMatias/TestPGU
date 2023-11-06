from .database import db

class User(db.Model):
  __tablename__ = 'User'
  id = db.Column(db.String(36), primary_key=True)
  name = db.Column(db.String(80), unique=False, nullable=False)

  def get_id(self):
      return str(self.id)
  
  def to_dict(self):
    return {
        'id': self.id,
        'name': self.name,
    }
  
  def __init__(self, id, name):
      self.id = id
      self.name = name
