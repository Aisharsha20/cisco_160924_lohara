class Book:
    def __init__(self, id, title, price, copies):
        self.id = id
        self.title = title
        self.price = price
        self.copies = copies
        
    def __str__(self):
        return f'[id={self.id}, title={self.title}, price={self.price}, copies={self.copies}]'
    
    def __repr__(self):
        return self.__str__()


# 2. books[]
books = []


# 3. book_add(id, title, price, copies)
def book_add(id, title, price, copies):
    global books
    book = Book(id, title, price, copies)
    books.append(book)


# 4. book_remove(id)
def book_remove(id):
    global books
    for book in books:
        if book.id == id:
            print(book)
            if input('Are you sure to delete (yes/no)? ').lower() == 'yes':
                books.remove(book)
                print('Book deleted successfully')
            return
    print(f'No such book with id {id}')


# 5. book_readbyid(id)
def book_readbyid(id):
    global books
    for book in books:
        if book.id == id:
            print(book)
            return
    print(f"Book with id {id} not found.")


# 6. book_updatebyid(id)
def book_updatebyid(id):
    global books
    for book in books:
        if book.id == id:
            title = input("Enter new title for the book: ")
            price = float(input("Enter new price for the book: "))
            copies = int(input("Enter new number of copies: "))
            book.title = title
            book.price = price
            book.copies = copies
            print(f"Book with id {id} has been updated.")
            return
    print(f"Book with id {id} not found.")


# 7. book_display()
def book_display():
    global books
    for book in books:
        print(book)


# 8. menu
def menu():
    choice = int(input('''1 - Add book
2 - Delete book by id
3 - Display all books
4 - Read book by id
5 - Update book by id
6 - End
Your choice: '''))
    
    if choice == 1:
        id = int(input('Enter book id: '))
        title = input('Enter book title: ')
        price = float(input('Enter book price: '))
        copies = int(input('Enter number of copies: '))
        book_add(id, title, price, copies)
    elif choice == 2:
        id = int(input('Enter book id to delete: '))
        book_remove(id)
    elif choice == 3:
        book_display()
    elif choice == 4:
        id = int(input('Enter book id to read: '))
        book_readbyid(id)
    elif choice == 5:
        id = int(input('Enter book id to update: '))
        book_updatebyid(id)
    elif choice == 6:
        pass
    else:
        print('Invalid menu')
    
    return choice


# 9. menus
def menus():
    choice = menu()
    while choice != 6:
        choice = menu()
    print('Thank you for using the library management system.')


# 10. driver program
menus()
