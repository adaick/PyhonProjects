# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []
        
    #Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        return b
    
    #Only available to admin
    #this function will add book item to the catalog 
    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)

    #this function will search book by its name    
    def searchByName(self,name):
        for book in self.books:
            if name.strip() == book.name:
                return book
    
    #this function will search book by its author name
    def searchByAuthor(self,author):
        for book in self.books:
            if author.strip() == book.author:
                return book
    
    #this function will display all book which are available in catalog
    def displayAllBooks(self):
        print ('Different Book Count',self.different_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        
        print ('Total Book Count',c)

    #this function will remove th ebook item from catalog    
    def removeBookItem(self,name,isbn):
        book = self.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)
