import os


folder = r'C:\Users\HOME\Desktop\GB\Python\HT\Mishkuz_Oleynik_HT_7'

# bin_files = [item for item in os.listdir(folder) if os.path.isfile(item)]
# bin_files = [item for item in os.listdir(folder) if os.path.isdir(item)]
# print(bin_files, sep="\n")

# django_dirs = (item for item in os.environ)
# for st in django_dirs:
#     print(type(st), st)


# bin_files = [os.path.join(folder, item) for item in os.listdir(folder) if item.lower().endswith('.py')]
# print(bin_files)

# print(os.path.join(folder, 'main.py'))
# print(os.path.split(r'C:\Users\HOME\Desktop\GB\Python\HT\Mishkuz_Oleynik_HT_7\test.py'))

#
# print(os.getcwd())
# os.chdir(r'C:\Users\HOME\Desktop\GB\Python\HT')
# print(os.getcwd())
# files= [[os.path.isfile(item), item] for item in os.listdir() ]
# print(files)
#
# dir_name = 'test_dir'
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)
# else:
#     os.rmdir(dir_name)
#
# dir_path = os.path.join('data', 'src')
# if not os.path.exists(dir_path):
#     os.makedirs(dir_path)

os.chdir(r'C:\Users\HOME\Desktop\GB\Python\HT\Mishkuz_Oleynik_HT_7')
print(os.getcwd())

# for root, dirs, files in os.walk(os.getcwd()):
#     print(root, dirs, files)
os.remove('data\src')



