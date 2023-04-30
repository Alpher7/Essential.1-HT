import copy

class Book:
    def __init__(self, name, writer, year, genre):
        self.name = name
        self.writer = writer
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"The book '{self.name}' was written by {self.writer} in {self.year}, genre is {self.genre}"

    def __repr__(self):
        return f"Book(name={repr(self.name)}, writer={repr(self.writer)}, year={self.year}, genre={repr(self.genre)})"


book1 = Book("For Whom the Bell Tolls", "Ernest Hemingway", 1940, "war_novel")

book2 = copy.deepcopy(book1)
book2.name = "A Farewell to Arms"
book2.year = 1929
book2.genre = "Realism"

book3 = Book(name="The Catcher in the Rye", writer="Jerome David Salinger", year=1951, genre="Realistic fiction")

book4 = eval(repr(book1))
book4.name = "A Moveable Feast"
book4.year = 1964
book4.genre = "Autobiography"

print(book1, '\n\t\t', repr(book1), '\n')
print(book2, '\n\t\t', repr(book2), '\n')
print(book3, '\n\t\t', repr(book3), '\n')
print(book4, '\n\t\t', repr(book4), '\n')
