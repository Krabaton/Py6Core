## Сериализация объектов Python

Сериализация -- процесс перевода какой-либо структуры данных в последовательность битов. Обратной к операции
сериализации является операция десериализации (структуризации) -- восстановление начального состояния структуры данных
из битовой последовательности.

Сериализация используется для:

* обмена объектами через каналы связи;
* сохранения состояния объекта на устройстве хранения информации.

В Python есть [модуль](https://docs.python.org/3/library/marshal.html) дающий возможность сериализировать любой (ну
почти любой) Python объект.

Пакет Marshal является несколько низкоуровневым с ограниченным функционалом и его основная задача -- это работа с `.pyc`
файлами. Рекомендуется использовать [pickle](https://docs.python.org/3/library/pickle.html#module-pickle) для разовых
задач или [shelve](https://docs.python.org/3/library/shelve.html#module-shelve) если необходимо постоянно
сериализировать/десериализировать объекты по мере работы ПО.

[Basic Python IO Tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

### JSON

__JSON__ -- _JavaScript Object Notation_. Формат хранения данных в виде JavaScript объектов в строчном представлении.

В качестве значений в JSON могут быть использованы:

* Запись — это неупорядоченное множество пар ключ:значение, заключённое в фигурные скобки «{ }». Ключ описывается
  строкой, между ним и значением стоит символ «:». Пары ключ-значение отделяются друг от друга запятыми.

* Массив (одномерный) — это упорядоченное множество значений. Массив заключается в квадратные скобки `[]`. Значения
  разделяются запятыми. Массив может быть пустым, т.е. не содержать ни одного значения.

* Число (целое или вещественное).
* Литералы true (логическое значение «истина»), false (логическое значение «ложь») и null.
* Строка — это упорядоченное множество из нуля или более символов юникода, заключённое в двойные кавычки. Символы могут
  быть указаны с использованием escape-последовательностей, начинающихся с обратной косой черты «\» (поддерживаются
  варианты \', \", \\, \/, \t, \n, \r, \f и \b), или записаны шестнадцатеричным кодом в кодировке Unicode в виде \uFFFF.

### [CSV](https://docs.python.org/3/library/csv.html)

Наиболее распространенный формат хранения данных в табличном виде. По сути является просто текстовым файлом где
оговоренные символы имеют значение разделителей. В UNIX принято:

* `\n` -- разделитель строк
* `,` -- разделитель колонок

Не редко встречается `\t` (символ табуляции) в качестве разделителя колонок.

### YAML

YAML — зручний для читання людиною формат серіалізації даних, концептуально близький до мов розмітки, але орієнтований
на зручність введення-виведення типових структур даних багатьох мов програмування.

Назва YAML це рекурсивний акронім YAML Ain't Markup Language («YAML — не мова розмітки»). У назві відображена історія
розвитку: на ранніх етапах мова називалася Yet Another Markup Language («Ще одна мова розмітки») і навіть розглядалася
як конкурент XML, але пізніше була перейменована з метою акцентувати увагу на даних, а не на розбивці документів.
