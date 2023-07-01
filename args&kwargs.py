# args
def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun("Hello", "My", "Name", "Is", "This")


class car:
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        self.speed = args[0]
        self.color = args[1]


audi = car(200, "red")
bmw = car(250, "black")
mb = car(190, "white")
print(audi.color)
print(bmw.speed)

# kwargs


def myFunc(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFunc("Hi", first="Name", mid="is", last="this")


class Car:
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs["s"]
        self.color = kwargs["c"]


audi = Car(s=200, c="red")
bmw = Car(s=250, c="black")
mb = Car(s=190, c="white")
print(audi.color)
print(bmw.speed)


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


myFun("temp", "for", "function", first="newtemp", mid="for", last="function")
