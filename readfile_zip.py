import zipfile
with zipfile.ZipFile('test1.zip') as thezip:
    list_name = thezip.namelist()
    # print(list_name)
    for name in list_name:
        with thezip.open(name, mode='r') as thefile:
            print(thefile.read().decode())