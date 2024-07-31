username = ["Dude", "Bro", "Mister"]
password = ("p@$$word", "abc123", "guest@123")
login_date = ['2024-07-25', '2024-07-21', '2024-07-19']

users = zip(username, password, login_date)

print('Type of Users:', type(users))

for user in users:
    print(user)

# for user, pwd in dict(users).items():
#     print(f'{user} has {pwd}')