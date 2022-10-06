try:
    from account_info import AccountInfo
except ImportError as e:
    import sys
    sys.path.append("../CSC510_PROJECT1/src")
    from account_info import AccountInfo


accInfo = AccountInfo()
print('Adding account...')
created_acc = accInfo.create_account('Ram', 'Bhusal', '12/23/1998', '"Eating pizza, Salsa, Ramen"', '"1, 2, 3, 5"', '"2, 3"')
_id = created_acc.ID.values[0]
created_row = created_acc[created_acc['ID']==_id]
assert(created_row.Name.values[0] == 'Ram')
assert(created_row.Surname.values[0] == 'Bhusal')
assert(created_row.Birthday.values[0] == '12/23/1998')
assert(created_row.FriendList.values[0] == '"2, 3"')

print('Reading account')
assert(accInfo.get_info(2).all()[0] == 1)

print('Reading non-existing account, error case')
assert(accInfo.get_info(200) == -1)

print('Deleting account')
assert(accInfo.delete_account(_id).all()[0] == 1)

print('Deleting an nonexisting account')
assert(accInfo.delete_account(300) == -1)
