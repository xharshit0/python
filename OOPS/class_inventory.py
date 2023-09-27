class Inventory:
    def __init__(self):
        self.inventory = {}
    def add_item(self,item_id,item_name,stock_count,price):
        self.inventory[item_id]={"item_name":item_name,"stock_count":stock_count,"price":price}
    def update_item(self,item_id,stock_count,price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"]="stock_count"
            self.inventory[item_id]["price"]="price"
        else:
            print("item is not found in inventory")
    def check_item_details(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}, Price: {item['price']}"
        else:
            return "Item not found in inventory."
inventory = Inventory()

inventory.add_item("1001","Iphone",100,500.00)
inventory.add_item("1002","Realme",150,200.00)
inventory.add_item("1003","Samsung",115,300.00)
inventory.add_item("1004","Micromax",89,200.00)
print("Item Detail:")
print(inventory.check_item_details("1001"))
print(inventory.check_item_details("1002"))
print(inventory.check_item_details("1003"))
print(inventory.check_item_details("1004"))
print("\nUpdate the price of item code - 'I001':")
inventory.update_item("1001", 100, 505.00)
print(inventory.check_item_details("I001"))
print("\nUpdate the stock of item code - 'I003':")
inventory.update_item("I003", 115, 500.00)








