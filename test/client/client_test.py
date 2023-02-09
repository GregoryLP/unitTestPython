import unittest
from unitTestPython.bibliotheque import *

class TestClient(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)
        self.client1 = Client("John Doe")

    def test_check_out_book(self):
        self.client1.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertEqual(len(self.client1.checked_out_books), 1)
        self.assertEqual(self.client1.checked_out_books[0].title, "To Kill a Mockingbird")
        self.assertTrue(self.client1.checked_out_books[0].is_checked_out)

        self.client1.check_out_book(self.library, "Pride and Prejudice")
        self.assertEqual(len(self.client1.checked_out_books), 2)
        self.assertEqual(self.client1.checked_out_books[1].title, "Pride and Prejudice")
        self.assertTrue(self.client1.checked_out_books[1].is_checked_out)

    def test_check_in_book(self):
        self.client1.check_out_book(self.library, "To Kill a Mockingbird")
        self.client1.check_in_book(self.library, "To Kill a Mockingbird")
        self.assertEqual(len(self.client1.checked_out_books), 0)
        self.assertFalse(self.client1.checked_out_books[0].is_checked_out)

        self.client1.check_out_book(self.library, "Pride and Prejudice")
        self.client1.check_in_book(self.library, "Pride and Prejudice")
        self.assertEqual(len(self.client1.checked_out_books), 0)
        self.assertFalse(self.client1.checked_out_books[0].is_checked_out)

if __name__ == "__main__":
    unittest.main()
