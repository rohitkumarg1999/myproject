#there are so many built in exception those are raise in program
#exceptions are raised when errors occur at runtime

#syntax
'''
try:
    statement1
    statement2
    statement3
except:
    statemnt4
else:         #it is optional to use else or not
    stsement6
finally:      #its is also optonal to use  but it paly very important role

    ststement5
'''
###example1
'''
import sys
try:
    a=10
    b=int(input("enter num"))
    result=a/b
except:
    print("oops! ",sys.exc_info()[0],"occured") #this sys.exc_info give the reason of exception
'''
#>>another method
#*note : a try block can have more than one exception block
'''
import sys
try:
    a=10
    b=int(input("enter num"))
    result=a/b
except Exception as e:
    print("oops! ",e.__doc__,"occured")
    print("oops! ",e.__class__,"occured")
'''
#error free execution f try block ,so we use else ,further error in else block is not handaled
'''
try:
    num = int(input("Enter a number: "))
    assert num % 2==0 
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
'''
      ## >>> raise exception <<< ##
#* manually raising of the exception we use raise keyword for this
try:
    val=int(input("enter any positive number"))
    if val<0:
        raise ValueError("this is not a positive number")
except ValueError as e:
    print(e)


