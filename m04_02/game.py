"""
- s (Spades) Пики
- h (Hearts) Чирвы
- d (Diamonds) Бубны
- c (Clovers) Трефы
"""
from random import randrange


def create_deck() -> list:
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value}{suit}')
    return deck


def shuffle_deck(deck: list) -> list:
    new_deck = deck.copy()
    for i in range(0, len(new_deck)):
        random_index = randrange(0, len(new_deck))
        new_deck[i], new_deck[random_index] = new_deck[random_index], new_deck[i]
    return new_deck


def deal(players: int, numbers_cards_of_player: int, deck: list) -> list[list]:
    if players * numbers_cards_of_player > len(deck):
        print(f"Игра не возможно не хватает карт в колоде")
        return None

    table = []  # [['ss', 'ss'], ['as', 'as']]
    print(table)
    for _ in range(0, numbers_cards_of_player):
        for player in range(0, players):
            if player >= len(table):
                # Игрок впервые добавляется в раздачу
                table.append([deck.pop()])
            else:
                table[player].append(deck.pop())
    return table


def main():
    init_deck = create_deck()
    print(f'Открываем новую колоду: {init_deck}')
    deck = shuffle_deck(init_deck)
    print(f'Тасуем колоду: {deck}')
    players = 7
    numbers_cards_of_player = 5
    table_deal = deal(players, numbers_cards_of_player, deck)
    for i in range(players):
        print(f"Карты игрока {i + 1} : {table_deal[i]}")

    print(f"Колода после раздачи: {deck}")


if __name__ == '__main__':
    main()
