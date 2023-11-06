from flask import Flask, Blueprint, render_template
from app.database import db

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

# Iniciando DB
db.init_app(app)

with app.app_context():
    # # Executar operação que requer o contexto da aplicação Flask
    db.create_all()


# Config Rotas
app.register_blueprint(users_bp)

#   ROTA RAIZ
bp_index= Blueprint("main", __name__, static_folder="/static", template_folder="./templates")
@bp_index.route('/')
def index():
    return render_template('users/index.html', title='Gerar Usuarios')


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
