#写入版本
__version__ = '0.0.1'


'''
导入同一级文件时：
from .同级文件名 import 函数名

导入上一级文件时：
from ..上一级文件名 import 函数名

'''

from .io import reader,writer
from .core import processor
__all__ = ['processor','reader','writer']