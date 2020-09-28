# try, except, esle
name = ['koo', 'kim', 'park']
try:
    z = 'zho'
    x = name.index(z)
    print("{} Found it! in name {}".format(z, x))
except ValueError:
    print("Not Found it! -Occurred ValueError!")
else: # 에러가 발생하지 않았을 경우 실행
    print("ok! else!")

print("-----------------------------------------")
print("-----------------------------------------")
print("-----------------------------------------")

#filnally는 예외가 발생해도 안되도 무조건 실행 -> 리소스 해제와 같은 상황에서 사용한다, 
name = ['koo', 'kim', 'park']
try:
    z = 'zho'
    x = name.index(z)
    print("{} Found it! in name {}".format(z, x))
except ValueError:
    print("Not Found it! -Occurred ValueError!")
else: # 에러가 발생하지 않았을 경우 실행
    print("ok! else!")
finally:
    print("finally ok!")

print("-----------------------------------------")
print("-----------------------------------------")
print("-----------------------------------------")

name = ['koo', 'kim', 'park']
try:
    z = 'zho'
    x = name.index(z)
    print("{} Found it! in name {}".format(z, x))
except ValueError as l:
    print(l)
except IndexError:
    print("Not Found it! -IndexError ValueError!")
except Exception: # 순서가 중요, 맨처음에 놓았다면 모든 에러가 이곳으로 오기때문에 원하는 결과 아닐 수 있음
    print("Not Found it! -Occurred ValueError!")
else: # 에러가 발생하지 않았을 경우 실행
    print("ok! else!")
finally:
    print("finally ok!")

print("-----------------------------------------")
print("-----------------------------------------")
print("-----------------------------------------")

#raise 키워드로 문제 발생 -> 예외 처리로 특정 상황을 관리하고 싶을때 
try: 
    a='333'
    if a == 'kim':
        print("ok 허가")
    else:
        raise ValueError
except ValueError:
    print("문제 발생")
except Exception as f:
    print(f)
else:
    print("ok")

