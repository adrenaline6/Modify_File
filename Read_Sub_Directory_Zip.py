import zipfile

# thay doi ten zip file
zip_name = 'test1.zip'

with zipfile.ZipFile(zip_name, 'r') as thezip:
    print(thezip.namelist())
thezip.close()