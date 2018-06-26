# f = open('a.txt')
#
# g = (line.strip() for line in f)
# for line in g:
#     print(line)
# else:
#     f.close()


try:
    f = open('a.txt')
    g = (line.strip() for line in f)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    # f.close(
    print("没有了")
