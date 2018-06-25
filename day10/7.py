import time
# def timer(func):
#     def inner():
#         start = time.time()
#         func()
#         print(time.time() - start)
#     return inner
#
# @timer   #==> func1 = timer(func1)
# def func1():
#     print('in func1')
#
#
# func1()

def timer(func):
    def inner(a):
        start = time.time()
        func(a)
        print(time.time() - start)
    return inner

@timer
def func1(a):
    print(a)

func1(1)

# 装饰器——带参数的装饰器