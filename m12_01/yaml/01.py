import yaml

users = [
    {'name': 'Николай', 'age': 22, 'gender': 'male'},
    {'name': 'Мария', 'age': 22, 'gender': 'female'},
    {'name': 'Назар', 'age': 22, 'gender': 'male'},
]

serialize = yaml.dump(users)
result = yaml.load(serialize, Loader=yaml.FullLoader)

with open('test.yaml', 'w', encoding='utf-8') as f:
    yaml.dump({'users': users}, f, allow_unicode=True)

with open('test.yaml', 'r', encoding='utf-8') as f:
    copy_users = yaml.load(f, Loader=yaml.FullLoader)

print(copy_users)
