import random

squares = []
r_num = 0
num_list = [] #使用済みリスト
num_required = [] #必須リスト
num_candidate = [] #候補リスト
num_list_area = [] #エリア内の使用済みリスト
tmr = 0
roop_flag = "roopなし"


# 全マス目作成(行単位)
for y in range(9):
    squares.append([0]*9)

# 数字作成関数
def create_num(num_list, roop_count = 1):
    global r_num, roop_flag
    #roop_count = 1
    #print("roop_flag" + str(print(roop_flag)))

    while True:

        r_num = random.randint(1, 9)
        # リスト化から1文字ずつはき出して、ぶつけるやり方
##        flag_append = "OK"
##        for num_ind in num_list:
##            if num_ind == r_num:
##                flag_append = "NG"
##
##        if flag_append == "OK":
##            num_list.append(r_num)
##            return r_num

        if r_num not in num_list:
            num_list.append(r_num)
            return r_num

        roop_count += 1
        # テスト用
##        print("roop_count:"+str(roop_count))
        if roop_count >= 100:
            roop_flag = "roopが発生した"
            #print(roop_flag)
            return roop_flag


def num_area_middle_line(tmr):

    # 2行(列)目の作成
     # 左のエリア
    if tmr == 0:
        num_list = [] # 初期化
    ##    テスト用
    ##    print("num_list：" + str(num_list))
        for x in range(3):
            num_list.append(squares[0][x])
    ##    テスト用
    ##    print("リスト：" + str(num_list))
        for x in range(3):
            create_num(num_list)
            squares[1][x] = r_num

     # 真ん中のエリア
    num_list = [] # 初期化
    num_required = [] # 初期化
    num_candidate = [] # 初期化

##    テスト用
##    print("num_list：" + str(num_list))
##    print("num_required：" + str(num_required))
##    print("num_candidate：" + str(num_candidate))
##    squares[0][6] = 7
##    squares[0][7] = 8
##    squares[0][8] = 9
##    squares[1][0] = 7
##    squares[1][1] = 8
##    squares[1][2] = 9

      # 必須リスト作成
    for x in range(6, 9):
        if tmr == 0:
            num_required.append(squares[0][x])
        elif tmr == 1:
            num_required.append(squares[x][0])
##    テスト用
##    print("必須(候補)：" + str(num_required))

    for x in range(3):
        try:
            if tmr == 0:
                num_required.remove(squares[1][x])
            elif tmr == 1:
                num_required.remove(squares[x][1])
        except ValueError:
            pass
    num_candidate += num_required
##    テスト用
##    print("必須：" + str(num_required))
##    print("必須数：" + str(len(num_required)))
##    print("候補：" + str(num_candidate))

      # 数字作成
    if len(num_required) < 3:
        num_list += num_required

        for x in range(3):
            if tmr == 0:
                num_list.append(squares[1][x])
            elif tmr == 1:
                num_list.append(squares[x][1])

        for x in range(3, 6):
            if tmr == 0:
                num_list.append(squares[0][x])
            elif tmr == 1:
                num_list.append(squares[x][0])
##    テスト用
##        print("リスト：" + str(num_list))

        for a in range(3-len(num_required)):
            create_num(num_list)
            num_candidate.append(r_num)
      # 数字の入力
    random.shuffle(num_candidate)
    x = 3
    for num_ind in num_candidate:
        if tmr == 0:
            squares[1][x] = num_ind
        elif tmr == 1:
            squares[x][1] = num_ind
        x += 1

     # 右もしくは最下のエリア
    num_list = [] # 初期化
    for x in range(6):
        if tmr == 0:
            num_list.append(squares[1][x])
        elif tmr == 1:
            num_list.append(squares[x][1])
    for x in range(6, 9):
        create_num(num_list)
        if tmr == 0:
            squares[1][x] = r_num
        elif tmr == 1:
            squares[x][1] = r_num

def num_area_last_line(tmr):
    if tmr == 0:
        a, b, c = 0, 3, 3
    elif tmr == 1:
        a, b, c = 3, 6, 2
    for i in range(c):
        num_list = [] # 初期化
##    テスト用
##        print("リストの初期化；" + str(num_list))
##        print("a:"+ str(a))
##        print("b:"+ str(b))

        for y in range(2):
            for x in range(a, b):
                if tmr == 0:
                    num_list.append(squares[y][x])
                elif tmr == 1:
                    num_list.append(squares[x][y])
        for x in range(a, b):
            create_num(num_list)
            if tmr == 0:
                squares[2][x] = r_num
            elif tmr == 1:
                squares[x][2] = r_num
        a += 3
        b += 3
##    テスト用
##        print("+=3を通過")



def create_top_of_area():
    # 1行目の作成
    num_list = [] # 初期化

    for x in range(9):
        create_num(num_list)
        squares[0][x] = r_num

    #--------------------------------------------
    # 2行目の作成
    num_area_middle_line(tmr=0)

    #--------------------------------------------
    # 3行目の作成
    num_area_last_line(tmr=0)
    #return squares #不要

def create_left_of_area():
    # 1列目の作成
    num_list = [] # 初期化
    for y in range(3):
        num_list.append(squares[y][0])
##    テスト用
##    print("2つめ：" + str(num_list))

    for y in range(3, 9):
        create_num(num_list)
        squares[y][0] = r_num

    #--------------------------------------------
    # 2列目の作成
    num_area_middle_line(tmr=1)

    #--------------------------------------------
    # 3列目の作成
    num_area_last_line(tmr=1)

def create_the_rest_of_area():
    tmr2 = 0
    for i in range(2):
        tmr = 0
        for i in range(2):
            b = 3 # エリア内の上段のy
            if tmr2 == 1:
                b = 6
            num_list_area = [] # 初期化
            for i in range(3):
                a = 3 # エリア内の上段のx
                if tmr == 1:
                    a = 6
                for i in range(3):
                    num_list = [] # 初期化
                    num_list += num_list_area
                    # テスト用
##                    print("num_list_area:"+ str(num_list_area))

                    for x in range(a):
                        num_list.append(squares[b][x])

                    for y in range(b):
                        num_list.append(squares[y][a])

                    create_num(num_list)
                    squares[b][a] = r_num
                    num_list_area.append(r_num)
                    a += 1
                b += 1
            tmr += 1
        tmr2 += 1

roop_flag1 = 0
roop_flag2 = 0
roop_flag3 = 0
while True:
##    global roop_flag
##    global roop_flag3

    roop_flag = "roopなし"
    create_top_of_area()
    #print("roop_flag1:"+roop_flag)
    if roop_flag == "roopが発生した":
        roop_flag1 += 1

    create_left_of_area()
    #print("roop_flag2:"+roop_flag)
    if roop_flag == "roopが発生した":
        roop_flag2 += 1

    create_the_rest_of_area()
    #print("roop_flag3:"+roop_flag)
    if roop_flag == "roopが発生した":
        roop_flag3 += 1
##    if roop_flag == "roopなし":
##        break
    if roop_flag == "roopなし":
        break


##    テスト用
##    print("リスト：" + str(num_list))
print ("総行："+str(len(squares)))
print("roop_flag1:"+str(roop_flag1))
print("roop_flag2:"+str(roop_flag2))
print("roop_flag3:"+str(roop_flag3))
for y in range(len(squares)):
    print (squares[y])

#print (num_list)