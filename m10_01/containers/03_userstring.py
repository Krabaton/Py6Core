from collections import UserString

template = [
    "Вы можете достичь всего. Стоит только немного постараться и запастись книгами.",
    "Этот смартфон — настоящая находка. Большой и яркий экран, мощнейший процессор — всё это в небольшом гаджете.",
    "Собрать камни бесконечности легко, если вы прирожденный герой.",
    "Освоить вёрстку несложно. Возьмите книгу новую книгу и закрепите все упражнения на практике.",
    "Бороться с прокрастинацией несложно. Просто действуйте. Маленькими шагами.",
    "Программировать не настолько сложно, как об этом говорят.",
    "Простые ежедневные упражнения помогут достичь успеха."
]

for i, comment in enumerate(template):
    print("|{:^5}|{:<15}|".format(i, comment))


class Comments(UserString):
    def get_limit_comment(self, limit=10):
        return f"{self.data[:limit - 3]}..."


comments = [Comments(comment) for comment in template]

for i, comment in enumerate(comments):
    print("|{:^5}|{:<15}|".format(i + 1, comment.get_limit_comment(35)))
