dictionary_en_to_ru = \
    {
        'q':'й',
        'w':'ц',
        'e':'у',
        'r':'к',
        't':'е',
        'y':'н',
        'u':'г',
        'i':'ш',
        'o':'щ',
        'p':'з',
        '[':'х',
        ']':'ъ',
        'a':'ф',
        's':'ы',
        'd':'в',
        'f':'а',
        'g':'п',
        'h':'р',
        'j':'о',
        'k':'л',
        'l':'д',
        ';':'ж',
        "'":'э',
        'z':'я',
        'x':'ч',
        'c':'с',
        'v':'м',
        'b':'и',
        'n':'т',
        'm':'ь',
        ',':'б',
        '.':'ю',
        '/':'.',
        '?':','
    }

dictionary_ru_to_en = \
    {
        'й':'q',
        'ц':'w',
        'у':'e',
        'к':'r',
        'е':'t',
        'н':'y',
        'г':'u',
        'ш':'i',
        'щ':'o',
        'з':'p',
        'х':'[',
        'ъ':']',
        'ф':'a',
        'ы':'s',
        'в':'d',
        'а':'f',
        'п':'g',
        'р':'h',
        'о':'j',
        'л':'k',
        'д':'l',
        'ж':';',
        'э':"'",
        'я':'z',
        'ч':'x',
        'с':'c',
        'м':'v',
        'и':'b',
        'т':'n',
        'ь':'m',
        'б':',',
        'ю':'.',
        '.':'/',
        ',':'?'
    }

# По умолчанию перевод идёт с английского на русский. 
# Если нужно наоборот, в аргумент нужно подать 'ru'
def layout_switch(text,arg = 'en'): 
    text = text.lower()
    buffer_list = []
    for i in range(len(text)):
        buffer_list.append(text[i])
    if arg == 'ru':
        for i in range(len(text)):
            if text[i] in dictionary_ru_to_en.keys():
                buffer_list[i] = dictionary_ru_to_en[f'{text[i]}']
    if arg == 'en':
        for i in range(len(text)):
            if text[i] in dictionary_en_to_ru.keys():
                buffer_list[i] = dictionary_en_to_ru[f'{text[i]}']
    result = ''
    for i in range(len(text)):
        result += buffer_list[i]
    return result

# print(layout_switch('ghbdtn? XTKJDTR'))
