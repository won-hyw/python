#1 주민번호
# 주민등록번호 앞 6자리를 변수 id_number에 넣고, 출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
id_number = "020316"
year = id_number[0:2] # [:2], [-6:-4]
month_day = id_number[2:6] # [2:], [-4:]
print(year)
print(month_day)
print("둘의 곱은 : " + str(int(year) * int(month_day)))

#2 전화번호
# 집 전화번호를 phone_number에 넣고, 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
phone_number = "02-1234-5678"
x = phone_number.find('-') # index()가 찾는 문자가 없으면, ValueError. find()의 경우 찾는 문자가 없으면, -1.
print(phone_number[0:x]) # [:2]
print(phone_number[-4:]) # [8:]

phone_number2 = "032-9876-4321"
x = phone_number2.index('-')
print(phone_number2[0:x]) # [:3]
print(phone_number2[-4:]) # [9:]

# 전화번호 입력시, -가 있든, -가 없든, 찰떡같이 알아먹기
phone_number1 = '010-1234-5678'
phone_number2 = '01098765432'
phone_number3 = '010 1111 2222'

phone_number = phone_number3
result = phone_number.replace('-', '').replace(' ', '') # 대치
print(result)

# result = phone_number3.replace(' ', '')
# print(result)

# Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 1 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
student_number = "2302"
number = student_number[1] # '3'
number = int(number) # str -> int
# if number == 1 or number == 2:
#     print(f"{number}반 뉴미디어소프트웨어과")
# elif number == 3 or number == 4:
#     print(f"{number}반 뉴미디어웹솔루션과")
# elif number == 5 or number == 6:
#     print(f"{number}반 뉴미디어디자인과")
# else:
#     print("잘못 입력했습니다.")

# majors = ['뉴미디어소프트웨어과', '뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
# print(f"{number}반 {majors[number-1]}")

majors = ['뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어디자인과']
if 1 <= number <= 6:            # 1 <= number && number <= 6 in java
    print(f"{number}반 {majors[(number - 1) // 2]}") # number-1의 숫자에 2개의 반씩 있으니까 정수로 2 나누기
else:
    print("잘못입력했습니다.")

# Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2
def get_major(student_number):
    if student_number[1] == "1" or student_number[1] == "2": # or을 사용할 때 명시적으로 이렇게 써주는 것이 좋다.
        return "뉴미디어소프트웨어과", student_number[0]
    elif student_number[1] == "3" or student_number[1] == "4": # '4' == True, 문자만 있으면 무조건 트루가 되어버린다.
        return "뉴미디어웹솔루션과", student_number[0]
    elif student_number[1] == "5" or student_number[1] == "6":
        return "뉴미디어디자인과", student_number[0]
    else:
        return "잘못 입력했습니다.", ""
# if문 안에서 major을 생성하기 때문에, global major을 이용해서 변수를 만들어놓아둘 수 있다.
major, grade = get_major('2100')
print(major, grade)

# Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5
# 평균 = 총합 / 개수
def average(*numbers):
    sum_value = 0 # 파이썬은 sum이라는 함수가 있어서 변수로 사용해버리면 이 sum 함수를 사용하지 못한다.
    count = 0
    for number in numbers:
        sum_value += number
        count += 1
    return sum_value / count

print(average(10, 20, 30)) # (10, 20, 30) ==> numbers라는 이름으로 튜플로 들어간다.
print(average(4, 23))

def average2(*numbers):
    return sum(numbers) / len(numbers)

print(average2(10, 20, 30)) # (10, 20, 30) ==> numbers라는 이름으로 튜플로 들어간다.
print(average2(4, 23))

# Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만
def get_bmi(height, weight):
    height /= 100
    return round(weight / height ** 2, 1)

bmi = get_bmi(176, 69)
print(bmi) #22.3

if bmi < 18.5:
    print('저체중')
elif bmi < 23:
    print('정상')
elif bmi < 25:
    print('과체중')
elif 25 <= bmi:
    print('비만')
