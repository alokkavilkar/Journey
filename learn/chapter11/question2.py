# Library Management System:

# Create a Python class for a library book with attributes like title, author, and availability.Develop methods to borrow and return books, and to search for books by title or author.Utilize inheritance to differentiate between fiction and non-fiction books, each with their own unique properties.


class LibarySystem:

    @staticmethod
    def present_books(books_list):
        return books_list

    def __init__(self, name:str, location:str, year:int) -> None:
        self.name = name
        self.location = location
        self.year = year
        self.books = {'book_title': []}
        self.catalog = []

    def add_books(self, book):
        self.books['book_title'].append(book)

        
    def borrow(self, book_title, for_days):
        if self.books.get('book_title').count(book_title) > 0:
            self.books['book_title'].remove(book_title)
            self.catalog.append((book_title, for_days))
            print(f'successfully purchased book entitled {book_title} for {for_days}')
        else:
            print(f'{book_title} no found please come tommorrow')


    def return_book(self, book_title):
        pass
    
    def book_details(self):
        print(f'Welcome in {self.name} here are the book that are present in this libary')
        print(f"{self.present_books(self.books.get('book_title'))}")








lib = LibarySystem('Central Libary', 'Mumbai', 2024)

lib.add_books('Monk who sold his ferrari')
lib.add_books('Subconsious mind')
lib.book_details()
lib.borrow('Monk who sold his ferrari', 30)
lib.book_details()
lib.borrow('Monk who sold his ferrari', 20)


