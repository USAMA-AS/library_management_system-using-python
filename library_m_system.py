from json.tool import main


class Library:

    def __init__(self, listOfBooks) -> None:
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present in this library are: ")
        for book in self.books:
            print(book)


    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been Issued this book {bookName}. return it.")
            self.books.remove(bookName)
            return True
        else:
            print("Soory! This book is Borrowed")
        return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning book!")


class Student:

    def requestBook(self):
        self.book= input("Enter the name of the book you borrow: ")
        return self.book

    def returnBook(self):
        self.book= input("Enter the name of the book you Return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Alogrithms", "django", "chris", "python"])
    student = Student()
    
    while(True):
        welcomeMsg= '''\n === Welcome to Libraray ===
        Please choose an option:
        1. Listing All the Books
        2. Request a book
        3. Add/Return a book
        4. Exist the Library
        '''

        print(welcomeMsg)

        a= int(input("Enter a Choice: "))

        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a ==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4: 
            print("Thanks for chossing library")
            exit()
        else:
            print("invalid choice")
        