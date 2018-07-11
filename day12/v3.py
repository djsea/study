import time
FLAGE = True

def timer_out(flag):
    def timmer(func):
        def inner(*args, **kwargs):
            if flag:
                start = time.time()
                ret = func(*args, **kwargs)
                end = time.time()
                print(end-start)
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret
        return inner
    return timmer


@timer_out(FLAGE)
def wahaha():
    time.sleep(0.1)
    print('wahahaha')


@timer_out(FLAGE)
def heigaga():
    time.sleep(0.2)
    print('heigaga')


wahaha()
heigaga()