from flask import Flask
from views import views
from model import db

app = Flask(__name__)
app.secret_key = '9f4a3e84b2a1c749d73b3c8f5a6c4a1e'

#Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cipher_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize database
db.init_app(app)

#Registering Blueprints
app.register_blueprint(views)

#creating tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=9000)