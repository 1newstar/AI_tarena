# 1. 有一只小猴子，摘了很多桃.
#    第一天吃了全部桃子的一半，感觉不饱又吃了一个
#    第二天吃了剩下桃子的一半，感觉不饱又吃了一个
#    .... 以此类推
#    到第十天，发现只剩下一个了
#   请问第一天摘了多少个桃?

# 第十天
x = 1
# # 第九天
# x = (x + 1) * 2
# # 第八天
# x = (x + 1) * 2
# # ...
# x = (x + 1) * 2

# x = (x + 1) * 2
# x = (x + 1) * 2
# x = (x + 1) * 2
# x = (x + 1) * 2
# x = (x + 1) * 2
# x = (x + 1) * 2
for _ in range(9, 0, -1):
    x = (x + 1) * 2

print("第一天小猴子摘了", x, "个桃子")



