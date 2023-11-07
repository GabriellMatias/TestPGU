from flask import Flask, Blueprint, render_template
from uuid import uuid4

from app.database import db
from app.models import User
#BluePrint Rotas
from app.routes import users_bp

# criação do app
app = Flask(__name__, static_folder="./static", template_folder="./templates")
app.config['SECRET_KEY'] = 'TESTKEY'


## DATABASE ##
# Configuração da base de dados SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///TestPGU.db"
# Configuração para rastrear modificações de objetos SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Configuração da senha secreta para segurança do app
app.config['SECRET_KEY'] = 'TESTKEY'


# Criando SEED temporaria
def seed_database():
    db.create_all()
    try:
        for i in range(10):
            user = User(str(uuid4()), f'User Numero {i+1}')
            db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(f"Ocorreu um erro ao gerar a seed {e}")



# Iniciando DB
db.init_app(app)

with app.app_context():
    db.create_all()
    #Seed temporario
    #seed_database()

#   ROTA RAIZ
bp_index= Blueprint("main", __name__, static_folder="static", template_folder="./template")
@bp_index.route('/')
def index():
    return render_template('index.html', title='Gerar Usuarios')



# Config Rotas
app.register_blueprint(users_bp)
app.register_blueprint(bp_index)

### Adicionais que poderiam ser implantados ###

# Flask Migrate
# migrate = Migrate(app, db)

# Envoriment
#load_dotenv()

# Autenticacao
# login_manager = LoginManager()
# login_manager.init_app(app) 

# @login_manager.user_loader
# def load_user(user_id):
#     user = User.query.get(user_id)

if __name__ == '__main__':
  app.run(debug=True)
