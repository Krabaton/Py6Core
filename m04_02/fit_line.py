def best_fit_line(data: list[tuple]) -> tuple:
    list_x = []
    list_y = []
    for coord in data:  # coord = (1.0, 2.0)
        list_x.append(coord[0])
        list_y.append(coord[1])

    m1 = 0.0
    n = len(data)
    for i in range(n):
        m1 = m1 + list_x[i] * list_y[i]

    m2 = (sum(list_x) * sum(list_y)) / n

    m3 = 0.0
    for i in range(n):
        m3 = m3 + list_x[i] ** 2

    m4 = (sum(list_x) * sum(list_x)) / n

    m = round((m1 - m2) / (m3 - m4), 2)
    b = round(sum(list_y) / n - m * sum(list_x) / n, 2)
    return m, b


def main():
    data = []
    x = input('Введите координату x (Enter для выхода): ')
    while x != '':
        y = input('Введите координату y: ')
        data.extend([(float(x), float(y))])
        x = input('Введите координату x (Enter для выхода): ')

    print(data)

    m, b = best_fit_line(data)
    print(f"y = {m}x + {b}")


if __name__ == '__main__':
    main()
