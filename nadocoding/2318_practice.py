'''
# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 8)
print(3 * (3 + 1))

# 문자열 자료형 : 문자열과 정수를 섞어서 계산을 해서 실행을 할 수 있다.
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ" * 9)

# boolean 자료형 : 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
# age, is_adult는 정수형과 boolean 자료형이므로 +와 함께 출력문으로 쓰이기 위해서는 str()로 감싸줘야한다.
# 출력문은 쉼표로도 여러 문장을 합쳐서 str()로 감쌀 필요없이 출력할 수 있다. 콤마가 있는 부분에 공백이 하나씩 추가됨을 참고해야 한다.
# 애완동물을 소개해 주세요~
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print("연탄이는 어른일까요? " + str(is_adult))


# 주석
작은따옴표 3개를
이용하면은 여러문장을
한꺼번에 주석 처리 할 수 있다.


# 퀴즈 1
# Quiz) 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장 : xx 행 열차가 들어오고 있습니다.
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1 + 1)  # 2
print(3 - 2)  # 1
print(5 * 2)  # 10
print(6 / 3)  # 2

print(2 ** 3)  # 2^3 = 8
print(5 % 3)  # 나머지 구하기 2
print(10 % 3)  # 1
print(5 // 3)  # 몫 구하기 1
print(10 // 3)  # 3

print(10 > 3)  # 비교 연산 True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # True

print(3 == 3)  # True
print(4 == 2)  # False
print(3 + 4 == 7)  # True

print(1 != 3)  # True
print(not (1 != 3))  # False

print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True

print((3 > 0) or (3 > 5))  # True
print((3 > 0) | (3 > 5))  # True

print(5 > 4 > 3)  # True
print(5 > 4 > 7)  # False

# 간단한 수식
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
number = 2 + 3 * 4  # 14
print(number)
number = number + 2  # 16
print(number)
number += 2  # number = number + 2와 같은 말, 18
print(number)
number *= 2  # 36
print(number)
number /= 2  # 18
print(number)
number -= 2  # 16
print(number)
number %= 5  # 1
print(number)

# 숫자처리함수
print(abs(-5))  # 절댓값 5
print(pow(4, 2))  # 4^2 = 4*4 = 16
print(max(5, 12))  # 최댓값 12
print(min(5, 12))  # 최솟값 5
print(round(3.14))  # 반올림 3
print(round(4.99))  # 5

from math import *  # math 라이브러리 안에 있는 모든 것을 이용하겠다.

print(floor(4.99))  # 내림 4
print(ceil(3.14))  # 올림 4
print(sqrt(16))  # 제곱근 4

# 랜덤함수
from random import *

print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성, 양 끝 값 포함

# 퀴즈 2
# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다
# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
# (출력문 예제) 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
from random import *

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)  # 줄바꿈도 포함해서 4줄이 출력된다.

# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # :(콜론)의 의미는 0 부터 2 직전까지 (0~1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])  # 7 부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])  # 맨 뒤에서 7번째부터 끝까지, 맨 뒷자리 인덱스는 -1부터 시작한다.

# 문자열처리함수
python = "Python is Amazing"
print(python.lower())  # 대문자를 소문자로
print(python.upper())  # 소문자를 대문자로
print(python[0].isupper())  # 인덱스 번호의 문자가 대문자가 맞니? True
print(len(python))  # python 문자열의 길이
print(python.replace("Python", "Java"))  # 문자열에서 "Python"을 찾아서 "Java"로 바꿔서 출력시켜준다

index = python.index("n")  # python 문자열에서 "n"이 몇 번째 인덱스에 있니?
print(index)
index = python.index("n", index + 1)  # 두 번째 n을 찾는 것
print(index)

print(python.find("n"))  # n이 포함된 위치를 출력
print(python.find("Java"))  # 내가 원하는 값이 문자열에 포함되어 있지 않으면 -1이 출력된다.
# print(python.index("Java")) python에는 "Java"라는 값이 없으므로 오류를 내며 프로그램을 종료한다.
print("hi")

print(python.count("n"))  # python이라는 변수에서 "n"이라는 값은 몇 번이 나오는지 계산해준다.

# 문자열포맷
# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20)  # %d는 정수
print("나는 %s을 좋아해요." % "파이썬")  # %s는 문자열, String값
print("Apple은 %c로 시작해요." % "A")  # %c는 한글자만 받는다.
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))  # 두 개의 값을 콤마로 구분하고, 괄호로 묶는다.

# 방법 2
print("나는 {}살입니다.".format(20))  # 중괄호에 format 안에 있는 값을 넣어준다.
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))  # 중괄호 안에 숫자를 넣으면 순번에 맞게 출력이 된다.
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")  # f로 문장을 시작

# 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
print("G:\\ProgrammingPython\\nadocoding")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Rea\tApple")

# 퀴즈 3
# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#               (nav)              (5)           (1)           (!)
# 예) 생성된 비밀번호 : nav51!
url = "http://naver.com"
my_str = url.replace("http://", "")  # 규칙1
my_str = my_str[:my_str.index(".")]  # 규칙2
# my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
# my_str 안에 들어가있는 문자열에서 처음부터 my_str에서 처음 나오는 점의 위치 직전까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# 리스트 []
# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")  # append 더하다
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")  # insert 삽입하다
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())  # pop 꺼내다
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 사전
cabinet = {3: "유재석", 100: "김태호"}  # key : value
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) 오류 메시지를 내보내며 프로그램을 종료시킨다.
print(cabinet.get(5))  # none이라는 글씨가 출력되며, 계속 이어나갈 수 있다.
print(cabinet.get(5, "사용 가능"))  # 값이 없으면은 "사용 가능"이라는 문자를 출력한다.
print("hi")

print(3 in cabinet)  # 3이라는 키가 cabinet에 있으면 True가 나온다
print(5 in cabinet)  # False

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"  # 유재석이라는 값이 빠지고 김종국씨라는 값을 업데이트한다.
cabinet["C-20"] = "조세호"  # cabinet에 C-20이라는 키를 만들고 그 키에 조세호씨라는 값을 추가한다.
print(cabinet)

# 간 손님
del cabinet["A-3"]  # 키 삭제
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

# 튜플 : 리스트와 달리 내용 변경과 추가를 할 수 없다.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") => 추가 불가. 튜플은 고정된 값만 쓸 수 있다.

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = ("김종국", 20, "코딩")
print(name, age, hobby)

# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊었어요
java.remove("김태호")
print(java)

# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# 퀴즈 4
# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용
# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --
# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *

users = range(1, 21)  # 1부터 20까지 숫자를 생성
# print(type(users)) type이 range이기 때문에 type을 변경해준다.
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)  # 4명 중에서 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

# 분기 if
# if 조건:
#     실행 명령문
# elif 조건:
#     실행 명령문
# else :
#     실행 명령문
weather = input("오늘 날씨는 어때요? ") # 사용자의 입력을 받는 문장, input을 통해 입력 받고 문자열 형태로 변수에 저장된다.
if weather == "비" or weather == "눈":
    print("우산을 챙기세요") # or을 통해서 조건을 추가할 수 있다. or은 앞 조건 혹은 뒷 조건이 맞을 때 출력된다.
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요") # and : 앞 조건 뒷 조건이 모두 성립할 때 출력된다.
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

# 반복문 for
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# for 변수 in 리스트(범위):
#   실행 명령문
for waiting_no in range(1, 6):  # range를 통해 1 부터 6 미만까지를 for문에 쓸 수 있다. [1, 2, 3, 4, 5]라 써도 된다.
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# 반복문 while
customer = "토르"
index = 5
# while (조건):
#   실행 명령문
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
index = 1
while True: # 이 문장은 무한 반복되므로 Ctrl + C를 누르면 강제종료가 됩니다.
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1

customer = "토르"
person = "Unknown"
while person != customer: # 조건에 성립할 때까지 반복
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

# continue와 break
absent = [2, 5]  # 결석
no_book = [7]  # 책을 깜빡했음
for student in range(1, 11):  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent:
        continue
    # if student in no_book :
    #     print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
    #     break
    print("{0}, 책을 읽어봐".format(student))

# 한 줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1, 2, 3, 4, 5]
print(students)
students = [i + 100 for i in students]  # students 리스트에 있는 i들을 하나씩 불러와 100을 더한 값을 리스트에 집어넣어라.
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]  # len 문자열이나 어떤 값의 길이
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# 퀴즈 5
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2분
from random import *

cnt = 0  # 총 탑승 승객 수
for passenger in range(1, 51):  # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51)  # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15:  # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(passenger, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(passenger, time))
print("총 탑승 승객 : {0}분".format(cnt))


# 함수
# def 함수 이름(전달값):
#   함수가 하는 일
#   반환값
def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()  # 함수 호출


# 전달값과 반환값
def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission  # 여러 개의 값을 ,(콤마)를 통해서 반환할 수 있다.


balance = 0  # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
         .format(name, age, main_lang)) # \(역슬래시)를 이용하여 두 문장을 하나의 문장으로 처리하게 할 수 있다.

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
# 전달값을 적지 않을 시 기본값으로 자동 설정!

profile("유재석")
profile("김태호")

# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20) # 매개변수의 값을 키워드를 이용해서 함수를 호출해주면은 그 키워드에 해당하는 값이 순서가 뒤섞여있어도 잘 전달된다.
profile(main_lang="자바", age=25, name="김태호")

# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" "이 있으면 문장이 출력되고 나서 줄바꿈을 하지 않고 이어서 밑에 있는 문장을 계속 출력한다.
    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):  # *(가변인자)변수명 : 원하는 만큼 변수에 값을 넣을 수 있다.
    print("이름 : {0}\t나이 : {1}\t".format(name, age),
          end=" ")  # end=" "이 있으면 문장이 출력되고 나서 줄바꿈을 하지 않고 이어서 밑에 있는 문장을 계속 출력한다.
    for lang in language:
        print(lang, end=" ")
    print()  # 줄바꿈


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

# 지역변수(함수 내에서만 사용할 수 있는 것, 함수가 끝나면 사라짐)와 전역변수(프로그램 내 어디서든지 부를 수 있는 변수)
gun = 10


def checkpoint(soldiers):  # 경계근무
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)  # 함수를 호출하면서 변수를 넘긴다. 그래서 내부에서 계산을 하고, 변경된 값을 리턴을 해준다.
print("남은 총 : {0}".format(gun))


# 퀴즈 6
# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
#  남자 : 키(m) x 키(m) x 22
#  여자 : 키(m) x 키(m) x 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

height = int(input("키를 입력해주세요 "))
gender = input("성별을 입력해주세요 ")
def std_weight(height, gender):
    if gender == "남자":
        weight = round(height * height * 22, 2)
        print(f"키 {height} {gender}의 표준 체중은 {weight}kg 입니다.")
    elif gender == "여자":
         weight =  round(height * height * 21, 2)
         print(f"키 {height} {gender}의 표준 체중은 {weight}kg 입니다.")
    else:
        print("성별 오류")
std_weight(height / 100, gender)

def std_weight(height, gender):  # 키 m 단위 (실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175  # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# 스타크래프트 프로젝트 전반전 & 스타크래프트 프로젝트 후반전
from random import *
# 클래스 & __init__ & 메소드 오버라이딩
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # 생성자, 객체가 만들어질 때 자동으로 생성된다.
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

marine1 = Unit("마린", 40, 5) # Unit 클래스의 인스턴스
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 멤버변수
# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 클래스 외부에서 멤버변수를 확장할 수 있다, 그러나 확장한 객체에만 적용이 된다. (기존객체에 적용x)

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 메소드  & 상속
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X.
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 다중 상속
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0으로 초기화
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 오버라이딩
        self.fly(self.name, location)

# pass : 아무것도 안하고 일단은 넘어간다. 일단은 완성된 것처럼 보여진다. & super
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # 다중 상속 시에는 문제가 발생하므로, 여러 번을 통해 초기화해야 한다.
        self.location = location


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20,  5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else : # 클로킹 모드 해제 -> 모두 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1) # 리스트에 추가
attack_units.append(m1)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # 지금 만들어진 객체가 특정 클래스의 인스턴스인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank): # 이 클래스로 만들어진 객체(인스턴스)인지 확인한다.
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()

# 퀴즈 8
# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
'''

# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# 모듈을 별명을 통해 줄여서 사용
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# 모듈에 있는 모든 것을 사용하겠다는 의미
# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# 모듈에 있는 price와 price_morning만 사용하겠다는 의미
# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7) 오류 발생

# theater_module에 있는 price_soldier만 가져다 쓸 건데, price로 별명을 지어서 사용하겠다 (기존 price와 다르다)
# from theater_module import price_soldier as price
# price(3)

# import는 항상 모듈이나 패키지만 올 수 있다
# import travel.thailand
# import travel.thailand.ThailandPackage 사용 불가
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# travel.thailand에 있는 ThailandPackage 클래스를 import한 것
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))