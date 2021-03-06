# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from os import path as os_path
import time

# from config import *




name='tkitSeg'#修改包名字-
version='0.0.0.5.1'
description='Terry toolkit tkitSeg,一个中文分词和词性标注工具'
author='Terry Chan'
author_email='napoler2008@gmail.com'
url='https://docs.terrychan.org/tkit-seg/'

copyright = '2021, Terry Chan'
language = 'zh_cn'






this_directory = os_path.abspath(os_path.dirname(__file__))
"""帮助[https://www.notion.so/6bade2c6a5f4479f82a4e67eafcebb3a]

上传到anaconda
https://docs.anaconda.com/anacondaorg/user-guide/tasks/work-with-packages/
 
    """
# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]
# long_description="""

# 这里是说明
# 一个创建库的demo
# http://www.terrychan.org/python_libs_demo/
# """



try:
    long_description=read_file("README.md")
except:
    long_description=""
setup(
    name=name, #修改包名字-
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    # install_requires=read_requirements('requirements_seg.txt'),  # 指定需要安装的依赖
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'numpy>=1.21.2',
        'onnx>=1.10.1',
        'onnxruntime>=1.9.0',
        'transformers>=4.10.3',

    ],
    packages=['tkitSeg'],
    include_package_data=True,  # 打包包含静态文件标识
    )

"""
pip freeze > requirements.txt

python3 setup.py sdist
#python3 setup.py install
python3 setup.py sdist upload
"""