# -*- coding: utf-8 -*-
from Catalog import Catalog
from Book import Book
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name,days=10):
        pass
    
    #assume name is unique
    def returnBook(self,name):
        pass
        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,catalog,name,author,publish_date,pages):
        catalog.addBook(name,author,publish_date,pages)
    
    def removeBook(self,name):
        book_item=name
        Book.removeBookItem(book_item)
    
    def removeBookItemFromCatalog(self,catalog,book,isbn):
        name = book
        catalog.removeBookItem(name,isbn)
    
    
        