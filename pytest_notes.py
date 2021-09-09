          ########  >>> Pytest Module <<<  ####
it is the module which is resposible to cheak any funtion of program or part of
the program
* we need to install first :pip install pytest on cmd
script we want to test:
filename of below code is :script1.py
def mul(a,b):
    return a*b
def sub(x,y):
    return x-y

*funtion through which above script is tested:
prerequite for test
1-funtion file name start with test
2-import the test funtion like import script1
3-funtion also start with test
4-no of test caeses then number of test cases is pass after test goes right 
#filename of below code is :test_cheak.py
import script1
def test_sub():
    
    
    result=script1.sub(20,18)

    assert result==2
    
def test_mul():
    res=script1.mul("a",2)
    assert res=="aa"
    
    
    
    

   
    
    

