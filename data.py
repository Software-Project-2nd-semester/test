from random import randint                #랜덤 모듈에 randint만 사용

def generate_numbers():                   # 함수 선언
    numbers = []                          #세 가지 정수를 담을 숫자열 선언
    i = 0
    new_number = 0
    while i < 3:
        new_number = randint(0, 9)        # 0 ~ 9 사이의 랜덤한 수를 뽑는다.
        if new_number not in numbers:     # 수가 문자열에 겹치지 않으면
            numbers.append(new_number)    # 숫자열 오른쪽에 추가한다.
            i += 1
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers                        # 만들어진 숫자열을 리턴합니다.

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    i = 0
    new_guess = []                              # 입력받을 숫자열 선언
    while i < 3:
        gue_number = int(input("{}번째 숫자를 입력하세요: ".format(i + 1))) #사용자에게 입력받음
        if gue_number > 9 and gue_number < 0:   # 범위안에 숫자를 입력 받기 위한 IF문
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if gue_number in new_guess:             # 중복된 정수인지 판별
            print("중복되는 숫자입니다. 다시 입력하세요. ")
        else:
            new_guess.append(gue_number)        # 조건에 맞는 정수를 저장한다.
            i += 1

    return new_guess

def get_score(guess, solution):       # 사용자가 입력한 숫자열, 정답 숫자열을 받아서
    strike_count = 0
    ball_count = 0
    i = 0

    while i < len(guess):
        if guess[i] == solution[i]:   # 위치와 값이 같을 때
            strike_count += 1         # 스트라이크 카운팅
            i += 1
        elif guess[i] in solution:    # 값은 있지만 위치가 다를 때
            ball_count += 1           # 볼 카운팅
            i += 1
        else:                         # 둘다 다를 때
            i += 1

    return strike_count, ball_count   # 스트라이크 개수, 볼 개수 리턴

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while 1:
    GUESS = take_guess()
    strike, ball = get_score(GUESS, ANSWER)
    print("{}S {}B ".format(strike, ball))

    if strike == 3:
        tries += 1
        break
    else:
        tries += 1

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))