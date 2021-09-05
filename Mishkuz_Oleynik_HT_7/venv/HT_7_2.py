import os

# with open('config1.yaml', 'r', encoding='utf-8') as config_file:
#     try:
#         folders = [st.strip().split('|--')[-1] for st in config_file]
#         # print(*folders)
#         os.mkdir(folders[0])
#         os.chdir(folders[0]) 
#         for st in folders[1:]:
#             os.mkdir(st)
#     except FileExistsError:
#         print('КОнфликт совпадения имен')

settings = {}
with open('config2.yaml', 'r', encoding='utf-8') as config_file:
    lines = dict(map(str.split, config_file.readlines()))

basedir = lines.pop('base')
for k, v in lines.items():
    os.makedirs(os.path.join(os.curdir, basedir, k), exist_ok=True)
    for i in v.split(','):
        with open(os.path.join(os.curdir, basedir, k,i), "w") as f:
            print (i,k)

