"""
Counter
Например есть набор температур за первые 15 дней января. Найти количество общих температур, наиболее частую
"""

import collections

temperatures = [0.5, 0.0, -3.5, 0.0, 2.5, 3.5, 4.0, 0.5, 3.5, 5.5, 6.0, 10.0, 12.5]

t_count = collections.Counter(temperatures)
print(t_count)
print(t_count.most_common(1))
print(t_count.most_common())
