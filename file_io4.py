

# 파일에 있는 문자를 처리하는 예제
# 파일에 있는 문자의 비도수를 처리하는 예제

def process(filename):
    with open(filename, "r") as f: # 특정한 파일을  읽기 모드로 읽음
        # 각 문자의 빈도수를 추출하기 위하여 사전 데이터를 만들어주자
        # dict는 key와 value, 키와 값으로 구성되어 있기 때문에
        # 키:알파벳, 값: 빈도수
        dict={}
        data=f.read()
        for i in data: # 각 문자열을 방문하면서 하나씩 체크한다
            if i in dict: # 자료형에 키로 문자 알파벳이 포함되어 있다면
                dict[i] +=1 # 빈도수를 1씩 증가, 특정한 알바벳이 여러 번 나오는 경우, 1씩 증가
            else:
                dict[i]=1 # 그렇지 않으면 1로 설정, 특정한 알파벳을 처음 발견했한 경우.


    return dict # 해당 자료형을 리턴한다.


dict=process("input.txt")








with open("input.txt", "r", encoding= "UTF-8") as f:
    list = f.readlines()
     # 모드 줄을 읽 내용을 list에 담았다가 list 원소 처리기법 활용할 수 있다.
    for i, data in enumerate(list): #enumerate()는 각 원소에 접근 수 있도록
        # 리스트의 인덱스와 원소를 접근한다.
        print("%d번째 줄: %s" %(i+1, data), end='')
# open하는 부분과 close 하는 부분이 생략된다.
# 코드가 짧아지고 간결해 지는 것은 우리가 원하는 목표이다.






