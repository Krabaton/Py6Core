import json


d = {"a": 1}
l = [1, 2.2]
t = (3, 4)
s = "I am string!"
b = True
st = {1, 2, 'Test'}
obj = {"tuple": t, "list": l, "dict": d, "string": s, "bool": b}
print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s))
print(json.dumps(b))
# print(json.dumps(st)) # Error TypeError: Object of type set is not JSON serializable

with open('storage.json', 'w') as f:
    json.dump(obj, f)
