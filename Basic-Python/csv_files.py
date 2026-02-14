import csv
with open("excel_file.csv","r") as file:
    filecontents=file.read()
    for i in filecontents:
        print(i,end=' ')
