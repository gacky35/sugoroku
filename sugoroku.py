import random

def huridashi(i, list):
    print(list[i][0])
    temp = list[i][1]
    i = temp
    print(i)
    return i

def go(i, list):
    print(list[i][0])
    temp = list[i][1]
    i += temp
    print(i)
    return i

def back(i, list):
    print(list[i][0])
    temp = list[i][1]
    i += temp
    print(i)
    return i

def rest(i, list):
    print(list[i][0])
    i = -i
    return i

def main():
    list = [["Start!!", 0], ["自販機の下に500円落ちていた、タクシーで移動。1マス進む", 1], ["0", 0], ["0", 0], ["進む", 5], ["一回休み", 0], ["階段から転げ落ちた話を上司にしたら、上司が階段から落ちた。3マス戻る", -3], ["0", 0], ["戻る", -2], ["ふりだし", 0], ["0", 0], ["進む", 3], ["ふりだし", 0], ["0", 0], ["進む", 1], ["0", 0], ["戻る", -4], ["0", 0], ["不良に絡まれた。一回休み", 0], ["0", 0], ["馬を見つけた。2マス戻る", -2], ["0", 0], ["ふりだし", 0], ["0", 0], ["進む", 3], ["0", 0], ["進む", 1], ["0", 0], ["0", 0], ["0", 0], ["戻る", -6], ["0", 0], ["0", 0], ["戻る", -3], ["タケコプターを拾った、交番に届けるためにふりだしに戻る。", 0], ["0", 0], ["進む", 2], ["0", 0], ["0", 0], ["進む", 4], ["0", 0], ["0", 0], ["戻る", -2], ["0", 0], ["戻る", -3], ["0", 0], ["進む", 1], ["ふりだし", 0], ["進む", 2], ["戻る", -5], ["0", 0], ["戻る", -1], ["進む", 4], ["戻る", -6], ["0", 0], ["Goal!!", 0]]
    i = 0
    j = 0
    k = 0
    t = 0

    print(list[0][0])

    while i < 55 and j < 55:
        if k % 2 == 0:
            if i < 0:
                input("Player1's turn skip. Press enter key")
                i = -i
            else:
                input("Player1's turn. Press enter key")
                for n in range(0, 100000):
                    t = random.randint(1, 6)
                i += t
                print("player1 : " + str(i))
                if i < 55:
                    if  "ふりだし" in list[i][0]:
                        i = huridashi(i, list)
                    elif  "進む" in list[i][0]:
                        i = go(i, list)
                    elif "戻る" in list[i][0]:
                        i = back(i, list)
                    elif "休み" in list[i][0]:
                        i = rest(i, list)
        else:
            if j < 0:
                input("Player2's turn skip. Press enter key")
                j = -j
            else:
                input("Player2's turn. Press enter key")
                for n in range(0, 250000):
                    t  = random.randint(1, 6)
                j += t
                print("player2 : " +str(j))
                if j < 55:
                    if "ふりだし" in list[j][0]:
                        j = huridashi(j, list)
                    elif "進む" in list[j][0]:
                        j = go(j, list)
                    elif "戻る" in list[j][0]:
                        j = back(j, list)
                    elif "休み" in list[j][0]:
                        j = rest(j, list)
        k += 1

    if i >= 55:
        print(list[55][0])
        print("winner player1")
    elif j >= 55:
        print(list[55][0])
        print("winner player2")
    print("Game is Over")

main()
