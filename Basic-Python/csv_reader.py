import csv
with open("excel_file.csv","r") as file:
    filecontents=csv.reader(file)
    #filecontents=csv.reader(file,delimiter='\t')
    for i in filecontents:
        print(i,end=' ')



