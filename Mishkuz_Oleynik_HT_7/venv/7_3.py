import os
SRC_FOLDER = 'my_project'
DST_FOLDER = 'templates'
print(os.getcwd())
print(*os.walk(SRC_FOLDER), sep='\n')

for x, *y in os.walk(SRC_FOLDER):
    for i in y:
        newpath = os.path.join(os.curdir, DST_FOLDER, os.sep.join(x.split(os.sep)[1:]), i)
        print(x.split(os.sep),i,y)
        os.makedirs(newpath,exist_ok=True)

