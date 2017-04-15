import os
def my_listdir(leval,path):

    for i in os.listdir(path):
        print('|  '*(leval + 1) + i)
        if os.path.isdir(path+i):

            my_listdir(leval+1, path+i+"\\")


path = 'D:\py'#+os.sep+'ant'
print(path+os.sep)
my_listdir(0, path+os.sep)














