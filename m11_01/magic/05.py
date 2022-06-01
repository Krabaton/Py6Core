# Функтор

class Count:
    def __init__(self, init_steps):
        self.steps = init_steps

    def __call__(self, *args, **kwargs):
        inc, = args  # inc = args[0]
        self.steps += inc


count_step = Count(100)
count_step(25)
count_step(50)
print(count_step.steps)
