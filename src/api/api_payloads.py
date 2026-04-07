import random
import string


def generate_isbn():
    return ''.join(random.choices(string.ascii_lowercase, k=4))


def generate_aisle():
    return str(random.randint(1000, 9999))


def add_book_payload():

    isbn = generate_isbn()
    aisle = generate_aisle()

    payload = {
        "name": "Learn API Automation",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Chinmaya"
    }

    return payload, isbn + aisle