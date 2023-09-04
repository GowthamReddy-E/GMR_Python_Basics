file1=open("F:/gowthamCodingProjects/vsCodeWorkSpace/pythonWorkSpace/GMR_Python_Basics/File/basicInfo.txt","r")

print(file1.read())
    # it will read the file one by onbe line all the file text
print(file1.readline())
    #  it will read the file the first line only

print(file1.readlines())
    # it will also read the file the output type is array type and if you pass the number of lines also


file1.close()