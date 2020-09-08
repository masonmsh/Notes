import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="File OPT.")
    parser.add_argument('--path', nargs='?', default='./', help='Input path.')
    parser.add_argument('--opt', type=int, default=0,
                        help='1:Intercept part of the file name as the new file name, 2:Add zero in front of the file name, 3:Batch number before file.')
    parser.add_argument('--exec', type=int, default=0,
                        help='0:Not execute, 1:Execute.')
    return parser.parse_args()


# 截取部分文件名作为新文件名 | 重命名
def rename(path, execute):
    ls = os.listdir(path)
    for l in ls:
        if l == 'fileopt.py':
            continue
        x = -4  # 后缀名(带.)
        a, b = 1, -2  # 截取位置
        name = l[a:b+x] + l[x:]  # 新文件名
        print(l, '||', name)
        if execute:
            os.rename(path + l, path + name)


# 截取文件名数字并补零 | 重命名
def addzero(path, execute):
    ls = os.listdir(path)
    for l in ls:
        if l == 'fileopt.py':
            continue
        a = 16  # 截取位置
        name = l[a:]  # 新文件名
        name = str('%03d' % int(name))
        print(l, '||', name)
        if execute:
            os.rename(path + l, path + name)


# 文件前批量加序号 | 重命名
def addnum(path, execute):
    ls = os.listdir(path)
    a = 1  # 序号
    for l in ls:
        if l == 'fileopt.py':
            continue
        name = l
        if a < 10:
            name = '[00' + str(a) + '] ' + l
        elif a < 100:
            name = '[0' + str(a) + '] ' + l
        else:
            name = '[' + str(a) + '] ' + l
        print(l, '||', name)
        if execute:
            os.rename(path + l, path + name)
        a += 1


if __name__ == '__main__':
    args = parse_args()
    path = args.path
    opt = args.opt
    execute = args.exec
    if opt == 1:
        rename(path, execute)
    elif opt == 2:
        addzero(path, execute)
    elif opt == 3:
        addnum(path, execute)
    else:
        print('none')
