import csv  #导入其他人的csv模块
import json  #用json格式生成报告

def read_students_csv(filename):       #读取
    '''
    读取学生信息
    :param filename:文件名,students.csv
    :return: 返回列表,json格式,存储学生学习
    {
        'name':'aaa'
        'age':18
        'score':100    
    }
    
    '''
    students =[]
    try:
        with open(filename,'r',encoding='utf-8') as f :
            reader = csv.DictReader(f)
            for row in reader:
                students.append(
                    {
                        'name' : row['name'],
                        'age' : int(row['age']),
                        'score' : float(row['score'])
                    }
                )
        return students
    except Exception as e:
        print(f'文件读取错误:Error is :{e}')
        return []
    

def calculate_average(students):  #计算平均值
    '''
    计算平均值
    :param students:传入的学生列表，每个元素是一个字典
    :return: 所有学生的平均值
    '''
    if not students:
        return None
    total = sum(s['score'] for s in students)
    return total/len(students)

def find_top_student(students):  #查找最高分
    '''
    查找最高分的学生
    :param students:传入的学生列表，每个元素是一个字典
    :return: 返回最高分的学生信息
    '''
    if not students:
        return None
    top_student = max(students, key=lambda s: s['score'])   #lambda 参数列表 : 返回表达式（比较字典中某个key的值）
    return top_student

def save_report(filename,students):#保存文件
    '''
    将字典信息储存为json文件
    :param filename:文件名json文件路径
    :param students:学生列表
    :return: None
    '''
    try:
        report = {
            'total_students':len(students),
            'average_student':calculate_average(students),
            'top_student':find_top_student(students),
            'students':students
        }
        with open(filename,'w',encoding='utf-8') as f:
            json.dump(report,f,ensure_ascii=False,indent=4)       #调用json库的dump函数
        print(f'报告已经保存到{filename}')
    except Exception as e:
        print(f'文件保存错误:Error is :{e}')


if __name__== '__main__':
    students = read_students_csv('../students.csv')
    print(students)
    print(calculate_average(students))
    print(find_top_student(students))
    save_report('./students.json', students)