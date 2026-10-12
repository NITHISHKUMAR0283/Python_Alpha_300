class Item():
    objects = []
    def __init__(self,name:str,quantity:int,price:float=1):

        assert quantity>=0 , f"quantity is lesser than 0 ,received {quantity}"
        assert price >=0 , f"prices is lesser than 0 , received {price}"

        self.name = name
        self.quantity = quantity
        self.price = price

        Item.objects.append(self)

    def calculate_net (self):
        self.payRate = 0.2
        
        # print(self.payRate) # belongs to objects
        # print(Item.payRate) # belongs to class

        return self.quantity*self.price
    def __repr__(self):
        return f"Item({self.name},{self.quantity},{self.price})"

    

Item.payRate= 0.9
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.objects)