from baseball_game_engine import make_quiz, check
answer = make_quiz()
# print(answer)

# 무한 반복
while True:
    # 숫자 3자리 중복 없이 묻자
    player = input("숫자 3자리는? : ")
    # strike, ball 확인하자
    strike, ball = check(answer, player)
    # 출력하자
    print(f'{player}\tstrike : {strike}\tball : {ball}')
    # strike가 3일 때, 나가자
    if strike == 3:
        break
# 축하해주자

