'''
#使用__init__.py方法一，直接使用函数，不需要加前缀
from info_utils import *
if __name__== '__main__':
    students = read_students_csv('../students.csv')
    print(students)
    print(calculate_average(students))
    print(find_top_student(students))
    save_report('./students.json', students)

'''


from info_utils import utils
#当前使用__init__.py中的方法二，需要加上utils.前缀

if __name__== '__main__':
    students = utils.read_students_csv('./students.csv')#同级目录下‘./’可加可不加
    print(utils.calculate_average(students))
    print(utils.find_top_student(students))
    utils.save_report('./students.json', students)