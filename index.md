## Welcome
***
[blog](https://masonmsh.github.io/ "冷香榭")

- [Welcome](#welcome)
- [Linux](#linux)
    - [linux配置文件](#linux配置文件)
    - [进程操作](#进程操作)
      - [查看进程](#查看进程)
      - [杀死进程](#杀死进程)
      - [断连继续运行](#断连继续运行)
    - [硬盘操作](#硬盘操作)
      - [列举文件](#列举文件)
      - [占用空间](#占用空间)
- [Windows](#windows)
    - [7-zip](#7-zip)
    - [文件操作](#文件操作)
- [Python](#python)
    - [pip](#pip)
      - [pip配置文件](#pip配置文件)
      - [pip配置文件位置](#pip配置文件位置)
    - [基本数据类型](#基本数据类型)
      - [遍历字典](#遍历字典)
    - [Pandas](#pandas)
      - [统计每一行元素的个数](#统计每一行元素的个数)
    - [Numpy](#numpy)
      - [序列排序返回索引](#序列排序返回索引)
      - [获得列表中每个元素出现的次数](#获得列表中每个元素出现的次数)
      - [Pandas和Numpy互相转化](#pandas和numpy互相转化)
    - [Scrapy](#scrapy)
      - [新建项目](#新建项目)
      - [执行项目](#执行项目)
    - [Tensorflow](#tensorflow)
      - [静态分配GPU](#静态分配gpu)
      - [动态分配GPU](#动态分配gpu)
      - [指定GPU](#指定gpu)
- [Aria2](#aria2)
    - [aria2配置文件](#aria2配置文件)
    - [运行](#运行)
- [VSCode](#vscode)
    - [vsc设置](#vsc设置)

***
## Linux
#### linux配置文件
[.bashrc](https://github.com/masonmsh/Notes/blob/master/plugin/linux/bashrc.txt "bash")  
[.vimrc](https://github.com/masonmsh/Notes/blob/master/plugin/linux/vimrc.txt "vim")  
[source.list](https://github.com/masonmsh/Notes/blob/master/plugin/linux/sources.txt "/etc/apt/source")
#### 进程操作
##### 查看进程
```
ps -aux
ps -ef
```
##### 杀死进程
```
kill -9 pid
```
##### 断连继续运行
```
nohup xxx >xxx.out 2>&1 &
```
#### 硬盘操作
##### 列举文件
```
ls [-alht]
```
##### 占用空间
```
du -sh --max-depth=1
```
## Windows
#### 7-zip
[批量操作.bat](https://github.com/masonmsh/Notes/blob/master/doc/bat/7zip%E6%89%B9%E9%87%8F%E6%93%8D%E4%BD%9C.txt "7-zip")
#### 文件操作
[fileopt.py](https://github.com/masonmsh/Notes/blob/master/doc/bat/fileopt.py "fileopt")
## Python
#### pip
##### pip配置文件
[pip.conf](https://github.com/masonmsh/Notes/blob/master/doc/python/pip.ini "conf")  
[pip mirror](https://github.com/masonmsh/Notes/blob/master/doc/python/pip%20mirror.txt "mirror")
##### pip配置文件位置
```
pip -v config list
```
#### 基本数据类型
##### 遍历字典
```python
a={'a': '1', 'b': '2', 'c': '3'}
### 遍历 key
# 法1
for key in a:
    print(key+':'+a[key])

# 法2
for key in a.keys():
    print(key+':'+a[key])

### 遍历 value
for value in a.values():
    print(value)

### 遍历 item
for kv in a.items():
    print(kv)

### 遍历 key value
for key,value in a.items():
    print(key+':'+value)
```
#### Pandas
##### 统计每一行元素的个数
```python
import pandas as pd
df = pd.DataFrame([list('AABBAB'), list('BABAAA')])
d = (df == 'A').sum(axis=1)
print(d)
```
#### Numpy
##### 序列排序返回索引
```python
# argsort()函数是将x中的元素从小到大排列，提取其对应的index(索引)
import numpy as np
x = np.array([2,1,4,5,7,3,6])
y = x.argsort()
print(y, y[1], y[-1], sep='\n')
```
##### 获得列表中每个元素出现的次数
```python
from collections import Counter
l = [1,2,3,4,1,1,2,4,5,1,4,3,8,7,8,3]
count = Counter(l)
c = dict(count)
print(c)
```
##### Pandas和Numpy互相转化
```python
array = Dataframe_Name.values
df = pd.Dataframe(array)
```
#### Scrapy
##### 新建项目
```
scrapy startproject xxx
```
##### 执行项目
```
scrapy crawl xxx -o xxx.json -t json
```
#### Tensorflow
##### 静态分配GPU
```python
# 假如有12GB的显存并使用其中的4GB:
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
```
##### 动态分配GPU
```python
config = tf.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)
```
##### 指定GPU
```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# 或者在脚本或者命令行中指定
CUDA_VISIBLE_DEVICES=0
```
## Aria2
#### aria2配置文件
[aria2.conf](https://github.com/masonmsh/Notes/blob/master/aria2/aria2.conf "conf")
#### 运行
```
aria2c.exe --conf-path=aria2.conf
```
[run.bat](https://github.com/masonmsh/Notes/blob/master/aria2/run.bat "run")
## VSCode
#### vsc设置
[setting.json](https://github.com/masonmsh/Notes/blob/master/plugin/vsc/setting.json "json")  
[list](https://github.com/masonmsh/Notes/blob/master/plugin/vsc/list.txt "list")

