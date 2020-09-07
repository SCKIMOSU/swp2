# open(): 파일을 특정한 모드로 여는 함수. 읽을 때는 r, 쓸 때는 w
# read(): 파일 객체로부터 모든 내용을 읽는 함수
# readline(): 파일 객체로부터 한 줄씩 문자열을 읽는 함수
# readlines(): 전체 내용을 한 번에 리스트에 담는 함수

f=open("input.txt", "r", encoding= "UTF-8")
list = f.readlines()
# 모든 줄을 읽은 내용을 list에 담았다가 list 원소 처리기법 활용할 수 있다.
for i, data in enumerate(list): #enumerate()는 각 원소에 접근 수 있도록 함
    print("%d번째 줄: %s" %(i+1, data), end='')
f.close() #file 을 open 하면 close 한다

# file 을 open 하면 close 하는 과정이 번거롭게 느껴질 수 있다.
# file을 자동으로 열러주고, 자동으로 닫아주는 기법, 즉, 메모리에 자동할당하는 기법을 활용해보자
# 편리한 파일 입출력을 지원하는 문법을 다음으로 알아보자
# with 문법이다.

