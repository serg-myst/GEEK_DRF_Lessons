# Тестовые классы для проверки сериализатора Lesson_3

class Author:
    def __init__(self, name, birthday_year):
        self.name = name
        self.birthday_year = birthday_year

    def __str__(self):
        return self.name


class Biography:
    def __init__(self, text, author):
        self.text = text
        self.author = author


class Book:
    def __init__(self, name, authors):
        self.name = name
        self.authors = authors


class Article:
    def __init__(self, name, author):
        self.name = name
        self.author = author
