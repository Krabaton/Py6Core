# List: Например для температур надо учесть ошибку и повысить каждую температуру на 0.5 градуса

temps = [0.5, 0.0, -3.5, 0.0, 2.0, 3.5, 0.5,
         -4.0, -3.5, -0.5, -3.5, -10.5, -14.0, -1.0, -1.0]

fix_t = [t + 0.5 for t in temps]
print(fix_t)

# Set: для того же списка температур найдем уникальные значения

unique_t = {t + 0.5 for t in temps}
print(unique_t)

# Dict: создадим словарь соответствия старой и исправленной температуры

tr_t = {t: t + 0.5 for t in temps}
print(tr_t)
