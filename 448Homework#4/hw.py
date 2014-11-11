class Book:
	def __init__(self, ID, title, genre, price):
		self.ID = ID
		self.title = title
		self.genre = genre
		self.price = price

class BookList:
	#all books in the list must have a unique ID
	def __init__(self):
		self.bookList = []
	def addBook(self, ID, title, genre, price):
		for index, item in enumerate(self.bookList):
			if item.ID == ID:
				return 'that ID is already in stock'
		for index, item in enumerate(self.bookList):
			if ID < item.ID:
				self.bookList.insert(index, Book(ID, title, genre, price))
				return
		self.bookList.append(Book(ID, title, genre, price))
	def addBook2(self, Book):
		self.addBook(Book.ID, Book.title, Book.genre, Book.price)
	def removeBook(self, ID):
		if len(self.bookList) == 0:
			print('no books in list')
			return False
		for index, item in enumerate(self.bookList):
			if item.ID == ID:
				self.bookList.pop(index)
				return True
		print('book ID not in list')
		return False
	def getTotalCost(self):
		totalCost = 0
		if len(self.bookList) == 0:
			return 0
		for index, item in enumerate(self.bookList):
			totalCost = totalCost + item.price 
		return totalCost
	def displayList(self):
		for item in self.bookList:
			print('ID: ' + str(item.ID))
			print('Title: ' + str(item.title))
			print('Genre: ' + str(item.genre))
			print('Price: ' + str(item.price))
			print('--------')

class Library:
	def __init__(self):
		self.List = BookList()
	def addBook(self, ID, title, genre, price):
		self.List.addBook(ID, title, genre, price)
	def removeBook(self, ID):
		self.List.removeBook(ID)
	def showList(self):
		self.List.displayList()
	def viewByGenre(self, genre):
		self.tempList = BookList()
		for item in self.List.bookList:
			if item.genre == genre:
				self.tempList.addBook2(item)
		print('Viewing all ' + genre + ' books.')
		self.tempList.displayList()
	def getBookByID(self, ID):
		for item in self.List.bookList:
			if item.ID == ID:
				return item
		print('That book ID is not available')
		return False

class Order:
	def __init__(self):
		self.List = BookList()
	def addBook(self, Library, ID):
		self.book = Library.getBookByID(ID)
		if self.book == False:
			print('failed to add book')
			return
		self.List.addBook2(self.book)
	def removeBook(self, ID):
		self.List.removeBook(ID)
	def viewList(self):
		print('Viewing current order')
		self.List.displayList()
	def getTotalCost(self):
		return self.List.getTotalCost()

class User:
	#a user can only have one order
	def __init__(self):
		self.Order = Order()
	def viewAll(self, Library):
		Library.showList()
	def viewGenre(self, Library, genre):
		Library.viewByGenre(genre)
	def addToOrder(self, Library, ID):
		self.Order.addBook(Library, ID)
	def removeFromOrder(self, ID):
		self.Order.removeBook(ID)
	def viewOrder(self):
		self.Order.viewList()
	def viewTotalCost(self):
		print('$' + str(self.Order.getTotalCost()))

Lib = Library()
Lib.addBook(1, 'a', 'Sci Fi', 2)
Lib.addBook(2, 'b', 'Sci Fi', 2)
Lib.addBook(3, 'c', 'Sci Fi', 2)
Lib.addBook(4, 'd', 'Horror', 4)
Lib.addBook(5, 'e', 'Horror', 4)
Lib.addBook(6, 'f', 'Horror', 4)
Lib.addBook(7, 'g', 'Fantasy', 6)
Lib.addBook(8, 'h', 'Fantasy', 6)
Lib.addBook(9, 'i', 'Fantasy', 6)
Lib.addBook(10, 'j', 'Non-fiction', 8)
Lib.addBook(11, 'k', 'Non-fiction', 8)
Lib.addBook(12, 'l', 'Non-fiction', 8)
P = User()
P.viewAll(Lib)
P.viewGenre(Lib, 'Horror')
P.viewGenre(Lib, 'Non-fiction')
P.addToOrder(Lib, 2)
P.addToOrder(Lib, 3)
P.addToOrder(Lib, 4)
P.addToOrder(Lib, 5)
P.addToOrder(Lib, 8)
P.addToOrder(Lib, 12)
P.removeFromOrder(3)
P.viewOrder()
P.viewTotalCost()











