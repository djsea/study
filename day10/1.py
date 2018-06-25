#函数定义
def mylen(s1):
    length = 0
    for i in s1:
        length +=1
    return length

str_len = mylen("hello world")
print(str_len)