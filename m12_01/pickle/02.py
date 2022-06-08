import pickle

FILENAME = "users.dat"

users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]

with open('user.dat', 'wb') as f:
    pickle.dump(users, f)

with open('user.dat', 'rb') as f:
    users_form_file = pickle.load(f)
    print(users_form_file)
