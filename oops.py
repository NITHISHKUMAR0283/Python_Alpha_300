class Item():
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
        print("Created")


    def calculate_sum (self,a,b):
        return a+b

obj1 =Item("Pencil",5)
sum = obj1.calculate_sum(4,5)
print(sum)
print(obj1.name)

obj2 = Item("Pen",5)
print(obj2.name)