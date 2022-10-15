di = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
      {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
      {'name': 'Princess', 'phone': '555-3141', 'email': ''},
      {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]

print('Phone number ends in an: ')
for i in di:
    if i['phone'][-1] == "8":
        print(i['name'])
print('Don’t have an email address: ')
for i in di:
    if i['email'] == '':
        print(i['name'])
