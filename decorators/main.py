from datetime import datetime

# task 1 and 3
def showargs(func):
    def myinner(*args, **kwargs):
        if args:
            print("Отримані позиційні аргументи: ")
            for i in args:
                print(i)
        if kwargs:
            print("Отримані іменовані аргументи: ")
            for k, v in kwargs.items():
                print(f"{k} : {v}")
        else:
            print("Аргументи відсутні")
        return func(*args)
    return myinner

# task 2
def showtime(func):
    def myinner():
        print(datetime.now())
        return func
    return myinner


@showargs
def myfunc(x,b,k="hello world"):
    print(x + " " + b + " " + k)

@showargs
@showtime
def helloworld():
    print("Hello world")

myfunc("world","hello",k="str")

helloworld()