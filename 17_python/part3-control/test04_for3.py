# 구구단
index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in index[1:]:     # i에 2~9 까지 넣어줌
    for j in index:     # 1~9 까지 j에 넣어줌
        print(str(i) + " * " + str(j) + " = " + str(i*j))
    print()     # 한번의 루프를 돌때마다 줄바꿈

"""
2 * 1 = 2
2 * 2 = 4
....
9 * 8 = 72
9 * 9 = 81
"""
