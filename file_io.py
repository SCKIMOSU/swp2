# open(): 파일을 특정한 모드로 여는 함수. 읽을 때는 r, 쓸 때는 w
# read(): 파일 객체로부터 모든 내용을 읽는 함수
# readline(): 파일 객체로부터 한 줄씩 문자열을 읽는 함수
# readlines(): 전체 내용을 한 번에 리스트에 담는 함수

f=open("input.txt", "r", encoding= "UTF-8")
# f: file object (파일객체)
f.seek(9)
# seek(): 파일에서 읽을 위치를 선정해주는 함수
# 9 바이트의 위치에서부터 파일을 읽음
# 한글이 유니코드로 사용될 때, 파이썬에서는 한 글자당 3바이트를 할당함 (시스템마다 다름)
# 세요?
# 홍길동입니다.
# 세 번재 줄에는 무슨 말을 쓸까요?

data=f.read()
# 파일 내용을 한 번에 읽는 것은 read(),
# 파일 내용에서 한 줄씩 읽는 것은 readline()

print(data)
f.close() #해당 파일에 대한 리소스 사용이 끝남

# 두 번째 예제
f=open("input.txt", "r", encoding= "UTF-8")

count=0
while count < 3:
    data=f.readline()
    count = count +1
    print("%d번째 줄: %s" %(count, data), end='')
    # %s : 문자열이 출력될 형식지정자
f.close()