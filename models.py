from database import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def to_dict(self):
        user_dict = {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "created":f"{self.created_at:%Y-%m-%d}"
        }
        return user_dict

    def __str__(self):
        return f"ID: {self.id} -> {self.name} {self.email} gick med {self.created_at:%Y/%m/%d}"
    
    def __repr__(self):
        return f'User({self.name}, {self.email}, {self.created_at:%Y/%m/%d})'


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(100), nullable=False)  
    birthdate = db.Column(db.Date, nullable=False)
    favorit_book = db.Column(db.String(100), nullable=True)

    books = db.relationship('Book', back_populates='author', cascade='all, delete-orphan')

    def to_dict(self):
        user_dict = {
            "id":self.id,
            "name":self.name,
            "birthdate":f"{self.birthdate:%Y-%m-%d}",
            "favorit_book":self.favorit_book
        }
        return user_dict

    def __str__(self):
        return f"ID: {self.id} -> {self.name} born {self.birthdate:%Y/%m/%d}"
    

    def __repr__(self):
        return f'<Author {self.name}>'


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(150), nullable=False)  
    isbn = db.Column(db.String(20), unique=True, nullable=False)  
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    author = db.relationship('Author', back_populates='books')

    def to_dict(self):
        user_dict = {
            "id":self.id,
            "title":self.title,
            "isbn":self.isbn,
            "author_id":self.author_id
        }
        return user_dict

    def __str__(self):
        return f"ID: {self.id} -> {self.title} {self.isbn} {self.author}"
    
    def __repr__(self):
        return f'<Book {self.title} (ISBN: {self.isbn})>'
    

def create_dummy_data():
    """Function needs to run in app.context"""
    if not User.query.all():
        new_user1 = User(name="Sebastian", email="sebastian@example.com")
        new_user2 = User(name="Kalle", email="masterKalle44@example.com")
        new_user3 = User(name="Saturnus", email="stars_master@example.com")
        db.session.add(new_user1)
        db.session.add(new_user2)
        db.session.add(new_user3)

    if not Author.query.all():
        new_author1 = Author(name="J.K.Rowling", birthdate="1955-10-20")
        new_author2 = Author(name="J.R.R Martin", birthdate="1944-12-23")
        new_author3 = Author(name="Kalle Anka", birthdate="1988-11-17")
        db.session.add(new_author1)
        db.session.add(new_author2)
        db.session.add(new_author3)

        db.session.commit()

        if not Book.query.all():
            new_book1 = Book(title="Harry Potter 1", isbn="978-3-16-148410-0", author_id=new_author1.id)
            new_book2 = Book(title="Harry Potter 2", isbn="978-3-16-483920-0", author_id=new_author1.id)
            new_book3 = Book(title="Game of Thrones", isbn="955-2-16-843823-0", author_id=new_author2.id)
            new_book4 = Book(title="Luftens Hjältar", isbn="995-5-22-189010-2", author_id=new_author3.id)
            
            db.session.add(new_book1)
            db.session.add(new_book2)
            db.session.add(new_book3)
            db.session.add(new_book4)
 
            db.session.commit()
        


    