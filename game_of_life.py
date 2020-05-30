import random
import time
import os

def draw(main_list):
    time.sleep(0.0625)
    os.system("cls")
    for i in range(len(main_list)):
        print("".join(main_list[i]))


def how_nei(lis, i, j, sign, x, y):
    count = 0
    if j != y - 1 and lis[i][j + 1] == sign:
        count += 1
    if j != 0 and lis[i][j - 1] == sign:
        count += 1
    if i != x - 1 and lis[i + 1][j] == sign:
        count += 1
    if i != 0  and lis[i - 1][j] == sign:
        count += 1
    if i != 0 and j != 0 and lis[i - 1][j - 1] == sign:
        count += 1
    if i != 0 and j != y - 1 and lis[i - 1][j + 1] == sign:
        count += 1
    if i != x -1 and j != 0 and lis[i + 1][j - 1] == sign:
        count += 1
    if i != x - 1 and j != y - 1 and lis[i + 1][j + 1] == sign:
        count += 1
    return count

def main():

    x = 50
    y = 50
    chance = 8
    main = list()
    nmain = list()
    alive = "#"
    dead = " "

    #TODO : the first painting
    for i in range(x):
        main.append(list())
        for j in range(y):
            if j // chance == j / chance:
                pos_place = random.randrange(j, j + chance)
            if j == pos_place:
                main[i] += alive
            else:
                main[i] += dead
    nmain = main.copy()
    draw(nmain)
    
    #TODO : game main loop
    while 1:
        for i in range(x):
            for j in range(y):
                if 2 > how_nei(main, i, j, alive, x, y) or how_nei(main, i, j, alive, x, y) > 3:
                    nmain[i][j] = dead
                if how_nei(main, i, j, alive, x, y) == 3 and main[i][j] == dead:
                    nmain[i][j] = alive
        draw(nmain)
        main = nmain.copy()

if __name__ == '__main__':
    main()
