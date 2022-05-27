from random import randint

from card import Card
from gamer import Gamer
from typing import List, Tuple


class LotoGame:
    def __init__(self, gamers: List[Gamer]):
        # набор игроков для игры
        self.gamers = gamers
        # минимальный номер первого шара (бочонка)
        self.min_number = 1
        # максимальный номер последнего шара (бочонка) 75
        self.max_number = Card.numbers_per_letter * Card.limit_line
        # список победителей
        self.winners: List[Gamer] = []  # условие конца игры это список стал длиной больше 0
        # список выпавших номеров
        self.draw_numbers: List[int] = []
        # шаг (прогресс) игры
        self.progress = 0

    def start(self) -> Tuple[int, List[Gamer]]:
        while True:
            # шаг игры
            self.step_game()
            # проверить победителей
            self.check_winners()
            # условие конца игры это список стал длиной больше 0
            if len(self.winners) > 0:
                break

        return self.progress, self.winners

    def step_game(self):
        while True:
            # берем случайное число от min до max
            current_num = randint(self.min_number, self.max_number)
            # проверяем, что номер еще не выпадал, иначе повторяем, чтобы был новый
            if current_num not in self.draw_numbers:
                # запоминаем выпавший номер
                self.draw_numbers.append(current_num)
                break

        for gamer in self.gamers:
            # игроки проверяют карточки
            gamer.mark_number(current_num)
            # проверим не выиграла ли карточка
            gamer.check_winner()

        # увеличиваем шаг игры
        self.progress += 1

    def check_winners(self):
        for gamer in self.gamers:
            if gamer.winner:
                self.winners.append(gamer)


if __name__ == '__main__':
    players_name = ['Oleksandr', 'Volodymyr', 'Roman', 'Andrij', 'Boris', 'Iryna', 'Serjoga', 'Nissa', 'Krabat', 'Oleg',
                    'Oleksandra']

    gamers = []
    for name in players_name:
        card = Card()
        gamer = Gamer(name, card)
        gamers.append(gamer)

    game = LotoGame(gamers)
    quantity, winners = game.start()
    print(f"Количество шагов {quantity}")
    print(f"Выпавшие номера {game.draw_numbers}")
    for winner in winners:
        print(f"Победитель {winner.name}")
        winner.card.pretty_info()