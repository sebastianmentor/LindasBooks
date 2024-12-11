from unittest.mock import Mock
import unittest
from models import User, Author, Book
from datetime import date

class TestUser(unittest.TestCase):
    def test_user_to_dict(self):
        # Skapa en mock-instans av User
        mock_user = Mock()
        mock_user.id = 1
        mock_user.name = "testuser"
        mock_user.email = "testuser@example.com"
        mock_user.created_at = date.today()

        mock_user.to_dict = User.to_dict

        result = mock_user.to_dict(mock_user)

        correct_result = {
            "id": 1, 
            "name": "testuser", 
            "email": "testuser@example.com", 
            "created":date.today().strftime("%Y-%m-%d")
            }
        
        assert result == correct_result

class TestBook(unittest.TestCase):
    def test_book_to_dict(self):
        mock_book = Mock()
        mock_book.id = 1
        mock_book.title = "Test Book"
        mock_book.author_id = 42
        mock_book.isbn = "123-1-12-123456-0"

        mock_book.to_dict = Book.to_dict

        result = mock_book.to_dict(mock_book)
        correct_result = {
            "id": 1, 
            "title": "Test Book", 
            "author_id": 42,
            "isbn":"123-1-12-123456-0"}
        
        assert result == correct_result


if __name__ == "__main__":
    unittest.main()