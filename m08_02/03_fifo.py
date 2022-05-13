# FIFO (англ. first in, first out — «первым пришёл — первым ушёл») — способ организации данных или другими
# словами очередь. Это выражение описывает принцип технической обработки очереди или обслуживания конфликтных
#  требований путём упорядочения процесса по принципу: «первым пришёл — первым обслужен». Тот, кто приходит
#  первым, тот и обслуживается первым, пришедший следующим ждёт, пока обслуживание первого не будет закончено,
#  и так далее.


from collections import deque

MAX_LEN = 10

fifo = deque(maxlen=MAX_LEN)


def push(el):
    fifo.append(el)


def pop():
    return fifo.popleft()


push('Volodymyr')
push('Vitaliy')
push('Olexander')
push('Alexandr')
print(fifo)
name = pop()
print(name)
print(fifo)
