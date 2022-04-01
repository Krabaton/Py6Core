baz = int(input("Enter a number: "))
foo = int(input("Enter a number: "))

# if baz < foo:
#     temp = baz
#     baz = (baz + foo) / 2
#     foo = temp * foo
# else:
#     temp = foo
#     foo = (foo + baz) / 2
#     baz = temp * baz

if baz < foo:
    baz, foo = (baz + foo) / 2, baz * foo
else:
    foo, baz = (foo + baz) / 2, foo * baz

print(baz, foo)
