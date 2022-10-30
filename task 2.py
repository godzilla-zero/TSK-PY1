def get_count_char(str_):
    str_ = "".join(str_.lower().split())
    dict_ = {}
    for sym in str(str_):
        if sym.isalpha():
            if sym not in dict_:
                dict_[sym] = 1
            else:
                dict_[sym] += 1
                return dict_  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def percent(dict_):
    total_count = sum(dict_.values())
    for value in dict_.values():
        value = round(value / total_count * 100, 1)
        return dict_
    print(percent(check_dict))
