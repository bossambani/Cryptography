from flask import Flask
from flask_cors import CORS
from views import views
from model import db, User
from crypto import crypto
from flask_login import LoginManager

app = Flask(__name__)
CORS(app)
app.secret_key = '9f4a3e84b2a1c749d73b3c8f5a6c4a1e'

#Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cipher_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize database
db.init_app(app)

#Registering Blueprints
app.register_blueprint(views)
app.register_blueprint(crypto, url_prefix='/crypto')


#creating tables if they don't exist
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'views.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run(debug=True, port=9000)