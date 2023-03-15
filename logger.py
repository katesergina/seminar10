from datetime import datetime as dt
from guid import dict_log


def get_log(res, oper):
    dtime = dt.now()
    with open('log.txt', 'a') as file:
        file.write('{}; операция: {}; результат: {}\n'
                     .format(dtime, oper, res))