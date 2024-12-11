from flask import Flask
from database import db
from models import User, Author, Book,create_dummy_data
import json

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost:3306/LindasBokhandel'

db.init_app(app)

@app.route('/')
def index():
    return "Hej och välkommen till Lindas bokhandel!"

@app.route('/users')
def users():
    all_users:list[User] = User.query.all()   
    users_list = []
    for user in all_users:
        users_list.append(user.to_dict())

    return json.dumps(users_list)

@app.route('/authors')
def authors():
    all_authors = Author.query.all()
    return json.dumps(list(map(Author.to_dict, all_authors)))

@app.route('/books')
def books():
    all_books = Book.query.all()    
    return json.dumps(list(map(Book.to_dict, all_books)))


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_dummy_data()
    app.run(debug=True)
