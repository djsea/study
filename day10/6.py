def f1():
    print("in f1")
    def f2():
        print("in f2")

    f2()
f1()


def f1():
    def f2():
        def f3():
            print("in f3")

        print("in f2")
        f3()

    print("in f1")
    f2()


f1()