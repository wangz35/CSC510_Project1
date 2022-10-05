from pandas import *
class ItemManager:
    def __init__ (self):
        self.database = 'data/item_data.csv'

    def add_item(self, title, desc = '', cost = '', link = ''):
        data = read_csv(self.database)
        lastElement = data['ItemID'].tolist()[-1]+1
        new_data = {'ItemID': lastElement, 'Title': title, 'Description': desc,'Link': link, 'Cost': [cost]}
        df = DataFrame(new_data)
        df.to_csv(self.database, mode='a', index=False, header=False)
        print("Data appended successfully.")


    def get_item(self, ID: int):
        data = read_csv(self.database)
        return (data.loc[data['ItemID'] == ID])

    def delete_item(self, ID: int):
        data = read_csv(self.database)
        print(list(data.index[data['ItemID'] == ID]))
        data.drop(data.index[data['ItemID'] == ID], axis = 0, inplace= True)
        data.to_csv(self.database, mode='w', index=False, header=False)
        print("Item deleted.")


itemMan = ItemManager()
#itemMan.add_item('Toaster', '4 slice, with bagel setting', '35', 'www.amazon.com')
print(itemMan.get_item(17))
itemMan.delete_item(17)
