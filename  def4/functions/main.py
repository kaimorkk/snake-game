class laptop:
    def __init__(self,brand, model,price):
        self.brand=brand
        self.model=model
        self.price=price
laptop=laptop('acer','predator','s490')
print(laptop.__dict__)