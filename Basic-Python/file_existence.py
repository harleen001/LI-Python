from pathlib import Path
filename=input("Enter your bill filename : ")
path = Path(filename)

if path.is_file():
    print(f'The file exists')
else:
    print(f'The file does not exist')
    f = open(filename, "w")
    filecontent =input("Enter file contents = ")
    f.write(filecontent)
    f.close()