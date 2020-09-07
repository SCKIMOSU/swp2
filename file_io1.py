# open(): 파일을 특정한 모드로 여는 함수. 읽을 때는 r, 쓸 때는 w
# read(): 파일 객체로부터 모든 내용을 읽는 함수
# readline(): 파일 객체로부터 한 줄씩 문자열을 읽는 함수
# readlines(): 전체 내용을 한 번에 리스트에 담는 함수

f=open("input.txt", "r", encoding= "UTF-8")
list = f.readlines()
print(list)