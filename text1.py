'''
def fun1(*a,**b):
    with open ("a.txt",'w',encoding='utf-8') as f:
        c=str(a)
        f.write(c)
'''

def fun2():
    try:
        with open("b.txt",'r',encoding='utf-8') as f:
            contect=f.read()
            contect_lst=contect.strip('()').split()
            for i in contect_lst:
                print(f"文本内容为：{i}")
    except Exception as e:
        print("未找到文件:{}",e)
    finally:
        print("文件操作完成")

if __name__ == "__main__":
    '''fun1(222,333,444)'''
    fun2()