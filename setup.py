from setuptools import setup, find_packages
import os
import file2tree

this_directory = os.path.abspath(os.path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(name='file2tree',
      version=file2tree.__version__,
      description='file2tree',
      long_description=read_file('README.md'),
      long_description_content_type="text/markdown",
      url='https://github.com/guofei9987/file2tree',
      author='Guo Fei',
      author_email='guofei9987@foxmail.com',
      license='MIT',
      packages=['file2tree'],
      zip_safe=False,  # 为了兼容性，一般填 False
      entry_points={
          'console_scripts': [
              'file2tree = file2tree.file2tree:main'
          ]
      },
      )
