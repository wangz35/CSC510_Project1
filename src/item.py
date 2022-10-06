from item_manager import ItemManager
class item():
    def __init__(self, title, desc, link, cost):
        self.title = title
        self.desc = desc
        self.link = link
        self.cost = cost
        self.itemID = int(self.create_item()['ItemID'])

    
    def create_item(self):
        itemMan = ItemManager()
        item = itemMan.add_item(self.title, self.desc, self.link, self.cost)
        return item

    def modify_item(self, title, desc, link, cost):
        itemMan = ItemManager()
        self.title = title
        self.desc = desc
        self.link = link
        self.cost = cost
        itemMan.update_item( self.itemID, title, desc, link, cost)
    
    def view_item(self):
        itemMan = ItemManager()
        return itemMan.get_item(self.itemID)

    def delete_item(self):
        itemMan = ItemManager()
        itemMan.delete_item(self.itemID)



i = item('Football', 'NFL original', 'www.football.com', 50)
print(i.cost)
i.modify_item('Football', 'NFL original', 'www.football.com', 65)
print(i.view_item())
i.delete_item()