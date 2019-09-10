"""
print('hello python')
cars=100
print("there are",cars,"cars available.")
print("there are %s" % cars)

x="there are %d types of people" % 10
print(x)

# %r 好像是原样输出
# %r use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users.
# %r the %r is best for debugging,and the other formats are for actually displaying variables to users.
print ("i say %r" % x)
print ("i say %s." %x)


formatter = "%r %r %r %r"
print(formatter % (1,2,3,4))
print(formatter % ("one","two","three","four"))

'''
raw_input was removed in python 3 ,and its behavior switched to input.
input("\n\nPress the enter key to exit.")
'''
a,b,c=1,2,"character c"
del a
print(c[-5:])

list = ['abcd', 789, 2.34]
print(list*2)
#元组 tuple 用 （） 标识。内部用逗号隔开，但是元素不能二次赋值，相当于只读列表。
#元组中只包含一个元素时，需要在元素后面添加逗号。
#任意无符号的对象，以逗号隔开，默认为元组。
#列表是有序的对象集合，字典是无需的对象集合。区别在于，字典当中的元素是通过键来存取，而不是通过偏移量。
#字典用｛｝标识。字典由索引key和对应的value组成。
# a in list 相当于php的in_array(a,list)


#100以内的质数、素数

i=2
while(i<100):
    j=2
    while(j <= (i/j)):
        if not(i%j):break
        j=j+1
    else: print(i,"是素数")
    i=i+1

num=[]
i=2
#range 不包括右边界
for i in range(2,100):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        num.append(i)
print(num)

i=1
#j=1
while i<=9:
   if i<=5:
      print ("*"*i)

   elif i<=9 :
      j=i-2*(i-5)
      print("*"*j)
   i+=1
else :
   print("")

#cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算，都需要用import导入

import calendar
cal = calendar.month(2018,10)
print(cal);

def printinfo(arg,*vartuple):
    "print all input"
    print(arg)
    for var in vartuple:
        print(var)
    return;

printinfo(10)
printinfo(10,20,30,'a')
"""

"""
#对象与参考
#同一个对象
shoplist = ['apple','mango','carrot','banana']
mylist = shoplist # mylist is just another name pointing to the same object
del shoplist[0]
del mylist[0]
print(shoplist)
print(mylist)
#notice that both shoplist and mylist both print the same list without the 'apple' confirming that they point to the same object
#不同
mylist = shoplist[:]
del mylist[0]
print(shoplist)
print(mylist)
#如果你想要复制一个列表或者类似的序列或者其他复杂的对象（不是如整数那样的简单对象），那么你必须使用切片操作符来取得拷贝。如果你只是想要使用另一个变量名，两个名称都 参考 同一个对象，那么如果你不小心的话，可能会引来各种麻烦。
#记住列表的赋值语句不创建拷贝。你得使用切片操作符来建立序列的拷贝。


#join用法， delimiter.join(list)
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))


import timeit
def fun1(x,y):
    return x**2 +y**3
t_start = timeit.default_timer()
z=fun1(109.2,367.1)
t_end = timeit.default_timer()
cost =t_end-t_start
print(cost)
"""

#ndarray  n维数组
import numpy as np
a=np.arange(5)

def isValid(s):
    stack=[]
    paren_map={')':'(',']':'[','}':'{'}
    for c in s:
        if c not in paren_map:
            stack.append(c)
        elif not stack or paren_map!=stack.pop():
            return False
        return not stack

print(isValid('[]'))