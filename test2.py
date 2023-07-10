import random

prizes = []
prizes.extend(['1'])
prizes.extend(['2'])
prizes.extend(['3'])
prizes.extend(['4'])
prizes.extend(['5'])
prizes.extend(['nope'])

counts = {"1":1, "2":1, "3":3, "4":5, "5":9}

probabilities = [0.001, 0.03, 0.13, 0.18, 0.25, 0.409]

def draw_prize():
    prize_total = 19
    while prize_total!=0:
        go = input(f"目前還有{counts}")
        if go!="y":
            break
        prize = random.choices(prizes, weights=probabilities)[0]
        if prize != "nope":
            if counts[prize] == 0:
                print("沒抽到")
                continue
            counts[prize]-=1
            prize_total-=1
            print(f"抽到{prize}獎")
            print(counts)
        else:
            print("沒中")
    print("all none")

# 執行抽獎
draw_prize()