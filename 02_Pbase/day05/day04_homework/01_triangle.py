# 1. 用while语句实现打印三角形，输入一个整数，表示三角形的宽度和高度，打印出相应的三角形;
#  如:
#   请输入三角形宽度: 4
#   打印结果如下:
#   *
#   **
#   ***
#   ****
#   2. 再打印:
#      *
#     **
#    ***
#   ****
#   3. 再打印:
#   ****
#    ***
#     **
#      *
#   4. 再打印:
#   ****
#   ***
#   **
#   *



n = int(input("请输入三角形宽度: "))

#   2. 再打印这样的三角形:
#      *
#     **
#    ***
#   ****
i = 1  # 代表星号的个数
while i <= n:
    # 在此处打印一行
    print(' ' * (n - i) + "*" * i)
    i += 1

print('---------------------')
#   3. 再打印:
#   ****
#    ***
#     **
#      *
i = 0
while i < n:
    # 用变量i的值来算一行的空格和星的个数
    print(' ' * i + '*' * (n - i))
    i += 1
print("=======================")
#   4. 再打印:
#   ****
#   ***
#   **
#   *
i = n
while i > 0:
    print('*' * i)
    i -= 1