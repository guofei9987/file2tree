# -*- coding: utf-8 -*-
import os
import os.path
import sys
import platform


def get_tree(rootdir):
    stack = []
    ret = []
    stack.append(rootdir)
    while len(stack) > 0:
        tmp = stack.pop(len(stack) - 1)
        if os.path.isdir(tmp):
            tmp = os.path.normcase(tmp)
            ret.append(tmp.split(rootdir)[1])
            for item in os.listdir(tmp):
                stack.append(os.path.join(tmp, item))
        # print tmp
        elif os.path.isfile(tmp):
            tmp = os.path.normcase(tmp)
            ret.append(tmp.split(rootdir)[1])
        # print tmp
    return ret


def get_deepth(path):
    plat_sys = platform.system()
    deepth = 0
    if plat_sys == "Windows":
        path = path.strip("\\")
        deepth = path.count("\\") + 1
    elif plat_sys in ("Linux", "Darwin"):
        path = path.strip("/")
        deepth = path.count("/") + 1
    return deepth


def write_tree(rootdir):
    path_list = get_tree(rootdir)
    length = len(path_list)
    for index in range(1, length):
        tmp = path_list[index]
        deepth = get_deepth(tmp)
        if (index < length - 1):
            tmp_next = path_list[index + 1]
            deepth_next = get_deepth(tmp_next)
        else:
            deepth_next = -1

        path_name = os.path.split(tmp)[1]

        if deepth_next == deepth or deepth_next > deepth:
            space = ""
            for sp in range(0, deepth - 1):
                space += "│  "
            line = space + "├─" + path_name + "\n"
            sys.stdout.write(line)

        elif deepth_next < deepth:
            space = ""
            for sp in range(0, deepth - 1):
                space += "│  "
            line = space + "└─" + path_name + "\n"
            sys.stdout.write(line)


def main():
    rootdir = os.getcwd()
    rootdir = os.path.normcase(rootdir)
    write_tree(rootdir.rstrip("\\"))
