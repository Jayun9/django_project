#파일 읽기
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
f.close()

print("------------------------------------------------")
print("------------------------------------------------")
print(2)
#예제 2 with 문을 쓰면 close를 안써도 됨.
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)

print("------------------------------------------------")
print("------------------------------------------------")
print(3)

#기본적으로 반복 가능, 한줄 단위로 \n무시하기 위해strip 사용 가능
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())
        
print("------------------------------------------------")
print("------------------------------------------------")
print(4)
#read로 읽어오면 커서가 마지막으로 움직임, 그래서 두번째 read시에는 내용 없음
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content)

        
print("------------------------------------------------")
print("------------------------------------------------")
print(5)
#한문장 단위로 처리하기
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end=' #### ')
        line = f.readline()
print("------------------------------------------------")
print("------------------------------------------------")
print(6)
#readlines는 엔터 기준으로 리스트 형태로 반환해 준다.
with open('./resource/review.txt', 'r') as f:
    lines = f.readlines()
    for c in lines:
        print(c, end=" ***** ")

print("------------------------------------------------")
print("------------------------------------------------")
print(7)
#응용
scores = []
with open('./resource/score.txt', 'r') as f:
    for score in f:
        scores.append(int(score))
#6자리이고 소숫점은 3번째 자리까지
print("Average : {:6.3}".format(sum(scores)/len(scores)))