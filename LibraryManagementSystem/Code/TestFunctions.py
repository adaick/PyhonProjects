# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

catalog = Catalog()                                                         # creating object for the Catalog

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)                   # adding new book to the catalog
catalog.addBookItem(b, '123hg','H1B2')                                      # adding book item to catalog according to ISBN and rack no
catalog.addBookItem(b, '124hg','H1B4')                                      # adding book item to catalog according to ISBN and rack no
catalog.addBookItem(b, '125hg','H1B5')                                      # adding book item to catalog according to ISBN and rack no

c = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)       # adding new book to the catalog
catalog.addBookItem(c, '463hg','K1B2')                                      # adding book item to catalog according to ISBN and rack no

catalog.displayAllBooks()                                                   # this line will display available books in catalog
print("----------------------")

book = catalog.searchByName('Shoe Dog')                                     # searching book by name
print(book)
print("----------------------")

m1 = Member(" Vish "," Bangalore ",23,' asljlkj22 ',' std1233 ')            # creating object for member

librarian = Librarian("Awantik "," Bangalore ",34,' asljlkj22 ',' zeke101') # creating object for librarian
print (m1)                                                                  # printing details of member
print("----------------------")
print (librarian)                                                           # printing details of librarian
print("----------------------")

librarian.displayAllBooks(catalog)                                          # this line will display available books in catalog
print("----------------------")


catalog.removeBookItem('Shoe Dog','124hg')                                  # removing book item from catalog using name and ISBN no
catalog.displayAllBooks()                                                   # this line will display available books in catalog
print("----------------------")
librarian.addBook(catalog,'Shoe Dog','Phil Knight', '2015',312)             # librarian adding new book to catalog
catalog.displayAllBooks()                                                   # this line will display available books in catalog
print("----------------------")
librarian.removeBookItemFromCatalog(catalog,'Shoe Dog','125hg')             # librarian removing book item from catalog
catalog.displayAllBooks()                                                   # this line will display available books in catalog
print("----------------------")
librarian.removeBook(c,'Moonwalking with Einstien')                         # librarian reoving book from catalog
catalog.displayAllBooks()                                                   # this line will display available books in catalog
print("----------------------")
librarian.addBookItem(catalog,c, '126hg','H1B6')                            # librarian adding book item to catalog using catalog, book, ISBN and rack no
catalog.displayAllBooks()                                                   # this line will display available books in catalog
print("----------------------")
m1.issueBook(catalog,'Shoe Dog')                                            # member issuing book from library
catalog.displayAllBooks()                                                   # this line will display available books in catalog
print("----------------------")
m1.returnBook(b,'Shoe Dog')                                                 # member returning book to library
catalog.displayAllBooks()                                                   # this line will display available books in catalog
print("----------------------")
