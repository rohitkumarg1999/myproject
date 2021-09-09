############ INBULIT  IMPORTANT FUNTION IN PYTHON ##############
                             # >>> MAP  FUNTION <<< #
map() function returns a map object(which is an iterator) of the results after applying the given
function to each item of a given iterable (list, tuple etc.
map(fun, iter)
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

x=list(map(int,input("enter the number").split()))  # taking multipe input in one line
def multiply_by_two(x):
    return 2*x
y=map(multiply_by_two ,[1,2,3,4])

                   # >>> LAMBDA FUNTION <<< #
x=lambda argument:expression
x=lambda n:n**2
print(x(5)) #x is behave like a funtion
#lambda funtion also can be used with the map funtion
x=map(lambda x:x**2 ,range(20))

               ###### >>> Reduce funtion <<< #####
reduce funtion need to import functools
syntax of functools
import functools
list1=[2,5,8,3,9]
print(functools.reduce(lambda a,b :a+b,list1))

              ###### >>> filter function <<<<  ######
filter funtion used in case when you want to filter the
some value from the iterable
   #sysntax
filter(function,iterable)
list1=[9,2,5,12,14,23]
x=filter(lambda x:True if x%2==0 else False,list1)
print(list(x))

        ########## >>> zip funtion  <<< ##############
zip funtion is used to convert two list into dictionary
list1=[1,2,3,4]
list2=["rohit","mohit","amit","shubham"]
x=zip(list1,list2)



                                           
                                           
                                           
                                           
                                           
