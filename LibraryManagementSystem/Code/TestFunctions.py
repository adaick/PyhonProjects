# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

#b1 = Book('Shoe Dog','Phil Knight', '2015',312)
#b1.addBookItem('123hg','H1B2')
#b1.addBookItem('124hg','H1B3')

#b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '124hg','H1B4')
catalog.addBookItem(b, '125hg','H1B5')

c = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(c, '463hg','K1B2')

catalog.displayAllBooks()
print("----------------------")

m1 = Member(" Vish "," Bangalore ",23,' asljlkj22 ',' std1233 ')

librarian = Librarian(" Awantik "," Bangalore ",34,' asljlkj22 ',' zeke101 ') 
print (m1)
print("----------------------")
print (librarian)
print("----------------------")

book = catalog.searchByName('Shoe Dog')
print (book)
print("----------------------")


catalog.removeBookItem('Shoe Dog','124hg')
catalog.displayAllBooks()
print("----------------------")
librarian.addBook(catalog,'Shoe Dog','Phil Knight', '2015',312)
catalog.displayAllBooks()
print("----------------------")
librarian.removeBookItemFromCatalog(catalog,'Shoe Dog','125hg')
catalog.displayAllBooks()
print("----------------------")
librarian.removeBook(c,'Moonwalking with Einstien')
catalog.displayAllBooks()
print("----------------------")
librarian.addBookItem(catalog,c, '126hg','H1B6')
catalog.displayAllBooks()
print("----------------------")
m1.issueBook(catalog,'Shoe Dog')
catalog.displayAllBooks()
print("----------------------")
m1.returnBook(b,'Shoe Dog')
catalog.displayAllBooks()
print("----------------------")
b = catalog.searchByName('Shoe Dog')
print (b)
print("----------------------")


catalog.removeBookItem('Shoe Dog','124hg')
catalog.displayAllBooks()
print("----------------------")
librarian.addBook(catalog,'Shoe Dog','Phil Knight', '2015',312)
catalog.displayAllBooks()
print("----------------------")
librarian.removeBookItemFromCatalog(catalog,'Shoe Dog','125hg')
catalog.displayAllBooks()
print("----------------------")
librarian.removeBook(c,'Moonwalking with Einstien')
catalog.displayAllBooks()
print("----------------------")
librarian.addBookItem(catalog,c, '126hg','H1B6')
catalog.displayAllBooks()
print("----------------------")
m1.issueBook(catalog,'Shoe Dog')