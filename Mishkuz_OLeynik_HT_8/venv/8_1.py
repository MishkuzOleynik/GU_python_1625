# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
# почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
# Пример:


# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru


# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?


def email_parse(email):
    import re
    check = re.match('\w+@\w+\.\w+', email)
    if check:
        pars = re.split((r'@'), email)
        print({'username': pars[0], 'domain' : pars[1]})
    else:
        raise ValueError(f'wrong email: {email}')


email_parse('mishkuz@gmail.com')


