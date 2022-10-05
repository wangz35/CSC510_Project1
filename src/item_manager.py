from pandas import *
class ItemManager:
    def __init__ (self):
        self.database = 'data/item_data - Copy.csv'

    def add_item(self, title, desc = '', cost = '', link = ''):
        data = read_csv(self.database)
        lastElement = data['ItemID'].tolist()[-1]+1
        new_data = {'ItemID': lastElement, 'Title': title, 'Description': desc,'Link': link, 'Cost': [cost]}
        df = DataFrame(new_data)
        df.to_csv(self.database, mode='a', index=False, header=False)
        print("Data appended successfully.")


    def get_item(self, ID: int):
        data = read_csv(self.database)
        if data.loc[data['ItemID']==ID].empty:
            print("Item does not exist1")
            return -1
        return (data.loc[data['ItemID'] == ID])

    def delete_item(self, ID: int):
        data = read_csv(self.database)
        if data.index[data['ItemID'] == ID].empty:
            print("Item does not exist2")
            return -1
        data = data.drop(data.index[data['ItemID'] == ID], axis = 0)
        data.to_csv(self.database, mode='w', index=False)
        print("Item deleted.")
        return 0


itemMan = ItemManager()
#itemMan.add_item('Toaster', '4 slice, with bagel setting', '35', 'www.amazon.com')
itemMan.get_item(100)
itemMan.delete_item(100)
