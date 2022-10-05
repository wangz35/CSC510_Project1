from pandas import *
class ItemManager:
    def __init__ (self):
        self.database = 'data/item_data.csv'

    def add_item(self, title = 0, desc = 0, cost = 0, link = 0):
        data = read_csv(self.database)
        titles = data['Title'].tolist()
        lastElement = data['ItemID'].tolist()[-1]
        print(lastElement)



    def read_item(self, title = 0, desk = 0, cost = 0, link = 0):
        data = read_csv(self.database)
        titles = data['Title'].tolist()
        print(titles)


itemMan = ItemManager()
itemMan.add_item()