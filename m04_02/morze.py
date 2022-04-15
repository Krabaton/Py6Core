morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}


def convert_word_to_morze(text: str) -> str:
    result = ''
    text = text.upper()
    for ch in text:
        # if ch in morze_dict:
        result = result + morze_dict.get(ch, '')
        # result = result + morze_dict.setdefault(ch, '')
    return result


def main():
    text = input('Введите строку (Enter для выхода): ')
    while text != '':
        print(f"На азбуке морзе это будет: {convert_word_to_morze(text)}")
        print(morze_dict)
        text = input('Введите строку (Enter для выхода): ')


if __name__ == '__main__':
    main()
