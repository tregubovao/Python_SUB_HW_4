# Напишите функцию принимающую на вход только ключевые параметры(kwargs) 
# и возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

import os
os.system('cls')

def reverse_kwargs_func(**kwargs):
    reverse_dict = dict()       
    for key, value in kwargs.items():
        try:
            hash(value)  
            reverse_dict[value] = key
        except:
            reverse_dict[str(value)] = key
    return reverse_dict

print(reverse_kwargs_func(rev=True, acc="YES", stroka=4, my_set = {3, 4, 2, 9}, 
                            float_num=3.1415926, my_list=[5, 15, 25]))
