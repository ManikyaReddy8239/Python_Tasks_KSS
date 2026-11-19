'''16. Library Management System (Constructor & Inheritance) 
A library stores information about books and digital books.
Create a base class Book with a constructor to initialize book details.
Create a derived class EBook that adds file 
size information. 
'''

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_book(self):
        print("Book Title:",self.title)
        print("Book Author:",self.author)
class EBook(Book):
    def __init__(self,title,author,file_size):
        self.title=title
        self.author=author
        self.file_size=file_size
    def display_ebook(self):
        self.display_book()
        print("File size:",self.file_size,"MB")
obj=EBook("Python Programming","John",5)
obj.display_ebook()
