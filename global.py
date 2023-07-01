arr = [10, 20, 30]


def fun():
    global arr
    arr = [20, 30, 40]


print("'arr' list before executing fun():", arr)
fun()
print("'arr' list after executing fun():", arr)


def add():
    x = 15

    def change():
        global x
        x = 20

    print("Before making changing: ", x)
    print("Making change")
    change()
    print("After making change: ", x)


add()
print("value of x", x)
