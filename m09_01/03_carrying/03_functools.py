from functools import partial


def greeting_simple(msg, name):
    return f"{name} - {msg}"


msg_for_boris = partial(greeting_simple, name='Boris')

print(msg_for_boris('Go to home!'))
print(msg_for_boris('Go to work!'))
