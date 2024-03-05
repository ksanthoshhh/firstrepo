class Book:
    def __init__(self,title,author,pages,amount):
        self.title=title
        self.author=author
        self.pages=pages
        self.amount=amount
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.amount -(self.amount*self._discount)
        else:
            return self.amount
    def display(self):
        return self.title
    def discount(self,amount):
        self._discount=amount
b1=Book("new op","leo",1223,345.54)
b2=Book("one piece","naruto",1226,340.50)
print(b1.getprice())
b1.discount(0.23)
print(b1.getprice())
