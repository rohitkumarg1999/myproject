                #  >>> DECORATOR <<< #
#Decorators are very powerful and useful tool in Python since it allows programmers to modify
#the behavior of function or class
# this is direct way to used decorator
#method1

def modified_fun(func):
    def inner():
        print("this is modified function")
        func()
    return inner
def fun1():
    print("this is base funtion")
fun1=modified_fun(fun1)
fun1()
'''

#method2
#* use of @withfunction
# def decor_fun(func):
#     def inner(*args):#for parameter
#         print("this is modified one")
#         func(*args)
#     return inner
# @decor_fun
# def fun1(a,b):
#    print("this  is base funtion ")
#    print(a*b)
# fun1(4,5)
# docorator with parameter
def decorators(*args, **kwargs): 
    def inner(func): 
        ''' 
           do operations with func 
        '''
        return func 
    return inner #this is the fun_obj mentioned in the above content 
  
@decorators(params) 
def func(): 
# 
#
#
"""
    function implementation
"""

####################################################### >>> generator <<< ############

# A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# #*note :generator implemented with yeild statement,
# #1-The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its
# #states and later continues from there on successive calls.
#  #>>code
# # A simple generator function
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n

#     n += 1
#     print('This is printed second')
#     yield n

#     n += 1
#     print('This is printed at last')
#     yield n
# a=my_gen()
# print(next(a))#1
# print(next(a))#2
# print(next(a))#3
# #* list have small range to to calculate for big range gennerator is used
# g=(x*x for x in range(100000000000) ) #it work
# #*generator used to return tuple object
def fibonacchi(num):
  x,y=0,1
  for i in range(num):
    x,y=y,x+y
    yield x
  
  
      
fb=fibonacchi(20)
print(next(fb))
print(next(fb))
print(next(fb))






       
