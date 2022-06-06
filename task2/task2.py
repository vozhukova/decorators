import time
import os

def with_logfile(file_path):

    def with_log(old_function):

        def new_function(*args):
            result = old_function(*args)
            text = f'''{time.strftime("%d.%m.%Y г. %H:%M:%S", time.localtime())}
            Вызвана функция {old_function.__name__} с аргументами {args}
            Получен результат {result}\n'''
            with open(file_path, 'a', encoding='utf-8') as f:
                    f.write(text)
            return result

        return new_function

    return with_log

file_name = 'log.txt'

@with_logfile(os.path.abspath(file_name))
def sum(*args):
    sum_numbers = 0
    for arg in args:
        sum_numbers += arg
    return sum_numbers

sum(10, 10, 10)