from random import randint
from collections import UserDict


class Card(UserDict):
    # размер промежутка чисел для номеров в столбце буквы
    numbers_per_letter = 15
    # количество номеров в столбце
    limit_line = 5
    loto_fields = ["B", "I", "N", "G", "O"]

    def __init__(self) -> None:
        # Заставляем отработать конструктор UserDict, чтобы это был словарь
        super().__init__()
        # начинаем работать с 1
        self.start_num = 1
        # и выделяем промежуток в 15 чисел
        self.end_num = self.numbers_per_letter
        # создаем рандомную карточку
        self.create_card()

    def create_card(self) -> None:
        # Для каждой буквы создаем список рандомных номеров
        for letter in self.loto_fields:
            # Для текущей буквы создаем пустой список
            self.data[letter] = []
            # генерируем случайные номера, пока не наберется limit_line уникальных
            while len(self.data[letter]) < self.limit_line:
                next_num = randint(self.start_num, self.end_num)
                # Убеждаемся, что next_num не дубликат
                if next_num not in self.data[letter]:
                    self.data[letter].append(next_num)
            # Обновляем диапазон номеров для следующей буквы
            self.start_num = self.end_num + 1
            self.end_num = self.end_num + self.numbers_per_letter

    def set_num_to_zero(self, num: int):
        for k, line in self.data.items():
            self.data[k] = list(map(lambda x: 0 if x == num else x, line))
            # if num in line:
            #     for i in range(len(line)):
            #         if line[i] == num:
            #             line[i] = 0

    def pretty_info(self) -> None:
        print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*self.data))
        for i in range(self.limit_line):
            line = []
            for letter in self.loto_fields:
                line.append(self.data[letter][i])
            print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*line))
            line.clear()  # перестраховался

    # def __str__(self) -> str:
    #     view = ''
    #     view = view + '{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*self.data) + '\n'
    #     for i in range(self.limit_line):
    #         line = []
    #         for letter in self.loto_fields:
    #             line.append(self.data[letter][i])
    #         view = view + '{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*line) + '\n'
    #
    #     return view


if __name__ == '__main__':
    card = Card()
    print(card)
    card.pretty_info()
