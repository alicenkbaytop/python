import sqlite3

import time

class Book():
    
    def __init__(self,name,author,publisher,page):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.page = page
        
    def __str__(self):
        return "Book Name: {} \n Author: {} \n Publisher: {} \n Page: {}".format(self.name,self.author,self.publisher,self.page)

class Core_library():
    
    def __init__(self):
        self.create_connection()
        
    def create_connection(self):
        self.connection = sqlite3.connect("new_library.db")
        self.cursor = self.connection.cursor()
        
        query = "CREATE TABLE IF NOT EXISTS Books (Name TEXT, Author TEXT, Publisher TEXT, Page INT)"
        
        self.cursor.execute(query)
        self.connection.commit()
        
    def cut_connection(self):
        self.connection.close()
        
    def show_books(self):
        
        query = "SELECT * FROM Books "
        self.cursor.execute(query)
        
        books = self.cursor.fetchall()
        
        if(len(books) == 0):
            print("There is no book in this library.")
            
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3])
                print(book)
        
    def search_book(self,name):
        query = "SELECT * FROM Books WHERE Name = ?"
        self.cursor.execute(query,(name,))
        
        books = self.cursor.fetchall()
        
        if(len(books) == 0):
            print("There is no book in this library.")
            
        else:
            for i in books:
                book = Book(books[0][0],books[0][1],books[0][2],books[0][3])
                print(book)
        
    def add_book(self,book):
        query = "INSERT INTO Books VALUES(?,?,?,?)"
        self.cursor.execute(query,(book.name, book.author, book.publisher, book.page))
        self.connection.commit()
         

    def delete_book(self,name):
        query = "DELETE FROM Books WHERE Name = ?"
        self.cursor.execute(query,(name,))
        self.connection.commit()
         
