person = {
    "name": "Oleg",
    "age": 23,
    "phone": "38(050)9993322",
    "married": False
}

person.update({"address": "Ukraine, Kyiv", "lang": "ukr"})
person.pop("lang")
oleg = person.copy()
person.clear()
oleg["address"] = "Poltava"
print(oleg)
print(person)
print(oleg.get("name", "anonim"))
print(oleg.get("age", None))
print(oleg.get("lang", "Python"))
