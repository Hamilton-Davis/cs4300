import pytest
import numpy
from task1 import hello_world
from task2 import get_data_types
from task3 import check_number, first_n_primes, sum_to_100
from task4 import calculate_discount
from task5 import get_books, get_students
from task6 import count_words
from task7 import array_sum

# test_task1.py

def test_hello_world():
    assert hello_world() == "Hello, World!"

# test_task2.py

def test_data_types():
    data = get_data_types()
    assert isinstance(data["integer"], int)
    assert isinstance(data["float"], float)
    assert isinstance(data["string"], str)
    assert isinstance(data["boolean"], bool)

# test_task3.py

def test_check_number():
    assert check_number(5) == "Positive"
    assert check_number(-3) == "Negative"
    assert check_number(0) == "Zero"

def test_first_n_primes():
    assert first_n_primes(5) == [2, 3, 5, 7, 11]

def test_sum_to_100():
    assert sum_to_100() == 5050

# test_task4.py

def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(50.0, 20) == 40.0

# test_task5.py

def test_get_books():
    books = get_books()
    assert books[:3] == ["Book A", "Book B", "Book C"]

def test_get_students():
    students = get_students()
    assert "Alice" in students and students["Alice"] == 101

# test_task6.py

def test_count_words():
    assert count_words("task6_read_me.txt") > 0

# test_task7.py

def test_array_sum():
    assert array_sum([1, 2, 3, 4]) == 10
