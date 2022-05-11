"""
Класс datetime.timedelta - разница между двумя моментами времени, с точностью до микросекунд.
Рассмотрим следующую задачу. Например, врач прописала пациенту принимать лекарство в течение 45 дней.
Надо найти дату окончания приема лекарства от текущей даты.
"""

from datetime import datetime, timedelta

d = datetime.now()
interval = timedelta(days=45)
finish_d = d + interval
print(finish_d)

