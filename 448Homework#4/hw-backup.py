import fileinput

class Book:
	#Book object containing all information pertaining to a specific book
	def __init__(self, ID, author, title, genre, price):
		self.ID = ID #This is not displayed, but it was provided so we inputted it
		self.author = author
		self.title = title
		self.genre = genre
		self.price = price

class BookList:
	#all books in the list must have a unique title
	def __init__(self):
		self.bookList = [] #Contains a booklist
	def addBook(self, ID, author, title, genre, price): 
		#Adds a book to list, books are added alphabetically by title
		#All info must be inputted manually
		for index, item in enumerate(self.bookList):
			if item.title == title:
				print('THAT TITLE IS ALREADY IN THE LIST')
		for index, item in enumerate(self.bookList):
			if title < item.title:
				self.bookList.insert(index, Book(ID, author, title, genre, price))
				return
		self.bookList.append(Book(ID, author, title, genre, price))
	def addBook2(self, Book):
		#This adds a book via book item.
		self.addBook(Book.ID, Book.author, Book.title, Book.genre, Book.price)
	def removeBook(self, title):
		#Removes book with inputted title from list
		if len(self.bookList) == 0:
			print('NO BOOKS IN LIST')
			return False
		for index, item in enumerate(self.bookList):
			if item.title == title:
				self.bookList.pop(index)
				return True
		print('BOOK TITLE IS NOT IN LIST')
		return False
	def getTotalCost(self):
		#Adds the cost of all books in the list
		totalCost = 0
		if len(self.bookList) == 0:
			return 0
		for index, item in enumerate(self.bookList):
			totalCost = totalCost + item.price 
		return totalCost

def displayList(BookList):
	#Displays all books in inputted booklist
	for item in BookList.bookList:
		#print('ID: ' + str(item.ID))
		print('Author: ' + str(item.author))
		print('Title: ' + str(item.title))
		print('Genre: ' + str(item.genre))
		print('Price: $' + str(item.price))
		print('--------')

class Library:
	def __init__(self):
		#Books can be added manually
		#for initialization books in files are added automatically
		#files must be in the format
			#Genre
			#Price as an integer number
			#ID
			#Author
			#Title
			#ID Author and Title can be repeated for any number of books
			#Each genre must be a different file.
		self.List = BookList()
		count = 1
		for line in fileinput.input('SciFi($50).txt'):
			if count == 1:
				genre = line.rstrip()
				count = 2
			elif count == 2:
				price = int(line.rstrip())
				count = 3
			elif count == 3:
				ID = line
				count = 4
			elif count == 4:
				author = line.rstrip()
				count = 5
			elif count == 5:
				title = line.rstrip()
				self.List.addBook(ID, author, title, genre, price)
				count = 3
		count = 1
		for line in fileinput.input('Travel($40).txt'):
			if count == 1:
				genre = line.rstrip()
				count = 2
			elif count == 2:
				price = int(line.rstrip())
				count = 3
			elif count == 3:
				ID = line
				count = 4
			elif count == 4:
				author = line.rstrip()
				count = 5
			elif count == 5:
				title = line.rstrip()
				self.List.addBook(ID, author, title, genre, price)
				count = 3
		count = 1
		for line in fileinput.input('SoftwareEngineering($100).txt'):
			if count == 1:
				genre = line.rstrip()
				count = 2
			elif count == 2:
				price = int(line.rstrip())
				count = 3
			elif count == 3:
				ID = line
				count = 4
			elif count == 4:
				author = line.rstrip()
				count = 5
			elif count == 5:
				title = line.rstrip()
				self.List.addBook(ID, author, title, genre, price)
				count = 3
	def addBook(self, ID, author, title, genre, price): #adds book to library
		self.List.addBook(ID, author, title, genre, price)
	def removeBook(self, title): #removes book from library
		self.List.removeBook(title)
	def showList(self): #shows all books in library
		displayList(self.List)
	def viewByGenre(self, genre): #shows all books of a given genre
		self.tempList = BookList()
		for item in self.List.bookList:
			if item.genre == genre:
				self.tempList.addBook2(item)
		print('Viewing all ' + genre + ' books.')
		displayList(self.tempList)
	def getBookBytitle(self, title): #retrieves a book item by the books title
		for item in self.List.bookList:
			if item.title == title:
				return item
		print('THAT BOOK TITLE IS NOT AVAILABLE')
		return False

class Order:
	def __init__(self):
		#each order contains its own booklist
		self.List = BookList()
	def addBook(self, Library, title): 
		#adds book that is available at a library by title
		self.book = Library.getBookBytitle(title)
		if self.book == False:
			print('FAILED TO ADD BOOK')
			return
		self.List.addBook2(self.book)
	def removeBook(self, title):
		#removes a given title from the order
		self.List.removeBook(title)
	def viewList(self):
		#displays entire order
		print('Viewing current order')
		displayList(self.List)
	def getTotalCost(self):
		#displays total cost of all books in order
		return self.List.getTotalCost()

class User_Controller:
	#a user can only have one order
	def __init__(self):
		#user controller initializes both a library for use and an order
		self.Lib = Library()
		self.Order = Order()
		selection = 0
		while selection != '6':
			#prompts for input
			print("Please choose an action:")
			print("1 - View All Books")
			print("2 - View by Genre")
			print("3 - Add to Order")
			print("4 - Remove from Order")
			print("5 - View Total Cost")
			print("6 - Checkout")
			selection = raw_input()
			#number must be entered first, then other inputs
			if selection == '1':
				self.viewAll(self.Lib)
			elif selection == '2':
				stuff = raw_input("What Genre would you like to view? ")
				self.viewGenre(self.Lib, stuff)
			elif selection == '3':
				stuff = raw_input("What Title would you like to add? ")
				self.addToOrder(self.Lib, stuff)
			elif selection == '4':
				stuff = raw_input("What Title would you like to remove? ")
				self.removeFromOrder(stuff)
			elif selection == '5':
				self.viewTotalCost()
			elif selection == '6':
				self.viewOrder()
				self.viewTotalCost()
	def viewAll(self, Library):
		#displays all books in the library
		Library.showList()
	def viewGenre(self, Library, genre):
		#displays books by genre
		Library.viewByGenre(genre)
	def addToOrder(self, Library, title):
		#adds book to order by title
		self.Order.addBook(Library, title)
		self.viewOrder()
	def removeFromOrder(self, title):
		#removes book with given title from order
		self.Order.removeBook(title)
		self.viewOrder()
	def viewOrder(self):
		#displays current order
		self.Order.viewList()
	def viewTotalCost(self):
		#displays price
		print('TOTAL COST: $' + str(self.Order.getTotalCost()))




#Lib = Library()
#Lib.addBook(1, 'a', 'Sci Fi', 2)
#Lib.addBook(2, 'b', 'Sci Fi', 2)
#Lib.addBook(3, 'c', 'Sci Fi', 2)
#Lib.addBook(4, 'd', 'Horror', 4)
#Lib.addBook(5, 'e', 'Horror', 4)
#Lib.addBook(6, 'f', 'Horror', 4)
U = User_Controller() #initializes a user controller
#U.viewAll(Lib)
#U.viewGenre(Lib, 'Travel')
#U.addToOrder(Lib, 'Arctic Dreams')
#U.addToOrder(Lib, 'A Winter in Arabia')
#U.addToOrder(Lib, 'The Forever War')
#U.addToOrder(Lib, 'Code Complete: A Handbook of Software Construction')
#U.removeFromOrder('The Forever War')
#U.viewOrder()
#U.viewTotalCost()
