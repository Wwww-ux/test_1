def my_add(num1,num2):
    return num1+num2

'''
当my_math作为模块被导入时,__name__为my_math(模块名)
当my_math自己启动时,__name__为__main__
'''

'''
若只想部分函数在my_math自己启动时执行,则需要加上:
if __name__ =='__main__':
'''


