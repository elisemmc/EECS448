class Customer:
	def __init__(self, customerName, customerID, paymentMethod):
		#customers must be named the same as their instance
		self.customerName = customerName
		self.customerID = customerID
		self.paymentMethod = paymentMethod

	def selectOrder(self, Retailer, goodsID, goodsName, quantity, price):
		#All orders can only order one goodID at a time.
		#Orders must contain an existing item.  As inputs are not filtered or checked.
		#Order items must exist with all parameters correct, and have unique goodID 
		print('**Customer is Selecting Order\n')
		Retailer.getOrder( self, goodsID, goodsName, quantity, price)

	def makePayment(self, amount):
		#Customers pay in exact change
		print('Customer has made payment\n')
		return amount

	def contactRetailer(self, Retailer):
		#This doesn't seem to be used, and there is no retailer class that contains this based
		#on the uml diagram
		print('hello to you too')

	def viewGoods(self, Retailer):
		print('Customer is viewing goods\n')
		print(Retailer.giveList())

class GoodsItem:
	def __init__(self, goodsID, goodsName, quantity, price):
		self.goodsID = goodsID
		self.goodsName = goodsName
		self.quantity = quantity
		self.price = price

class Goods:
	def __init__(self):
		self.goodsList = []
	def addGood(self, goodsID, goodsName, quantity, price):
		for index, item in enumerate(self.goodsList):
			if item.goodsID == goodsID:
				item.quantity = item.quantity + quantity
				return
		for index, item in enumerate(self.goodsList):
			if price < item.price:
				self.goodsList.insert(index, GoodsItem(goodsID, goodsName, quantity, price))
				return
		self.goodsList.append(GoodsItem(goodsID, goodsName, quantity, price))
	def removeGood(self, CheckGoodsID, CheckQuantity):
		if len(self.goodsList) == 0:
			return 0
		for index, item in enumerate(self.goodsList):
			if item.goodsID == CheckGoodsID:
				if item.quantity > CheckQuantity:
					item.quantity = item.quantity - CheckQuantity
					return 1
				elif item.quantity == CheckQuantity:
					self.goodsList.pop(index)
					return 1
				else:
					return 0
		return 0
	def checkGood(self, CheckGoodsID, CheckQuantity):
		if len(self.goodsList) == 0:
			return 0
		for index, item in enumerate(self.goodsList):
			if item.goodsID == CheckGoodsID:
				if item.quantity >= CheckQuantity:
					return 1
				else:
					return 0
		return 0
	def displayList(self):
		for item in self.goodsList:
			print('ID: ' + str(item.goodsID))
			print('Name: ' + str(item.goodsName))
			print('Quantity: ' + str(item.quantity))
			print('Price per Unit: ' + str(item.price))
			print('--------')

class Supplier:
#The supplier never runs out of anything.  This is achieved by the supplier magically acquiring more stuff whenever goods are low.

	def __init__(self, supplierID):
		self.GoodsList = Goods()
		self.supplierID = supplierID

	def addGood(self, goodsID, goodsName, quantity, price):
		self.GoodsList.addGood(goodsID, goodsName, quantity, price)

	def removeGood(self, goodsID, goodsName, quantity, price):
		temp = self.GoodsList.removeGood(goodsID, quantity)
		if temp == 0:
			self.GoodsList.addGood(goodsID, goodsName, 1000, price)

	def updateGood(self, addRemove, goodsID, goodsName, quantity, price):
		if addRemove == 'add':
			self.addGood(goodsID, goodsName, quantity, price)
		else:
			self.removeGood(goodsID, quantity)

	def acceptPayment(self, TTLprice):
		print('Retailer has paid supplier\n')

class Retailer:

	GoodsList = Goods()

	def __init__(self, retailerName):
		self.retailerName = retailerName

	def getOrder(self, Customer, goodsID, goodsName, quantity, price):
		#Everybody orders from Frank
		if not self.checkSupply(goodsID, quantity):
			print('Retailer has determined it necessary to order more supplies\n')
			self.orderGoods(Frank, goodsID, goodsName, quantity+100, price)
		self.acceptOrder(Customer, goodsID, goodsName, quantity, price)

	def checkSupply(self, goodsID, quantity):
		print('Retailer is Checking Supply\n')
		if self.GoodsList.checkGood(goodsID, quantity) == 1:
			return True
		else:
			return False

	def acceptOrder(self, Customer, goodsID, goodsName, quantity, price):
		print('Retailer Accepts Order\n')
		Customer.makePayment(quantity*price)
		self.acceptPayment(goodsID, goodsName, quantity, price)

	def acceptPayment(self, goodsID, goodsName, quantity, price):
		print('Retailer Accepts Payment\n')
		self.updateGoods('remove', goodsID, goodsName, quantity, price)

	def orderGoods(self, SupplierName, goodsID, goodsName, quantity, price):
		SupplierName.removeGood(goodsID, goodsName, quantity, price)
		self.GoodsList.addGood(goodsID, goodsName, quantity, price)
		SupplierName.acceptPayment(price*quantity)

	def updateGoods(self, addRemove, goodsID, goodsName, quantity, price):
		print('Retailer is now updating goods\n')
		if addRemove == 'add':
			self.GoodsList.addGood(goodsID, goodsName, quantity, price)
		else:
			self.GoodsList.removeGood(goodsID, quantity)

	def giveList(self):
		print('Displaying Retailer List of Goods\n************')
		self.GoodsList.displayList()
		return ' '

Frank = Supplier('Frank')

Bob = Retailer('Bob')
Bob.orderGoods(Frank, 1, 'a', 100, 6)
Bob.orderGoods(Frank, 2, 'b', 100, 3)
Bob.orderGoods(Frank, 3, 'c', 100, 7)
Bob.orderGoods(Frank, 4, 'd', 100, 4)
Bob.orderGoods(Frank, 5, 'e', 100, 7)
Bob.orderGoods(Frank, 6, 'f', 100, 9)

Harry = Customer('Harry', 2, 'Money')
Harry.viewGoods(Bob)
Harry.selectOrder(Bob, 1, 'a', 4, 6)
Harry.selectOrder(Bob, 1, 'a', 105, 6)
Harry.viewGoods(Bob)






