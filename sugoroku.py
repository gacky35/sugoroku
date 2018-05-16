import random

list = ["Start!!", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Goal!!"]
i = 0
j = 0
k = 0
t = 0

while i < 55 and j < 55:
    if k % 2 == 0:
        input("Player1's turn. Press enter key")
        if i < 55:
            print("player1 : " + str(i))
        for n in range(0, 100000):
            t = random.randint(1, 6)
        i += t
    else:
        input("Player2's turn. Press enter key")
        if i < 55:
            print("player2 : " +str(j))
        for n in range(0, 100000):
            t  = random.randint(1, 6)
        j += t
    k += 1

if i >= 55:
    print(list[55])
    print("winner player1")
elif j >= 55:
    print(list[55])
    print("winner player2")
print("Game is Over")
