        #  >>>>   thread without implementing class <<< #
        

from threading import *
def fun1():
    print("this is child thread")
    print("name of thread:",current_Thread().getName())
t=Thread(target=fun1)
t.start()
print("this is main thread")



     # >>>> thread implemented by inheriting Thread class <<<< # 

from threading import   *
class A(Thread):
  def run(self):
    for x in range(10):
      print("chiled thread")
t=A()
t.start()
t.join()
for i in range(10):
  print("this is main Thread")


      # >>> thread using class but without inheringthread class <<< #

from threading import *
class A:
    def fun1(self):
      for x in range(10):

        print('child Thread')
a=A()
t=Thread(target=a.fun1)
t.start()
t.join()  #comment it and cheak
for i in range(10):
  print("this is main thread")
print(current_thread().ident)#it use to see the identification number of thread


