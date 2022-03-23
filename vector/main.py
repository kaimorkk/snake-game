class Laptop:
     def __init__(self,brand,model,price):
         self.brand=brand
         self.model=model
         self.price=price
     def display_attr_with_values(self):
         for attr in self.__dict__.keys():
             print(attr)
laptop=Laptop('Dell','Inspiron',3699)
print(laptop.display_attr_with_values())