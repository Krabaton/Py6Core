import sys
import pow

if __name__ == "__main__":
    try:
        _, base, exp, *rest = sys.argv
        print(pow.my_pow(int(base), int(exp)))
    except ValueError:
        print('Введите два параметра')
