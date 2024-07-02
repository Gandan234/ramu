#from collections import itertools
#a = [1]
#b = [1, 2]
from itertools import product
a = [1,2]
b = [3]
prod_obj = product(a,b)
list(prod_obj)
#[(1,3)(2,3)]
#permuations all possible orderings of an impact
from itertools import permutations
a = [1,2,3]
perm_obj = permutations(a,2)
len(list(perm_obj))
# 6 resutl
from itertools import accumulate
a = [1,2,3,4]
acc_obj = accumulate(a)
print(list(acc_obj))
# restult[1,3,6,10]
def add_num(x):
    return x+10
output = add_num(5)
print(output)
# result 15
# lambda
# lamba arguments: expression
# <function __main__,<lambda>(arguments)>
#small one line functions without a name
add_1 = lambda x:x+1
add_1
# result 6
mult = lambda x,y:x*y
mult(2,10)
# result 20
point2d = [(1,2),(15,1),(5,-2),(10,4)]
sorted(point2d)
# result[(1,2),(15,1),(5,-2),(10,4)]
def sort_by_y(tup):
    return tup[1]
sorted(point2d,key=sort_by_y)
#[(5,2),(15,1),(1,2),(10,4)]
def sort_by_sum(tup):
    return tup[0]+tup[1]
sorted(point2d,key=sort_by_sum)
[(1,2),(5,-2),(10,4),(15,1)]
sorted(point2d, key= lambda tup: tup[1])
# [(5,-1),(15,1),(1,2),(130,4)]
#maps
# map transforms each element with a func

def multwith2(x):
    return 2*x
a = [1,2,3,4,5,]
list(map(multwith2,a))
# result [2,4,6,8,10]

# without def multwith2(X) retult is not possible
list(map(lambda x: x%2, a))
#restult [1,0,1,0,1,0]
#filter
# function should return true or falsem what ever is true filters that
a = [1,2,3,4,5,6]
3%2 ==0
#return = false
b=filter(lambda x: x%2 == 0,a)
list(b)
#result [2,4,6]
a = ['oshdf','ihksfg,''ohjgf']
b = filter(lambda x: x[0]=='o' and x[-1]=='f',a)
#list[b]
#rslt ['oshdf', 'ohjgf']
a = [1,2,3,4,5,6]
list(map(lambda x: 'chocklet' if x <=3 else 'cadbury',a))
# rslt ['chocklet','chocklet','chocklet','cadbury','cadbury','cadbury']
def choc_bis(x):
    if x<=3:
        return 'chocolate'
    else:
        return 'biscut'
list(map(choc_bis,a))
#rslt    ['chocolate','chocolate','chocolate','biscuit','biscuit','biscuit']
from functools import reduce
#reduce(func, seq)
a = [1,2,5,4,8,6]
reduce((lambda x,y:x+y,a))
#slt 26 suming all numbers
a if a<b else b
#'<' not supported betw list & filter
reduce((lambda x,y: x if x>y else y,a))
#slt 8




