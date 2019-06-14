import os
xyt_path = 'Output/2004_A/'
file_path = 'FVC/'

dbs = os.listdir(xyt_path)
print(dbs)

for db in dbs:
    counter = 0
    xyts = set()
    for xyt in os.listdir(xyt_path+db):
        xyts.add(xyt)
    for img in os.listdir(file_path+db):
        if img.split('.')[0]+'.xyt' not in xyts:
            counter += 1
            os.remove(file_path+db+'/'+img)
    print(db, "Done")
    print(counter, "files deleted")
