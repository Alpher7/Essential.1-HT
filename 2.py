class Review:
    def __init__(self, book, rating, comment):
        self.book = book
        self.rating = rating
        self.comment = comment

    def __repr__(self):
        return f"{self.rating}: {self.comment}"


class Book:
    def __init__(self, name, writer, year, genre):
        self.name = name
        self.writer = writer
        self.year = year
        self.genre = genre
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def __str__(self):
        return f"The book '{self.name}' was written by {self.writer} in {self.year}, " \
               f"genre is {self.genre} \n\t\t {self.reviews}"

    def __repr__(self):
        return f"Book(name={self.name}, writer={self.writer}, year={self.year}, genre={self.genre})"


book1 = Book("For Whom the Bell Tolls", "Ernest Hemingway", 1940, "war_novel")
review1 = Review(book1, 4, "Great book, highly recommend it")
review2 = Review(book1, 5, "One of my all-time favorites")
book1.add_review(review1)
book1.add_review(review2)
print(book1)

book2 = Book("A Farewell to Arms", "Ernest Hemingway", 1929, "Realism")
review3 = Review(book2, 3, "Not my cup of tea, but still a good book")
review4 = Review(book2, 5, "The best Hemingway book I've read")
book2.add_review(review3)
book2.add_review(review4)
print(book2)

book3 = Book("The Catcher in the Rye", "Jerome David Salinger", 1951, "Realistic fiction")
book4 = Book("A Moveable Feast", "Ernest Hemingway", 1964, "Autobiography")
