#演示模块导入方法

'''
#导入模块
import my_math
#调用my_math包里的my_add
print(my_math.my_add(1,2))
'''

'''
#导入my_math包,起别名
import my_math as mt
print(mt.my_add(1,4))
'''
'''
#导出my_math中所有的函数和变量
from my_math import *

#导出my_math中某一个函数（例如my_add)
from my_math import my_add
print(my_add(1,3))
'''

'''
导入模块时，被导入的模块会从上到下执行一遍
例如:在my_math模块中加入print(),调用my_math时,不论调用的时所有函数还是单个函数,都会先输出print(),再执行函数
'''