class Book:
	def __init__(self, goodsID, goodsName, quantity, price):
		self.goodsID = goodsID
		self.goodsName = goodsName
		self.quantity = quantity
		self.price = price

class BookList:
	def __init__(self):
		self.bookList = []
	def addGood(self, goodsID, goodsName, quantity, price):
		for index, item in enumerate(self.bookList):
			if item.goodsID == goodsID:
				item.quantity = item.quantity + quantity
				return
		for index, item in enumerate(self.bookList):
			if price < item.price:
				self.bookList.insert(index, Book(goodsID, goodsName, quantity, price))
				return
		self.bookList.append Book(goodsID, goodsName, quantity, price))
	def removeGood(self, CheckGoodsID, CheckQuantity):
		if len(self.bookList) == 0:
			return 0
		for index, item in enumerate(self.bookList):
			if item.goodsID == CheckGoodsID:
				if item.quantity > CheckQuantity:
					item.quantity = item.quantity - CheckQuantity
					return 1
				elif item.quantity == CheckQuantity:
					self.bookList.pop(index)
					return 1
				else:
					return 0
		return 0
	def checkGood(self, CheckGoodsID, CheckQuantity):
		if len(self.bookList) == 0:
			return 0
		for index, item in enumerate(self.bookList):
			if item.goodsID == CheckGoodsID:
				if item.quantity >= CheckQuantity:
					return 1
				else:
					return 0
		return 0
	def displayList(self):
		for item in self.bookList:
			print('ID: ' + str(item.goodsID))
			print('Name: ' + str(item.goodsName))
			print('Quantity: ' + str(item.quantity))
			print('Price per Unit: ' + str(item.price))
			print('--------')