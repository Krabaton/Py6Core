# Работа с датой и временем (datetime)

Класс `datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)` - комбинация даты и времени.

Обязательные аргументы:

`datetime.MINYEAR (1) ≤ year ≤ datetime.MAXYEAR (9999)`

1 ≤ month ≤ 12

1 ≤ day ≤ количество дней в данном месяце и году

Необязательные:

0 ≤ minute < 60 0 ≤ second < 60 0 ≤ microsecond < 1000000

## Методы класса `datetime`:

`datetime.today()` - объект datetime из текущей даты и времени. Работает также, как и datetime.now() со значением tz=None.

`datetime.fromtimestamp(timestamp)` - дата из стандартного представления времени.

`datetime.fromordinal(ordinal)` - дата из числа, представляющего собой количество дней, прошедших с 01.01.1970.

`datetime.now(tz=None)` - объект datetime из текущей даты и времени.

`datetime.combine(date, time)` - объект datetime из комбинации объектов date и time.

`datetime.strptime(date_string, format)` - преобразует строку в datetime (так же, как и функция strptime из модуля time).

`datetime.strftime(format)` - см. функцию strftime из модуля time.

`datetime.date()` - объект даты (с отсечением времени).

`datetime.time()` - объект времени (с отсечением даты).

`datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])` - возвращает новый объект datetime с изменёнными атрибутами.

`datetime.timetuple()` - возвращает struct_time из datetime.

`datetime.toordinal()` - количество дней, прошедших с 01.01.1970.

`datetime.timestamp()` - возвращает время в секундах с начала эпохи.

`datetime.weekday()` - день недели в виде числа, понедельник - 0, воскресенье - 6.

`datetime.isoweekday()` - день недели в виде числа, понедельник - 1, воскресенье - 7.

`datetime.isocalendar()` - кортеж (год в формате ISO, ISO номер недели, ISO день недели).

`datetime.isoformat(sep='T')` - красивая строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm" или, если microsecond == 0, "YYYY-MM-DDTHH:MM:SS"

`datetime.ctime([сек])` - преобразует время, выраженное в секундах с начала эпохи в строку вида "Thu Sep 27 16:42:37 2012".
