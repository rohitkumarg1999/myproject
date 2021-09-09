"""
In python there are Five standard data type '
number
list
tuple
dictionary
string

#number
int x=1
float y=2.1
complex z=2+3j
long any long number"""

##################################  string   #######################
'''
single quote string ' '
double quote string  " "
triple quote string  """ """
str1="rohit kumar gautam"
print(str1[1:10]) #it will give the substring or you can say slicing
print(str[-5:-2])#-1 is the index of last element of string
                      ######   funtion    ######
len(str1) #calculate lenght
str1.strip() #remove any white sapace begining of the string
str1.lower() #convert the string in lowercase
str1.upper() #convert the string in uppercase
str1.title() #convert the first letter of each word the string
str1.split() # it return the list of ecah world
str1.swapcase() #it convert the smallcase to uppper and upper case to smallcases
str1.capitalize()# it convertthe first world first letter captal
print(' '.join(list1)) #it will join ecah elemnt of list with the gap and return a string out of it
'''



                 # use of format
print("my name is {0} and i am a {1} engineer".format("rohit","sofware"))
"""

#############################################################   LIST    ################
'''
list element can have any data type ,it is mutable and iterable
and so many inbultfuntion in list,index always start from zero
list can be multidimentional
list allow assignment
list is iterable
list support slicing


operation
if list1 and list2 is there it support
1-list3=list1+list2 it extend the value and add both lists
2-len(list1)
3-list1*3 #repitition
4-membership operation: 2 in [1,2,3] #true




list1=[5,2,4,7,8,1,9]
print(list1[2]) #output 4
print(list1[1:]) # [2,4,7,8,9]
                     #########built in funtion and methods############
#functions
cmp(list1,list2)
len(list1)
max(list1)
min(list1)
list(tuple)

#methods
list1.append(obj)
list1.extend(obj)
list1.coount(obj)
list1.index(obj)
list1.insert(index,obj)
list1.pop()
list1.remove(obj)
list1.sort()
list1.reverse()
list1.clear() #it will completely clean the list

   ###########shalow and deepcopy concept####
import copy
list1=[1,3,5,6,2]
list2=copy.copy(list1) #shalow copy
list2=copy.deepcopy(list1)  #deepcopy
'''

#############################################################   Tuple #################
Tuple is same as list it is immutable and orderd
it does not support assignment
represente by ()

######################################################### dictionary  #################################
'''
dictionary is the datatype having key and value pairs
dictionary is reprenst by this way {key:values,key:value}
empty dictionary=dict1=dict()
dictionay is iterable

                  ######### dict iteration  ######
dict1={1:"rohit",2:"mohit",3:"amit"}
for x in dict1:  # by default it will give keys
  print(x)
for x in dict1.values(): #  it will iterates value
  print(x)
for x ,y in dict1.items(): #  it will iterates x as key and y as values
  print(x,y)
  it is accesseble through
dict1[1] #  output will be :rohit
dictionary also support assignment
dict1[4]="shobhit"
    ################methods in dictionary ##############
dict1.clear() #it will remove all element from the dictionary
dict1.copy()  #it copy the dictionary
dict1.get(key) #it will gives the value
dict1.pop(key)    # it will remove specific key and value
dict1.popitem() #it will remove last inserted key value pairs
dict1.update({key:value})
'''


############################################ set ######################################################
'''
A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.
setis represent set1={1,5}
set is iterable
it avoid the duplicate entry
set1=set() #empty set
iteration is same like list  #for x in set1:
always data in sort way
              ########funtion and methods###############
myset.add(element)
set1.intersection(set2)
set1.difference(set2)
set1.union(set2)
set1.clear()
set.remove(elemnt)
set.discard(element)#it thrown an error if the elemt is not present in set


set1.isdisjoint(set2)# it return true or false

'''
##################################################### list comprrehension ###############################
'''
l1=[x for x in range(1,20)] #it is list of 1 to 19
l2=[x*x for x in range(1,100) if x*x in range(1,20)] # it contain if within the compression it will give only square  value within the range
l3=[x for x in range(1,100) if math.sqrt(x) in range(1,100)] #it contain if within the compression it will give only square  value within the range
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]#More then one if 
print(num_list)
list1=["even" if x%2==0 else "odd" for x in range(20)] # this is list comprehension with if and else
'''





 











  



"""
