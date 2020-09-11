from Library import *

print("""
-------------------------------------      
*                                   *
*  ----Welcome to Library Menu----  *
*                                   *
*     1. Show Books:                *
*     2. Search Books:              *
*     3. Add a Book:                *
*     4. Delete a Book:             * 
*     to exit press 'q'.            *
*                                   *
-------------------------------------
""")

library = Core_library()

while True:
    operation = input("Please, choice an operation: ")
    
    if(operation == "q" or operation == "Q"):
        print("Your process is ending...")
        print("Exit.")
        break
    
    elif(operation == "1"):
        library.show_books()
        
    elif(operation == "2"):
        name = input("which book would you like to search?")
        print("Book is searching...")
        time.sleep(2)
        library.search_book(name)
        
    elif(operation == "3"):
        name = input("Enter a book name: ")
        author = input("Enter an author: ")
        publisher = input("Enter publisher: ")
        page = input("Enter page: ")
        new_book = Book(name, author, publisher, page)
        print("Book is adding...")
        time.sleep(2)
        library.add_book(new_book)
        print("Book is added.")
        
    elif(operation == "4"):
        name = input("which book would you like to delete?")
        answer = input("Are you sure?(Y/N)")
        if (answer == "Y" or answer == "y"):
            print("Book is deleting...")
            time.sleep(2)
            library.delete_book(name)
            print("Book is deleted.")
        
    else:
        print("Invalid Operation.")
        
