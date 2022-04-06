from unittest import result


def greetins(**kwargs):
    print(kwargs)
    name = kwargs.get("name", "Незнакомец")
    age = kwargs.get("age", None)
    return f"Hello {name} - {age} age"


result = greetins()
print(result)

result = greetins(name="Mixail", age=34, baz=12, bar="foo")
print(result)
