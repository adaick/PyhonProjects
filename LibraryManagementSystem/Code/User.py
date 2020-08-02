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
    members_list = []

    @classmethod
    def addMemberList(cls, member):
        cls.members_list.append(member)

    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issuedbook = []
        Member.addMemberList(self)
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,obj, name,days=10):
        m_name=self.name
        try:
            for book in obj.books:
                if book.name==name:
                    isbn=book.book_item[0].isbn
                    rack=book.book_item[0].rack
            isssued_item=obj.removeBookItem(name,isbn)
            self.issuedbook.extend((name,isbn,rack))
            print('{} successfully Issued'.format(name))
        except  IndexError:
            print('{} Not available'.format(name))
    
    #assume name is unique
    def returnBook(self,obj,name):
        try:
            if name in self.issuedbook:
                isbn=self.issuedbook[1]
                rack=self.issuedbook[2]
            obj.addBookItem(isbn,rack)
            print('{} successfully returned'.format(name))
        except UnboundLocalError:
            print('{} is not issued'.format(name))


        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,catalog,name,author,publish_date,pages):
        catalog.addBook(name,author,publish_date,pages)

    def addBookItem(self,catalog,book,isbn,rack):
        catalog.addBookItem(book,isbn, rack)
    
    def removeBook(self,book,name):
        book.removeBookItem(name)
    
    def removeBookItemFromCatalog(self,catalog,book,isbn):
        name = book
        catalog.removeBookItem(name,isbn)
    
    
        