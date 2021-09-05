# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей
# вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# import sys
def unpars_str(st):
    st_list = str.split(st)
    return st_list[0], st_list[5], st_list[6]
# Выборка нужных элементов из строки лога
with open("log.txt" , "r") as log:
    unparsed_log = (unpars_str(st) for st in log)
    print(*unparsed_log, sep='\n')
print(type(unparsed_log))

# Нахождение адреса спамера
adresses_count = {}
with open("log.txt" , "r") as log:
    unparsed_log = (unpars_str(st) for st in log)
    for item in unparsed_log:
        if adresses_count.get(item[0]):
            adresses_count[item[0]] += 1
        else:
            adresses_count[item[0]] = 1
print('Максимальное количество запросов с одного адреса: ', max(adresses_count.values()))
for key, val in adresses_count.items():
    if val == max(adresses_count.values()):
        spam_adress = key
print('Адрес спамера: ', spam_adress)