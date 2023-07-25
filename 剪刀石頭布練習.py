#NTU 360期,課堂練習
print("歡迎來到剪刀、石頭、布")
name = input("請輸入你的名稱:")
count_win = 0
count_lose = 0
count_peace = 0
for i in range(0, 3):
    player_hand = int(input(("請出拳: (1)  剪刀 (2) 石頭 (3) 布 : ")))
    import random
    computer_hand = random.randint(1,3)
    
    if player_hand == computer_hand :
        print("平手")
        count_peace += 1
    elif player_hand == 1 and computer_hand == 2 or player_hand == 2 and computer_hand == 3 or player_hand == 3 and computer_hand == 1:
        print("你輸了")
        count_lose += 1
    #elif (player_hand, computer_hand) in [(1, 2), (2, 3), (3, 1)]:              #使用資料結構方法
        #print("你輸了")
        #count_lose += 1
    else :
        print("你贏了")
        count_win += 1
        
    if player_hand == 1:
        player_hand = "剪刀"    
    elif player_hand == 2:
        player_hand = "石頭"
    elif player_hand == 3:
        player_hand = "布"
    if computer_hand == 1:
        computer_hand = "剪刀"
    elif computer_hand == 2:
        computer_hand = "石頭"
    elif computer_hand == 3:
        computer_hand = "布"
    print(f"{name} 出了: {player_hand} 電腦出了: {computer_hand}" )
print("===============================\n總結:")    
if count_peace == 3:
    print(f"平手了{count_peace}把")
elif count_peace == 2 and count_win == 1:
    print(f"平手{count_peace}把,贏了{count_win}把")
elif count_peace == 2 and count_lose == 1:
    print(f"平手{count_peace}把,贏了{count_lose}把")
elif count_peace == 1 and count_win == 1 and count_lose == 1:
    print(f"平手{count_peace}把,贏了{count_lose}把,輸了{count_lose}把")
elif count_win > count_lose:
    print(f"你贏了{count_win}把,輸了{count_lose}把,平手{count_peace}把")
else:
    print(f"你輸了{count_lose}把,贏{count_win}把,平手{count_peace}把")
#print(name + " 出了: " + player_hand + ", 電腦出了: " + computer_hand )
print("==============================")
print("感謝你玩剪刀石頭布")
