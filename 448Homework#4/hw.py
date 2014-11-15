import fileinput

class Book:
	def __init__(self, ID, author, title, genre, price):
		self.ID = ID
		self.author = author
		self.title = title
		self.genre = genre
		self.price = price

class BookList:
	#all books in the list must have a unique ID
	def __init__(self):
		self.bookList = []
	def addBook(self, ID, author, title, genre, price):
		for index, item in enumerate(self.bookList):
			if item.title == title:
				return 'that title is already being used'
		for index, item in enumerate(self.bookList):
			if title < item.title:
				self.bookList.insert(index, Book(ID, author, title, genre, price))
				return
		self.bookList.append(Book(ID, author, title, genre, price))
	def addBook2(self, Book):
		self.addBook(Book.ID, Book.author, Book.title, Book.genre, Book.price)
	def removeBook(self, title):
		if len(self.bookList) == 0:
			print('no books in list')
			return False
		for index, item in enumerate(self.bookList):
			if item.title == title:
				self.bookList.pop(index)
				return True
		print('BOOK TITLE IS NOT IN LIST')
		return False
	def getTotalCost(self):
		totalCost = 0
		if len(self.bookList) == 0:
			return 0
		for index, item in enumerate(self.bookList):
			totalCost = totalCost + item.price 
		return totalCost

def displayList(BookList):
	for item in BookList.bookList:
		#print('ID: ' + str(item.ID))
		print('Author: ' + str(item.author))
		print('Title: ' + str(item.title))
		print('Genre: ' + str(item.genre))
		print('Price: $' + str(item.price))
		print('--------')

class Library:
	def __init__(self):
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


	def addBook(self, ID, author, title, genre, price):
		self.List.addBook(ID, author, title, genre, price)
	def removeBook(self, title):
		self.List.removeBook(title)
	def showList(self):
		displayList(self.List)
	def viewByGenre(self, genre):
		self.tempList = BookList()
		for item in self.List.bookList:
			if item.genre == genre:
				self.tempList.addBook2(item)
		print('Viewing all ' + genre + ' books.')
		displayList(self.tempList)
	def getBookBytitle(self, title):
		for item in self.List.bookList:
			if item.title == title:
				return item
		print('THAT BOOK TITLE IS NOT AVAILABLE')
		return False

class Order:
	def __init__(self):
		self.List = BookList()
	def addBook(self, Library, title):
		self.book = Library.getBookBytitle(title)
		if self.book == False:
			print('FAILED TO ADD BOOK')
			return
		self.List.addBook2(self.book)
	def removeBook(self, title):
		self.List.removeBook(title)
	def viewList(self):
		print('Viewing current order')
		displayList(self.List)
	def getTotalCost(self):
		return self.List.getTotalCost()

class User_Controller:
	#a user can only have one order
	def __init__(self):
		self.Lib = Library()
		self.Order = Order()
		selection = 0
		while selection != '5':
			print("Please choose an action:")
			print("1 - View by Genre")
			print("2 - Add to Order")
			print("3 - Remove from Order")
			print("4 - View Total Cost")
			print("5 - Checkout")
			selection = raw_input()
			if selection == '1':
				stuff = raw_input("What Genre would you like to view? ")
				self.viewGenre(self.Lib, stuff)
			elif selection == '2':
				stuff = raw_input("What Title would you like to add? ")
				self.addToOrder(self.Lib, stuff)
			elif selection == '3':
				stuff = raw_input("What Title would you like to remove? ")
				self.removeFromOrder(stuff)
			elif selection == '4':
				self.viewTotalCost()
			elif selection == '5':
				self.viewOrder()
				self.viewTotalCost()
	def viewAll(self, Library):
		Library.showList()
	def viewGenre(self, Library, genre):
		Library.viewByGenre(genre)
	def addToOrder(self, Library, title):
		self.Order.addBook(Library, title)
		self.viewOrder()
	def removeFromOrder(self, title):
		self.Order.removeBook(title)
		self.viewOrder()
	def viewOrder(self):
		self.Order.viewList()
	def viewTotalCost(self):
		print('TOTAL COST: $' + str(self.Order.getTotalCost()))




#Lib = Library()
#Lib.addBook(1, 'a', 'Sci Fi', 2)
#Lib.addBook(2, 'b', 'Sci Fi', 2)
#Lib.addBook(3, 'c', 'Sci Fi', 2)
#Lib.addBook(4, 'd', 'Horror', 4)
#Lib.addBook(5, 'e', 'Horror', 4)
#Lib.addBook(6, 'f', 'Horror', 4)
U = User_Controller()
#U.viewAll(Lib)
#U.viewGenre(Lib, 'Travel')
#U.addToOrder(Lib, 'Arctic Dreams')
#U.addToOrder(Lib, 'A Winter in Arabia')
#U.addToOrder(Lib, 'The Forever War')
#U.addToOrder(Lib, 'Code Complete: A Handbook of Software Construction')
#U.removeFromOrder('The Forever War')
#U.viewOrder()
#U.viewTotalCost()
