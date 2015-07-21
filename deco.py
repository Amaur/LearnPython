def repeater(old_function):
    def new_function(*args,**kwds):
        return 2*old_function(*args, **kwds)

    return new_function



@repeater
def multiply(num1, num2):
    return (num1*num2)


print(multiply(2,3))