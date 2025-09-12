import datetime

class Book:
    def __init__(self, title, author, publication_year):
        #initialize attributes
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        #calculate and return book's age
        current_year = datetime.datetime.now().year
        return current_year - self.publication_year
    
userBook = Book("Two States", "Chetan Bhagat", 2020)
print(f"Book Age: {userBook.get_age()} years")