"""
Методы: strip, removeprefix, replace, format
------
Провести валидацию списка телефонов
Телефон: +380501234567 Где: +380 код страны телефон 501234567
Считаем, что код валиден с кодом и без кода
"""
phone_storage = ["380669640547", "0637306465 ", " 380961935171", "632643973", "050832520 ",
                 "000000000", "48730283918", "986223575", "375297947963", "+38(050)123-32-34", "38(050)123 32 34",
                 "38(050)123 32 3b"]

codes_operators = {"067", "068", "096", "097", "098",
                   "050", "066", "095", "099", "063", "073", "093"}


def isvalid_phone(phone):
    def is_valid_operator(phone):
        if phone[:3] in codes_operators:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == '38':
                return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


def sanitize_phone(phone):
    new_phone = (phone.strip()
                 .removeprefix('+')
                 .replace("(", '')
                 .replace(")", '')
                 .replace(" ", '')
                 .replace("-", ''))

    return new_phone


if __name__ == '__main__':
    for phone in phone_storage:
        phone = sanitize_phone(phone)
        is_valid = isvalid_phone(phone)
        if is_valid:
            print("Телефон {:>12} валиден".format(phone))
        else:
            print("Телефон {:>12} невалиден".format(phone))
