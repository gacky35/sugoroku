import random

def go(i, list):
    temp = list[i]
    i += temp
    print("move" + str(temp))
    print(i)
    return i

def back(i, list):
    temp = list[i]
    i += temp
    print("back" + str(temp))
    print(i)
    return i

def main():
    list = ["Start!!", 1, 0, 0, 5, 0, -3, 0, -2, 0, 0, 3, 0, 0, 1, 0, -4, 0, 0, 0, -2, 0, 0, 0, 3, 0, 1, 0, 0, 0, -6, 0, 0, -3, 0, 0, 2, 0, 0, 4, 0, 0, -2, 0, -3, 0, 1, 0, 2, -5, 0, -1, 4, -6, 0, "Goal!!"]
    i = 0
    j = 0
    k = 0
    t = 0

    print(list[0])

    while i < 55 and j < 55:
        if k % 2 == 0:
            input("Player1's turn. Press enter key")
            for n in range(0, 100000):
                t = random.randint(1, 6)
            i += t
            print("player1 : " + str(i))
            if i < 55 and list[i] > 0:
                i = go(i, list)
            elif i < 55 and list[i] < 0:
                i = back(i, list)
        else:
            input("Player2's turn. Press enter key")
            for n in range(0, 400000):
                t  = random.randint(1, 6)
            j += t
            print("player2 : " +str(j))
            if j < 55 and list[j] > 0:
                j = go(j, list)
            elif j < 55 and list[j] < 0:
                j = back(j, list)
        k += 1

    if i >= 55:
        print(list[55])
        print("winner player1")
    elif j >= 55:
        print(list[55])
        print("winner player2")
    print("Game is Over")

main()
