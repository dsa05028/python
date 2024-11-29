# 파일입출력

'''with open("test.txt","w",encoding="utf-8") as file:
    file.write("안녕하세요\n")
    file.write("파이썬쓰기연습\n")'''

    
with open("user.txt","r",encoding="utf-8") as file:
    line=file.readline()
    while line:
        print(line.strip())
        line = file.readline()
