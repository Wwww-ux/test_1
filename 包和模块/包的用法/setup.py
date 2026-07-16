from setuptools import setup,find_packages

setup(
    name='datatools',      #包名称
    version='1.0.0',       #包版本号
    description='数据处理工具包',    #描述
    author='Wzb',           #作者名字
    author_email='204479991@qq.com',     #邮箱
    url='',                    #包的链接
    license='MIT',          #权限采用MIT协议
    packages=find_packages(),     #导入所有子包
    python_requires ='>=3.7',     #python版本>=3.7
    install_requires=[            
        'numpy>=1.19.0',         #使用该包需要安装numpy，版本>=1.19
    ],
    classifiers=[
        'Development Status :: 4 - Beta',       #开发状态
        'Intended Audience :: Developers',      #使用对象：开发者
        'License :: OSI Approved :: MIT License',   #
        'Programming Language :: Python :: 3',         #语言
    ],
)