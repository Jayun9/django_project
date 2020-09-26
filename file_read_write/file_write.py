from random import randint
with open("./resource/test.txt",'w') as f:
    f.write("Nice man! \n")

with open("./resource/test.txt",'a') as f:
    f.write("Good man! \n")

with open("./resource/test2.txt",'w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write("\n")
#리스트를 파일로
with open("./resource/test3.txt",'w') as f:
    list = ['kim\n', 'park\n', 'cho\n']
    f.writelines(list)
with open("./resource/test4.txt",'w') as f:
    print("real good man!!", file=f)
    print("real nice man!!", file=f)
