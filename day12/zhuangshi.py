def wrapper(func):
    def inner(*args, **kwargs):
        print("在被装饰的函数执行之前的事")
        ret = func(*args, **kwargs)
        print("在被装饰的函数执行之后的事")
        return ret
    return inner


@wrapper
def holiday(day):
    print("全体放假%s天" %day)
    return "好开心"

ret = holiday(3)
print(ret)