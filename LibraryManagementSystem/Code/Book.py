# -*- coding: utf-8 -*-
from BookItem import BookItem

class Book:
    def __init__(self,name,author,publish_date,pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []
        
    #this function will add book item to the catalog according to ISBN and rack no
    def addBookItem(self,isbn,rack):
        b = BookItem(self,isbn,rack)
        self.book_item.append(b)
        self.total_count +=1

    #this function will print the book name and author name    
    def printBook(self):
        print (self.name,self.author)
        for book_item in self.book_item:
            print (book_item.isbn)

    #this function will search the book by its ISBN no        
    def searchBookItem(self,isbn):
        for book_item in self.book_item:
            if isbn.strip() == book_item.isbn:
                return book_item

    #this function will remove the book item from catalog        
    def removeBookItem(self,book_item):
        if book_item in self.book_item:
            self.book_item.remove(book_item)
            self.total_count -=1
            
    def __repr__(self):
        return self.name + ' ' + self.author
