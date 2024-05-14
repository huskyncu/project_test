with open("data.txt", mode='r+') as myfile:
    myfile.write("12345")
    myfile.seek(0)
    myfile.write("***")
    
with open('chinese.txt',mode='w',encoding='UTF-8') as f:
    f.write("中文文字")