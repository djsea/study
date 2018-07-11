from functools import wraps
def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("在被装饰的函数执行之前的事")
        ret = func(*args, **kwargs)
        print("在被装饰的函数执行之后的事")
        return ret
    return inner


@wrapper
def holiday(day):
    '''---放假通知---'''
    print("全体放假%s天" %day)
    return "好开心"
print(holiday.__name__)
print(holiday.__doc__)
ret = holiday(3)
print(ret)