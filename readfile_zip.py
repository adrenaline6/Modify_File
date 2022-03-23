import zipfile
def read_in_zip():
    #change file zip name
    with zipfile.ZipFile('test1.zip') as thezip:
        list_name = thezip.namelist()
        # print(list_name)
        for name in list_name:
            with thezip.open(name, mode='r') as thefile:
                print(thefile.read().decode())
            thefile.close()
    thezip.close()
def write_to_zip():
    #change name zip file
    zip_file = zipfile.ZipFile('added.zip', 'w')
    #change file name
    zip_file.write('result.txt')
    zip_file.write('pdf_test.txt')
    zip_file.close()
def read_directory():
    zip_name = 'test1.zip'
    with zipfile.ZipFile(zip_name, 'r') as thezip:
        print(thezip.namelist())
    thezip.close()
if __name__ == '__main__':
    # write_to_zip()
    # read_in_zip()
    read_directory()