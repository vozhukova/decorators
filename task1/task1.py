import time

def with_logfile(old_function):

    def new_function(a, b):
        result = old_function(a, b)
        text = f'''{time.strftime("%d.%m.%Y г. %H:%M:%S", time.localtime())} 
        Вызвана функция {old_function.__name__} с аргументами {a} и {b}
        Получен результат {result}\n'''
        with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(text)
        return result

    return new_function

@with_logfile
def sum(a, b):
    return a + b

sum(10, 12)