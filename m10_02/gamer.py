from card import Card


class Gamer:
    def __init__(self, name: str, card: Card):
        self.card = card
        self.name = name
        self.winner = False

    # Метод проверки выигрышная ли карточка игрока на данном этапе игры
    def check_winner(self):
        # проверить вертикальные линии карточки
        for col in self.card.values():
            if sum(col) == 0:
                self.winner = True

        # проверить горизонтальные линии карточки
        for i in range(self.card.limit_line):
            row = []
            for key in self.card.keys():
                row.append(self.card[key][i])
            if sum(row) == 0:
                self.winner = True

    # Отмечаем выпавший номер (и обнуляем его в карточке)
    def mark_number(self, num: int):
        self.card.set_num_to_zero(num)

        # for line in self.card.values():
        #     if num in line:
        #         for i in range(len(line)):
        #             if line[i] == num:
        #                 line[i] = 0
