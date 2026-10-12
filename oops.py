import csv
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
    @classmethod
    def Instatantiate_from_csv(cls):
        with open("item.csv",'r') as f:
            reader = csv.DictReader(f)
            items =list(reader)
        for item in items:
            Item(
                name = str(item.get("name")),
                quantity= int(item.get("quantity")),
                price = float(item.get("price"))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        if isinstance(num,int):
            return True
        return False

class Phone(Item):
    Objects  =[]
    
    def __init__(self,name:str,quantity:int,price:float=1,broken_phone =1 ):
        super().__init__(name,quantity,price)
        assert quantity>=0 , f"quantity is lesser than 0 ,received {quantity}"
        assert price >=0 , f"prices is lesser than 0 , received {price}"
        assert broken_phone>=0 , f"broken phone is lesser than 0 , received{broken_phone}"

        self.broken_phone=  broken_phone

        Phone.objects.append(self)

Item.payRate= 0.9
Item.Instatantiate_from_csv()
print(Item.objects)
print(Item.is_integer(8))
phone1 = Phone("lava",10,10.2,2)
print(phone1.calculate_net())
