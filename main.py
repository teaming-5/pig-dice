import random

player1 = input("플레이어1의 이름을 입력하세요 : ")
player2 = input("플레이어2의 이름을 입력하세요 : ")

player1_score = 0
player2_score = 0

goal = int(input('목표 점수 : '))

current_player = player1
while player1_score < goal and player2_score < goal:
    print(player1_score, player2_score)
    print('지금 플레이어 :', current_player)
    
    sum = 0
    while True:
        dice = random.randrange(1, 7)
        print(dice)
        if dice == 1:
            sum = 0
            break

        else :
            sum += dice
            reroll = input()

            if reroll == 'bank':
                break

    if current_player == player1:
        player1_score += sum
        current_player = player2

    else:
        player2_score += sum
        current_player = player1

print(player1_score, player2_score)
