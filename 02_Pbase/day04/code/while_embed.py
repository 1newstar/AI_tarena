# while 嵌套示例:
#   打印1~20的整数,打印在一行显示，每个数字之间用一个空格分隔:
#     1 2 3 4 5 6 7 .... 18 19 20
#   打印10行

j = 1
while j <= 10:
    # print('1 2 3 4 5 6 7 8 ... 18 19 20')
    i = 1
    while i <= 20:
        print(i, end=' ')
        i += 1
    else:
        print()
    j += 1

