class Info:
    def __init__(self, first_name, sur_name, birthday, interests):
        self.fname = first_name
        self.sname = sur_name
        self.birthday = birthday
        self.interests = interests

class WishLists:
    def __init__(self, item):
        self.item = item

class Friends:
    def __init__(self, account_id):
        self.account_id = account_id

    def add_friend(self, account_id):
        pass

    def delete_friend(self, account_id):
        pass
