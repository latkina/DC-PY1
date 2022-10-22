def get_count_char(str_):
    str_ = str_.lower()
    dict_symbols = {}
    DEFAULT_COUNT = 0
    for symbol in str_:
        if symbol.isalpha():
            dict_symbols[symbol] = dict_symbols.get(symbol, DEFAULT_COUNT) + 1
    return dict_symbols


def percentage_content(dict_):
    sum_value = sum(dict_.values())
    PERCENT = 100
    for count in dict_:
        dict_[count] = round(dict_[count] * PERCENT / sum_value, 2)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percentage_content(get_count_char(main_str)))
