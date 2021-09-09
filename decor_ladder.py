
def mod_decor(func):
    def inner(*args):
        print("hello this is mod_decor funtion")
        func(*args)
        
    return inner

def decor_fun(func):
    def modify_fun(*args):
        print("this is decor funtion funtion")
        func(*args)
    return modify_fun



@mod_decor
@decor_fun
def fun1(a,b):
    print("i am fun1")
    x=a**b
    print("this is the square of the paramer: {}".format(x))
fun1(10,2)
