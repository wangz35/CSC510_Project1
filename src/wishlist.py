import pandas as pd

class wishlist():
    def __init__(self):
        print ("hello")
        df = pd.read_csv(r'C:\\Users\\piyuj\\OneDrive\\Desktop\\Sem 1\\SE\\PROJ 1\\CSC510_Project1\\src\\item_data.csv')
        print(df['Title'])

    def view_all(self):
        print("============================================================")
        df = pd.read_csv(r'C:\\Users\\piyuj\\OneDrive\\Desktop\\Sem 1\\SE\\PROJ 1\\CSC510_Project1\\src\\item_data.csv')
        print(df['Title'])

    def option(self):
        print("============================================================")
        print ("Enter index number to do follwing function")
        print ("0 to View all item; 1 to view specific item; 2 to create item; 3 to delete item")
        input_decision = int(input())

        if input_decision == 0:
            self.view_all()
            self.option()

        elif input_decision == 1:
            self.view()

        elif input_decision == 2:
            print("ADDING ITEM")
            self.option()

        elif input_decision == 3:
            print("DELETING ITEM")
            self.option()

        else:
            print("INVALID INPUT")
            self.option()

    def view(self):

        df = pd.read_csv(r'C:\\Users\\piyuj\\OneDrive\\Desktop\\Sem 1\\SE\\PROJ 1\\CSC510_Project1\\src\\item_data.csv')
        print("Enter index number of item you want to view")
        input_choice = int(input())
        if input_choice < len(df):
            print("Item:  "+ str(df['ItemID'][input_choice]))
            print("Title:  " + str(df['Title'][input_choice]))
            print("Description:  " + str(df['Description'][input_choice]))
            print("Link:  " + str(df['Link'][input_choice]))
            print("Cost:  " + str(df['Cost'][input_choice]))
            self.option()
        else:
            print ("=====================================")
            print("INVALID INPUT")
            self.view()

obj = wishlist()
obj.option()
