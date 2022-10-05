from pandas import *
class ItemManager:
    def __init__ (self):
        self.database = 'data/item_data.csv'

    def add_item(self, title, desc = '', cost = '', link = ''):
        data = read_csv(self.database)
        lastElement = data['ItemID'].tolist()[-1]+1
        new_data = {'ItemID': lastElement, 'Title': title, 'Description': desc,'Link': link, 'Cost': cost}
        df = DataFrame(new_data)
        df.to_csv(self.database, mode='a', index=False, header=False)
        print("Data appended successfully.")


    def read_item(self, ID: int):
        data = read_csv(self.database)
        print(data.loc[data['ItemID'] == ID])


itemMan = ItemManager()
#itemMan.add_item('Toaster', '4 slice, with bagel setting', '35', 'amazon')
itemMan.read_item(2)
