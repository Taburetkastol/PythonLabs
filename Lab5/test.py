import unittest
import date
import book



class DateTest(unittest.TestCase):
    def test_year(self):
        self.assertTrue(date.Date.check_even_year(date.Date(), year=4))
        self.assertFalse(date.Date.check_even_year(date.Date(), year=5))

    def test_days(self):
        self.assertEqual(book.Book.days_of_book(book.Book()), 18583)


if __name__ == '__test__':
    unittest.test()