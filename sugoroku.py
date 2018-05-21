import random

def disp(list):
    for i in range(5):
        if i % 2 == 0:
            for j in range(11):
                if j == 10:
                    print(list[i * 11 + j][2])
                else:
                    print(list[i * 11 + j][2], end='')
        elif i % 2 == 1:
            for j in range(10, -1, -1):
                if j == 0:
                    print(list[i * 11 + j][2])
                else:
                    print(list[i * 11 + j][2], end='')

def reset(list, i, t, k):
    if "12" not in list[i-t][2]:
        list[i-t][2] = "□ "
    elif k % 2 == 0:
        list[i-t][2] = " 2"
    elif k % 2 == 1:
        list[i-t][2] = "1 "

def change(list, i, k):
    if k % 2 == 0:
        if i >= 54:
            list[54][2] = "1 "
        elif list[i][2] == "□ ":
            list[i][2] = "1 "
        else:
            list[i][2] = "12"
    else:
        if i >=54:
            list[54][2] = " 2"
        elif list[i][2] == "□ ":
            list[i][2] = " 2"
        else:
            list[i][2] = "12"

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
    list = [["Start!!", 0, "□ "], ["自販機の下に500円落ちていた、タクシーで移動。1マス進む", 1, "□ "], ["0", 0, "□ "], ["0", 0, "□ "], ["進む", 5, "□ "], ["一回休み", 0, "□ "], ["階段から転げ落ちた話を上司にしたら、上司が階段から落ちた。3マス戻る", -3, "□ "], ["0", 0, "□ "], ["戻る", -2, "□ "], ["ふりだし", 0, "□ "], ["0", 0, "□ "], ["進む", 3, "□ "], ["ふりだし", 0, "□ "], ["0", 0, "□ "], ["進む", 1, "□ "], ["0", 0, "□ "], ["戻る", -4, "□ "], ["0", 0, "□ "], ["不良に絡まれた。一回休み", 0, "□ "], ["0", 0, "□ "], ["馬を見つけた。2マス戻る", -2, "□ "], ["0", 0, "□ "], ["ふりだし", 0, "□ "], ["0", 0, "□ "], ["進む", 3, "□ "], ["0", 0, "□ "], ["進む", 1, "□ "], ["0", 0, "□ "], ["0", 0, "□ "], ["0", 0, "□ "], ["戻る", -6, "□ "], ["0", 0, "□ "], ["0", 0, "□ "], ["戻る", -3, "□ "], ["タケコプターを拾った、交番に届けるためにふりだしに戻る。", 0, "□ "], ["0", 0, "□ "], ["進む", 2, "□ "], ["0", 0, "□ "], ["0", 0, "□ "], ["進む", 4, "□ "], ["0", 0, "□ "], ["0", 0, "□ "], ["戻る", -2, "□ "], ["0", 0, "□ "], ["戻る", -3, "□ "], ["0", 0, "□ "], ["進む", 1, "□ "], ["ふりだし", 0, "□ "], ["進む", 2, "□ "], ["戻る", -5, "□ "], ["0", 0, "□ "], ["戻る", -1, "□ "], ["進む", 4, "□ "], ["戻る", -6, "□ "], ["Goal!!", 0, "□ "]]
    i = 0
    j = 0
    k = 0
    t = 0

    disp(list)
    print(list[0][0])

    while i < 54 and j < 54:
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
                if i < 54:
                    if  "ふりだし" in list[i][0]:
                        reset(list, i, t, k)
                        i = huridashi(i, list)
                        change(list, i, k)
                    elif  "進む" in list[i][0]:
                        reset(list, i, t, k)
                        i = go(i, list)
                        change(list, i, k)
                    elif "戻る" in list[i][0]:
                        reset(list, i, t, k)
                        i = back(i, list)
                        change(list, i, k)
                    elif "休み" in list[i][0]:
                        reset(list, i, t, k)
                        change(list, i, k)
                        i = rest(i, list)
                    else:
                        reset(list, i, t, k)
                        change(list, i, k)
        else:
            if j < 0:
                input("Player2's turn skip. Press enter key")
                j = -j
            else:
                input("Player2's turn. Press enter key")
                for n in range(0, 250000):
                    t  = random.randint(1, 6)
                j += t
                print("Player2 : " +str(j))
                if j < 54:
                    if "ふりだし" in list[j][0]:
                        reset(list, j, t, k)
                        j = huridashi(j, list)
                        change(list, j, k)
                    elif "進む" in list[j][0]:
                        reset(list, j, t, k)
                        j = go(j, list)
                        change(list, j, k)
                    elif "戻る" in list[j][0]:
                        reset(list, j, t, k)
                        j = back(j, list)
                        change(list, j, k)
                    elif "休み" in list[j][0]:
                        reset(list, j, t, k)
                        change(list, j, k)
                        j = rest(j, list)
                    else:
                        reset(list, j, t, k)
                        change(list, j, k)
        k += 1
        disp(list)

    if i >= 54:
        print(list[54][0])
        print("winner player1")
    elif j >= 54:
        print(list[54][0])
        print("winner player2")
    print("Game is Over")

main()
