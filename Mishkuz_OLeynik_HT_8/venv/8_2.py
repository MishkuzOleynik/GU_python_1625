import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as log:
    text = log.read()

patt = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)\s\D+(\b\d{2}\/\w{3}\/\d{4}\:\d{2}\:\d{2}\:\d{2}\ ' \
       r'\+\d{4}\b)\D+\"(\w+)\b\s(\/\D+\d\b)\s\D+\d\.\d\"\s(\d+)\s(\d+)\s\"'
parlogs = re.findall(patt, text, flags=re.ASCII)
print(parlogs)
# print(text)