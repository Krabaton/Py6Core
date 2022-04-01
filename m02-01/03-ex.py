a = int(input("Enter a number: "))

if not a % 2 and not a % 3:
    print("a кратно 2 и 3")

if not a % 2 and not a % 5:
    print("a кратно 2 и 5")

if a <= 10 or a >= 50:
    print("a не принадлежит промежутку (10, 50)")  # [10, 50)

if a > 10 and a < 50:
    print("a принадлежит промежутку (10, 50)")
