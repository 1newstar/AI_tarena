class ClassA():
    def __init__(self):
        print("object born, id:%s" % str(hex(id(self))))

    def __del__(self):
        print("object del, id:%s" % str(hex(id(self))))

def f1():
    c1 = ClassA()
    del c1


f1()

# 注释:
# c1=ClassA()会创建一个对象，放在0x7f3e512ed6a0内存中，c1变量指向这个内存，
# 这时候这个内存的引用计数是1
# del c1后，c1变量不再指向0x7f3e512ed6a0内存，所以这块内存的引用计数减一，等于0，
# 所以就销毁了这个对象，然后释放内存。

# 一 导致引用计数+1的情况
# 1.对象被创建，例如a=23
# 2.对象被引用，例如b=a
# 3.对象被作为参数，传入到一个函数中，例如func(a)
# 4.对象作为一个元素，存储在容器中，例如list1=[a,a]

# 二 导致引用计数-1的情况
# 1.对象的别名被显式销毁，例如del a
# 2.对象的别名被赋予新的对象，例如a=24
# 3.一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
# 4.对象所在的容器被销毁，或从容器中删除对象

# 2.循环引用导致内存泄露
# def f2():
#     c1 = ClassA()
#     c2 = ClassA()
#     c1.t = c2
#     c2.t = c1
#     print(hex(id(c1.t)))
#     print(hex(id(c2.t)))    
#     del c1
#     del c2


# f2()

# 注释:
# 创建了c1，c2后，0x7f2ff92b24e0（c1对应的内存，记为内存1）,0x7f2ff92b2518
# （c2对应的内存，记为内存2）这两块内存的引用计数都是1，执行c1.t=c2和c2.t=c1后，
# 这两块内存的引用计数变成2,在del c1后，内存1的对象的引用计数变为1，由于不是为0，
# 所以内存1的对象不会被销毁，所以内存2的对象的引用数依然是2，在del c2后，同理，
# 内存1的对象，内存2的对象的引用数都是1。虽然它们两个的对象都是可以被销毁的，
# 但是由于循环引用，导致垃圾回收器都不会回收它们，所以就会导致内存泄露。


# 3.垃圾回收
# import gc 

# import time

# def f3():
#     print(gc.collect()) # 调用gc.collect()方法,触发垃圾回收,此时为0
#     c1 = ClassA()
#     c2 = ClassA()
#     c1.t = c2
#     c2.t = c1
#     del c1
#     del c2
#     print(gc.garbage)   # 垃圾回收列表
#     print(gc.collect()) # 显示执行垃圾回收  4
#     print(gc.garbage)   # 垃圾回收列表
#     print(gc.collect()) # 0
#     time.sleep(10)


# if __name__ == "__main__":
#     # gc.set_debug(gc.DEBUG_LEAK) # 设置gc模块的日志
#     f3()

# 注释:
# 1.垃圾回收后的对象会放在gc.garbage列表里面
# 2.gc.collect()会返回不可达的对象数目，4等于两个对象以及它们对应的dict
# 有三种情况会触发垃圾回收：
# 1.调用gc.collect(),
# 2.当gc模块的计数器达到阀值的时候。
# 3.程序退出的时候

