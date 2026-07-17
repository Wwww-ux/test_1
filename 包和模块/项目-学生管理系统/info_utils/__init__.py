
#将utils作为模块导出
'''
#方法一:到处utils文件中的函数，主函数调用时可以直接使用
from utils import read_students_csv, calculate_average, find_top_student, save_report
__all__ = ['read_students_csv', 'calculate_average', 'find_top_student', 'save_report']
'''
#方法二：直接导出utils模块，主函数调用时需要加上utils.前缀
__all__ = ['utils']