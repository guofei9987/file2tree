# -*- coding: utf-8 -*-
import os
import os.path
import sys
import getopt
import platform
def usage():
    print('[ * ] use like "python file2tree.py -r d:/tree"')
    print('[ * ] or use like "python file2tree.py --rootdir d:/tree"')


def get_tree(rootdir):
	stack=[]
	ret=[]
	stack.append(rootdir)
	while len(stack)>0:
		tmp=stack.pop(len(stack)-1)
		if os.path.isdir(tmp):
			tmp=os.path.normcase(tmp)
			ret.append(tmp.split(rootdir)[1])
			for item in os.listdir(tmp):
				stack.append(os.path.join(tmp,item))
			#print tmp
		elif os.path.isfile(tmp):
			tmp=os.path.normcase(tmp)
			ret.append(tmp.split(rootdir)[1])
			#print tmp
	return ret

def get_deepth(path):
	plat_sys=platform.system()
	deepth=0
	if plat_sys == "Windows":
		path=path.strip("\\")
		deepth=path.count("\\")+1
	elif plat_sys == "Linux":
		path=path.strip("/")
		deepth=path.count("/")+1
	return deepth
	
def write_tree(rootdir):
	file_tree=open(os.path.join(rootdir,"file2tree.txt"),"w")
	path_list=get_tree(rootdir)
	length=len(path_list)
	#file_tree.write("├─"+os.path.split(rootdir)[1]+"\n")
	for index in range(1,length):
		tmp=path_list[index]
		deepth=get_deepth(tmp)
		if(index<length-1):
			tmp_next=path_list[index+1]
			deepth_next=get_deepth(tmp_next)
		else:
			deepth_next=-1
			
		path_name=os.path.split(tmp)[1]
		
		if deepth_next==deepth or deepth_next>deepth:
			space=""
			for sp in range(0,deepth-1):
				space+="│  "
			line=space+"├─"+path_name+"\n"
			file_tree.write(line)
	
		elif deepth_next<deepth :
			space=""
			for sp in range(0,deepth-1):
				space+="│  "
			line=space+"└─"+path_name+"\n"
			file_tree.write(line)
		#print os.path.split(i)[1]
	file_tree.close()
	
	
opts, args = getopt.getopt(sys.argv[1:], "hr:", ["help", "rootdir="])
if not opts:
	usage()
for op, value in opts:
	if op == "-r" or op == "--rootdir":
		rootdir = value
		if not os.path.exists(rootdir):
			print('[ * ] path "%s" does not exist,please check the param "-r"' % (rootdir))
			sys.exit()
		else:
			rootdir=os.path.normcase(rootdir)
			write_tree(rootdir.rstrip("\\"))	
	else:
		usage()
		sys.exit()
