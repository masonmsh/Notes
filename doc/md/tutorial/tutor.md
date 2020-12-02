Tutorial
=
***

## 目录
* [标题](#标题)
* [横线](#横线)
* [文本](#文本)
  * [普通文本](#普通文本)
  * [单行文本](#单行文本)
  * [文本块](#文本块)
  * [文字高亮](#文字高亮)
  * [换行](#换行)
  * [斜体/粗体/删除线](#斜体/粗体/删除线)
* [链接](#链接)
  * [直链](#直链)
  * [外部链接](#外部链接)
  * [本地链接](#本地链接)
  * [锚点](#锚点)
* [图片](#图片)
  * [网络图片](#网络图片)
  * [本地图片](#本地图片)
  * [为图片加入链接](#为图片加入链接)
* [列表](#列表)
  * [无序列表](#无序列表)
  * [有序列表](#有序列表)
  * [列表嵌套](#列表嵌套)
  * [复选框列表](#复选框列表)
* [块引用](#块引用)
* [表格](#表格)
* [脚注](#脚注)
* [注释](#注释)
* [转义字符](#转义字符)
* [文本块的高级应用](#文本块的高级应用)
  * [代码高亮](#代码高亮)
  * [版本控制](#版本控制)
  * [流程图](#流程图)
  * [时序图](#时序图)
  * [甘特图](#甘特图)
* [表情](#表情)
* [公式](#公式)
  * [行内公式](#行内公式)
  * [行间公式](#行间公式)
  * [字符对照表](#字符对照表)
  * [使用参考](#使用参考)
* [其它](#其它)
  * [Github图片引用方式](#github图片引用方式)
  * [HTML](#html)
* [后记](#postscript)

<!-- [TOC] -->

## 标题
#### 语法1
```
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```
#### 语法2
```
一级标题
=
二级标题
-
```

[返回目录](#目录)
## 横线
#### 语法
```
***
---
___
```
#### 示例
***
---
___

[返回目录](#目录)
## 文本
### 普通文本
#### 语法
```
word
```
>说明
>- `word`：普通文本
#### 示例
普通的文本

[返回目录](#目录)
### 单行文本
#### 语法1
```
[space][space][space][space]word
```
>说明
>- `[space]`：空格
#### 语法2
```
[tab]word
```
>说明
>- `[tab]`：制表符
#### 示例
    在一行的开头输入4个空格或一个制表符可以产生单行文本

[返回目录](#目录)
### 文本块
#### 语法1
```
[space][space][space][space]word
[space][space][space][space]word
...
```
#### 语法2
```
[tab]word
[tab]word
...
```
#### 语法3
```
[```]
word
[```]
```
>说明
>- `[```]`：三个反引号```，三个反引号不需要加括号，这里是为了防止转义
#### 示例
    在多行文本的每一行的开头
    打入4个空格或一个制表符
    可产生文本块
```
使用一对各三个的反引号
也会产生文本块
但似乎这两种方式在某些渲染器下不太相同，比如现在这款
```

[返回目录](#目录)
### 文字高亮
#### 语法
```
`word`
```
#### 示例
`linux`  
`windows`  
`macOS`  
`这也适合做一篇文章的tag`

[返回目录](#目录)
### 换行
#### 语法1
```
word[space][space]
word
```
#### 语法2
```
word
[null]
word
```
>说明
>- `[null]`：空行
#### 示例
直接回车不能换行  
可以在上一行文本后面补两个空格  
这样下一行的文本就换行了

在两行文本间直接加一个空行

也能实现换行效果，不过这个行间距有点大

[返回目录](#目录)
### 斜体/粗体/删除线
|语法|示例|
|-|-|
|`*word*`|*斜体1*|
|`_word_`| _斜体2_|
|`**word**`|**粗体1**|
|`__word__`|__粗体2__|
|`~~word~~`|~~删除线~~|
|`***word***`|***斜粗体1***|
|`___word___`|___斜粗体2___|
|`***~~word~~***`|***~~斜粗体删除线1~~***|
|`~~***word***~~`|~~***斜粗体删除线2***~~|
>说明
>- 斜体、粗体、删除线可混合使用

[返回目录](#目录)
## 链接
### 直链
#### 语法
```
<URL>
```
>说明
>- `URL`：网页链接
>- 链接可以使用绝对链接或相对链接
#### 示例
<https://www.baidu.com/>

[返回目录](#目录)
### 外部链接
#### 语法1
```
[alt](URL "title")
```
>说明
>- `alt`：此超链接显示文本
>- `title`：鼠标悬停在超链接时的显示文本，可以不加title
#### 语法2
```
[alt][URL-name]
[URL-name]:URL "title"
```
>说明
>- `URL-name`：URL标签
>- 使用URL标签能达到复用的目的，一般把全文所有的URL标签统一放在文章末尾，这样看起来比较干净
>- URL标签只是一个代号
>- 本文URL标签都放置于文末
#### 示例
[baidu](http://www.baidu.com/ "百度")  
[baidu][Baidu]

[返回目录](#目录)
### 本地链接
#### 语法
>说明
>- 链接本地URL与链接外部URL相同，只不过URL表示本地路径
#### 示例
[emoji](/tutorial/emoji.md "emoji")  
[emoji](./emoji.md "emoji")  
[emoji][emoji]

[返回目录](#目录)
### 锚点
#### 语法
```
[alt](#title)
```
>说明
>- `alt`：此锚点显示文本
>- `title`：锚点名称
>- 标题引用要小写，部分渲染器不支持中文和空格等特殊字符引用
>- 后记标题使用html方式进行引用，好处是可以设置id进行跳转，不用考虑中文问题
#### 示例
[目录均为锚点，点此返回查看](#目录)

[返回目录](#目录)
## 图片
### 网络图片
#### 语法1
```
![alt](URL "title")
```
>说明
>- `alt`：图片显示失败时的替换文本
>- `title`：鼠标悬停在图片时的显示文本
#### 语法2
```
![alt][URL-name]
[URL-name]:URL "title"
```
#### 示例
![baidu-logo](http://www.baidu.com/img/bdlogo.gif "百度logo")  
![baidu-logo][baidu-logo]

[返回目录](#目录)
### 本地图片
#### 语法
>说明
>- 链接本地图片与链接外部图片相同，只不过URL表示本地路径
#### 示例
![csdn-logo][CSDN-logo]

[返回目录](#目录)
### 为图片加入链接
#### 语法1
```
[pic](URL "title")
```
>说明
>- `pic`：图片，等于上面介绍的图片语法
#### 语法2
```
[pic][url-name]
[URL-name]:URL "title"
```
#### 示例
[![baidu-logo][baidu-logo]](https://www.baidu.com/ "百度")  
[![csdn-logo][CSDN-logo]][CSDN]

[返回目录](#目录)
## 列表
### 无序列表
#### 语法
```
+ word
- word
* word
```
#### 示例
+ 使用+号和空格构造无序列表
- 使用-号和空格构造无序列表
* 使用*号和空格构造无序列表

[返回目录](#目录)
### 有序列表
#### 语法
```
num. word
```
>说明
>- `num`：数字
#### 示例
1. 使用数字加点构造有序列表
2. 有序列表的编号只与第一个数字有关

[返回目录](#目录)
### 列表嵌套
#### 示例
+ 无序列表和有序列表可以相互嵌套
  + 每层嵌套需要缩进3个空格
    + 尤其是有序列表嵌套无序列表
      + 无序列表之间的嵌套只需2个空格
  + 但一般都会用2个显得整齐
+ 这是无序套有序
  1. 这是有序列表
  2. 接下来的数字是几都没有关系
1. 这是有序套无序
   + 无序列表可以随便使用
   * 但尽量用同一个符号
2. 这是有序套有序
   1. 嵌套列表尽量从1开始
   2. 因为不是所有的解析器都支持

[返回目录](#目录)
### 复选框列表
#### 语法
```
- [x] word
- [] word
```
#### 示例
- [x] 利用减号和方括号x构造选中的列表，方括号两边都有空格
- [ ] 如果中间没有x，则表示未选中
  - [x] 当然，复选框也可以嵌套
  - [ ] 只需要缩进2个空格
- [x] 您可以使用这个功能来标注某个项目各项任务的完成情况

[返回目录](#目录)
## 块引用
#### 语法
```
>word
```
#### 示例
>通过输入">"来进行块引用  
换行不需要输入">"，当然第一行后面需要打2个空格

>如果想另起一行则需要打印空行
>>块引用可以进行多级嵌套
>>>>嵌套可以跳级
>
>>可以通过">"来跳出嵌套
>
>随便你跳出到几层都可以

>引用的区块内也可以使用其他的 Markdown 语法，包括标题、列表、代码区块等
>1. 常用列表
>2. 其它组合进行尝试就行了

[返回目录](#目录)
## 表格
#### 语法
```
|word|word|
|-|-|
|word|word|
```
#### 示例
|使用竖线分割表格|使用减号分割表头和内容|
|-|-|
|减号个数随意|边侧的竖线随意|
|表格可以多行|默认是左对齐|

|表格可以声明对齐方式|在分割线两侧加冒号|第一行效果第二行方法|
|:-|:-:|-:|
|左对齐|居中|右对齐|
|左边加冒号|两边加冒号|右边加冒号|

|表格可以嵌入格式和链接|方式没有变化|
|-|-|
|文字操作|*斜体* **加粗** ~~删除线~~|
|插入链接|[baidu][Baidu]|
|插入图片|![baidu-logo][Baidu-logo]|

[返回目录](#目录)
## 脚注
#### 语法
```
[^word]
```
#### 示例
脚注用于引用，方式在中括号内加“^”和脚注内容[^note]

[返回目录](#目录)
## 注释
#### 语法
```
<!--word-->
```
#### 示例
<!--反正你也看不到-->

[返回目录](#目录)
## 转义字符
#### 语法
```
\symbol
```
>说明
>- `symbol`：需要转义的符号
#### 示例
\\
\`
\*
\_
\{\}
\[\]
\(\)
\#
\+
\-
\.
\!

[返回目录](#目录)
## 文本块的高级应用
### 代码高亮
#### 语法
```
[```]name
code
[```]
```
>说明
>- `name`：语言的名称
>- `code`：代码
#### 示例
```Java
public static void main(String[]args){} //Java
```
```c
int main(int argc, char *argv[]) //C
```
```Bash
echo "hello bash" #Bash
```
```javascript
document.getElementById("myH1").innerHTML="Welcome to my Homepage"; //javascipt
```
```cpp
string &operator+(const string& A,const string& B) //C++
```
```python
def hello()
    print("hello python") # Python
```

[返回目录](#目录)
### 版本控制
#### 语法
```
[```]diff
+ add
- delete
[```]
```
>说明
>- 版本控制的系统中都少不了diff的功能，即展示一个文件内容的增加与删除
>- 使用绿色表示新增，红色表示删除
#### 示例
```diff
+ 加号表示增加
- 减号表示删除
```

[返回目录](#目录)
### 流程图
#### 语法
```
[```]flow
tag=>type: content:>url
tag1->tag2
[```]
```
>说明
>- `tag`：标签的名称
>- `type`：标签的类型
>- `content`：标签内的文字
>- `url`：标签链接的url  
>**type有6种**
>- `start`：开始
>- `end`：结束
>- `operation`：操作
>- `subroutine`：子程序
>- `condition`：判断
>- `inputoutput`：输入输出
#### 示例
```flow
st=>start: Start
op=>operation: Your Operation:>https://www.baidu.com/
cond=>condition: Yes or No?
in=>inputoutput: input
out=>inputoutput: output
e=>end
st->op->in(right)->cond
cond(yes)->out->e
cond(no)->op
```

[返回目录](#目录)
### 时序图
#### 语法
```
[```]sequence
title: title
participant actor as act
actor1 opt actor2: content
Note actor: content
[```]
```
>说明
>- `title`：标题
>- `actor`：参与者
>- `act`：参与者别名
>- `opt`：交互
>- `content`：交互内容
>- `Note`：注释  
>**opt有4种**
>- `-`：实线，发送消息
>- `--`：虚线，返回消息
>- `>`：实心箭头，同步消息
>- `>>`：非实心箭头，异步消息  
>**Note有4种**
>- `Note left of actor`：actor左侧
>- `Note right of actor`：actor右侧
>- `Note over actor`：actor中间
>- `Note over actor1, actor2`：actor1和actor2中间
#### 示例
```sequence
title: Login
participant client
participant server
participant pass as pass center
Note over client: Enter account and password
client->pass: Send account and password
Note over pass: Verify account and password
pass-->>client: Return token
client->server: Send token
server->pass: Verify token
pass-->>server: Verify successfully
server-->>client: Login successfully
```

[返回目录](#目录)
### 甘特图
#### 语法
```
[```]gantt
title title
dateFormat dataFormat
section section
task:p1,p2,p3,p4,p5
[```]
```
>说明
>- `title`：标题
>- `dataFormat`：日期格式，常用`YYYY-MM-DD`
>- `section`：部分名
>- `task`：任务名
>- `p`：参数  
>**p有5种**
>- `p1`：强调`crit`
>- `p2`：状态`done` `active`
>- `p3`：别名
>- `p4`：开始日期`yyyy-mm-dd,after p3`
>- `p5`：截止时间`yyyy-mm-dd,nd`
#### 示例
```gantt
title Submit a paper
dateFormat YYYY-MM-DD
section experiment
Find datasets:done,s11,1999-12-31,2000-01-03
Write codes:crit,active,s12,after s11,10d
Run codes:s13,after s12,15d
section paper
Write architecture:done,s21,2000-01-05,5d
Write content:crit,active,s22,after s21,20d
Modify:after s13, 3d
```

[返回目录](#目录)
## 表情
#### 语法
```
:emoji:
```
>说明
>- `emoji`：表情名称
>- 表情详见`emoji.md`：[emoji](./emoji.md "emoji")
#### 示例
:blush:

[返回目录](#目录)
## 公式
### 行内公式
#### 语法
```
$formula$
```
>说明
>- `formula`：公式
#### 示例
$\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t$  
$x={-b\pm\sqrt{b^2-4ac}\over 2a}$

[返回目录](#目录)
### 行间公式
#### 语法
```
$$formula$$
```
#### 示例
$$x=y^2+1$$

[返回目录](#目录)
### 字符对照表
#### 希腊字母表
|输入|显示|大写|显示|变量|显示|
|:-:|:-:|:-:|:-:|:-:|:-:|
|`\alpha`|$\alpha$|`\Alpha`|$\Alpha$|||
|`\beta`|$\beta$|`\Beta`|$\Beta$|||
|`\gamma`|$\gamma$|`\Gamma`|$\Gamma$|||
|`\theta`|$\theta$|`\Theta`|$\Theta$|`\vartheta`|$\vartheta$|
|`\mu`|$\mu$|`\Mu`|$\Mu$|||
|`\delta`|$\delta$|`\Delta`|$\Delta$|||
|`\epsilon`|$\epsilon$|`\Epsilon`|$\Epsilon$|`\varepsilon`|$\varepsilon$|
|`\sigma`|$\sigma$|`\Sigma`|$\Sigma$|`\varsigma`|$\varsigma$|
|`\pi`|$\pi$|`\Pi`|$\Pi$|`\varpi`|$\varpi$|
|`\omega`|$\omega$|`\Omega`|$\Omega$|||
|`\xi`|$\xi$|`\Xi`|$\Xi$|||
|`\zeta`|$\zeta$|`\Zeta`|$\Zeta$|||
|`\chi`|$\chi$|`\Chi`|$\Chi$|||
|`\rho`|$\rho$|`P`|$P$|`\varrho`|$\varrho$|
|`\phi`|$\phi$|`\Phi`|$\Phi$|`\varphi`|$\varphi$|
|`\eta`|$\eta$|`\Eta`|$\Eta$|||
|`\lambda`|$\lambda$|`\Lambda`|$\Lambda$|||
|`\kappa`|$\kappa$|`\Kappa`|$\Kappa$|`\varkappa`|$\varkappa$|
|`\nu`|$\nu$|`\Nu`|$\Nu$|||
|`\upsilon`|$\upsilon$|`\Upsilon`|$\Upsilon$|||
|`\psi`|$\psi$|`\Psi`|$\Psi$|||
|`\tau`|$\tau$|`\Tau`|$\Tau$|||
|`\iota`|$\iota$|`\Iota`|$\Iota$|||
|`o`|$o$|`O`|$O$|||
#### 定界符
|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|
|\vert|$\vert$|\Vert|$\Vert$|
|\langle|$\langle$|\rangle|$\rangle$|
|\lfloor|$\lfloor$|\rfloor|$\rfloor$|
|\lceil|$\lceil$|\rceil|$\rceil$|
|\lbrace|$\lbrace$|\rbrace|$\rbrace$|
|\backslash|$\backslash$|/|$/$|
|\Uparrow|$\Uparrow$|\uparrow|$\uparrow$|
|\Downarrow|$\Downarrow$|\downarrow|$\downarrow$|
|\llcorner|$\llcorner$|\lrcorner|$\lrcorner$|
|\ulcorner|$\ulcorner$|\urcorner|$\urcorner$|
#### 关系运算符
|输入|显示|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|:-:|:-:|
|\pm|$\pm$|\times|$\times$|\div|$\div$|
|\mid|$\mid$|\nmid|$\nmid$|\cdot|$\cdot$|
|\circ|$\circ$|\ast|$\ast$|\bigodot|$\bigodot$|
|\bigotimes|$\bigotimes$|\bigoplus|$\bigoplus$|\leq|$\leq$|
|\geq|$\geq$|\neq|$\neq$|\approx|$\approx$|
|\equiv|$\equiv$|\sum|$\sum$|\prod|$\prod$|
|\coprod|$\coprod$|\backslash|$\backslash$|||
#### 集合运算符
|输入|显示|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|:-:|:-:|
|\emptyset|$\emptyset$|\in|$\in$|\notin|$\notin$|
|\subset|$\subset$|\supset|$\supset$|\subseteq|$\subseteq$|
|\supseteq|$\supseteq$|\bigcap|$\bigcap$|\bigcup|$\bigcup$|
|\bigvee|$\bigvee$|\bigwedge|$\bigwedge$|\biguplus|$\biguplus$|
#### 三角运算符
|输入|显示|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|:-:|:-:|
|30^\circ|$30^\circ$|\bot|$\bot$|\angle A|$\angle A$|
#### 微积分运算符
|输入|显示|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|:-:|:-:|
|\int|$\int$|\iint|$\iint$|\iiint|$\iiint$|
|\oint|$\oint$|\prime|$\prime$|\infty|$\infty$|
|\infty|$\infty$|\nabla|$\nabla$|||
#### 逻辑运算符
|输入|显示|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|:-:|:-:|
|\because|$\because$|\therefore|$\therefore$|\not\subset|$\not\subset$|
|\not<|$\not<$|\not>|$\not>$|\not=|$\not=$|
|\forall|$\forall$|\exists|$\exists$|||
#### 戴帽符号
|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|
|\hat{xy}|$\hat{xy}$|\widehat{xyz}|$\widehat{xyz}$|
|\tilde{xy}|$\tilde{xy}$|\widetilde{xyz}|$\widetilde{xyz}$|
|\check{x}|$\check{x}$|\breve{y}|$\breve{y}$|
|\grave{x}|$\grave{x}$|\acute{y}|$\acute{y}$|
#### 连线符号
|输入|显示|
|:-:|:-:|
|\fbox{a+b+c+d}|$\fbox{a+b+c+d}$|
|\overleftarrow{a+b+c+d}|$\overleftarrow{a+b+c+d}$|
|\overrightarrow{a+b+c+d}|$\overrightarrow{a+b+c+d}$|
|\overleftrightarrow{a+b+c+d}|$\overleftrightarrow{a+b+c+d}$|
|\underleftarrow{a+b+c+d}|$\underleftarrow{a+b+c+d}$|
|\underrightarrow{a+b+c+d}|$\underrightarrow{a+b+c+d}$|
|\underleftrightarrow{a+b+c+d}|$\underleftrightarrow{a+b+c+d}$|
|\overline{a+b+c+d}|$\overline{a+b+c+d}$|
|\underline{a+b+c+d}|$\underline{a+b+c+d}$|
|\overbrace{a+b+c+d}^{Sample}|$\overbrace{a+b+c+d}^{Sample}$|
|\underbrace{a+b+c+d}\_{Sample}|$\underbrace{a+b+c+d}_{Sample}$|
|\overbrace{a+\underbrace{b+c}\_{1.0}+d}^{2}|$\overbrace{a+\underbrace{b+c}_{1.0}+d}^{2.0}$|
|\underbrace{a\cdot a\cdots a}\_{b\text{ times}}|$\underbrace{a\cdot a\cdots a}_{b\text{ times}}$|
#### 箭头符号
|输入|显示|输入|显示|
|:--:|:--:|:--:|:--:|
|\to|$\to$|\mapsto|$\mapsto$|
|\implies|$\implies$|\impliedby|$\impliedby$|
|\uparrow|$\uparrow$|\Uparrow|$\Uparrow$|
|\downarrow|$\downarrow$|\Downarrow|$\Downarrow$|
|\leftarrow|$\leftarrow$|\Leftarrow|$\Leftarrow$|
|\rightarrow|$\rightarrow$|\Rightarrow|$\Rightarrow$|
|\leftrightarrow|$\leftrightarrow$|\Leftrightarrow|$\Leftrightarrow$|
|\longleftarrow|$\longleftarrow$|\Longleftarrow|$\Longleftarrow$|
|\longrightarrow|$\longrightarrow$|\Longrightarrow|$\Longrightarrow$|
|\longleftrightarrow|$\longleftrightarrow$|\Longleftrightarrow|$\Longleftrightarrow$|
|\iff|$\iff$|||
#### 标准函数名
|输入|显示|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|:-:|:-:|
|\arccos|$\arccos$|\arcsin|$\arcsin$|arctan|$\arctan$|
|\arg|$\arg$|\cos|$\cos$|\cosh|$\cosh$|
|\cot|$\cot$|\coth|$\coth$|\csc|$\csc$|
|\deg|$\deg$|\det|$\det$|\dim|$\dim$|
|\exp|$\exp$|\gcd|$\gcd$|\hom|$\hom$|
|\inf|$\inf$|\ker|$\ker$|\lg|$\lg$|
|\lim|$\lim$|\liminf|$\liminf$|\limsup|$\limsup$|
|\ln|$\ln$|\log|$\log$|\max|$\max$|
|\min|$\min$|\Pr|$\Pr$|\sec|$\sec$|
|\sin|$\sin$|\sinh|$\sinh$|\sup|$\sup$|
|\tan|$\tan$|\tanh|$\tanh$|||
#### 数学字体
|输入|说明|显示|
|:-:|:-:|:-:|
|\mathit{A}|意大利体|$\mathit{A}$ $\mathit{B}$ $\mathit{C}$ $\mathit{R}$ $\mathit{a}$ $\mathit{b}$ $\mathit{c}$ $\mathit{r}$ $\mathit{1}$ $\mathit{2}$ $\mathit{3}$ $\mathit{4}$|
|\mathrm{A}|罗马体|$\mathrm{A}$ $\mathrm{B}$ $\mathrm{C}$ $\mathrm{R}$ $\mathrm{a}$ $\mathrm{b}$ $\mathrm{c}$ $\mathrm{r}$ $\mathrm{1}$ $\mathrm{2}$ $\mathrm{3}$ $\mathrm{4}$|
|\mathcal{A}|花体|$\mathcal{A}$ $\mathcal{B}$ $\mathcal{C}$ $\mathcal{R}$ $\mathcal{a}$ $\mathcal{b}$ $\mathcal{c}$ $\mathcal{r}$ $\mathcal{1}$ $\mathcal{2}$ $\mathcal{3}$ $\mathcal{4}$|
|\mathbf{A}|粗体|$\mathbf{A}$ $\mathbf{B}$ $\mathbf{C}$ $\mathbf{R}$ $\mathbf{a}$ $\mathbf{b}$ $\mathbf{c}$ $\mathbf{r}$ $\mathbf{1}$ $\mathbf{2}$ $\mathbf{3}$ $\mathbf{4}$|
|\mathbb{A}|黑板粗体|$\mathbb{A}$ $\mathbb{B}$ $\mathbb{C}$ $\mathbb{R}$ $\mathbb{a}$ $\mathbb{b}$ $\mathbb{c}$ $\mathbb{r}$ $\mathbb{1}$ $\mathbb{2}$ $\mathbb{3}$ $\mathbb{4}$|
|\mathsf{A}|等线字体|$\mathsf{A}$ $\mathsf{B}$ $\mathsf{C}$ $\mathsf{R}$ $\mathsf{a}$ $\mathsf{b}$ $\mathsf{c}$ $\mathsf{r}$ $\mathsf{1}$ $\mathsf{2}$ $\mathsf{3}$ $\mathsf{4}$|
|\mathtt{A}|打字机体|$\mathtt{A}$ $\mathtt{B}$ $\mathtt{C}$ $\mathtt{R}$ $\mathtt{a}$ $\mathtt{b}$ $\mathtt{c}$ $\mathtt{r}$ $\mathtt{1}$ $\mathtt{2}$ $\mathtt{3}$ $\mathtt{4}$|
|\mathfrak{A}|旧德式字体|$\mathfrak{A}$ $\mathfrak{B}$ $\mathfrak{C}$ $\mathfrak{R}$ $\mathfrak{a}$ $\mathfrak{b}$ $\mathfrak{c}$ $\mathfrak{r}$ $\mathfrak{1}$ $\mathfrak{2}$ $\mathfrak{3}$ $\mathfrak{4}$|
#### 文字字体
|输入|说明|显示|
|:-:|:-:|:-:|
|\it{Sample}|意大利体|$\it{Sample}$|
|\rm{Sample}|罗马体|$\rm{Sample}$|
|\cal{Sample}|花体|$\cal{Sample}$|
|\bf{Sample}|粗体|$\bf{Sample}$|
|\Bbb{Sample}|黑板粗体|$\Bbb{SAMPLE}$|
|\sf{Sample}|等线字体|$\sf{Sample}$|
|\tt{Sample}|打字机体|$\tt{Sample}$|
|\frak{Sample}|旧德式字体|$\frak{Sample}$|
#### 数学字号
|输入|显示|
|:-:|:-:|
|{\displaystyle \int f(x-x_a)\,dx}|${\displaystyle \int f(x-x_a)\,dx}$|
|{\textstyle \int f(x-x_a)\,dx}|${\textstyle \int f(x-x_a)\,dx}$|
|{\scriptstyle \int f(x-x_a)\,dx}|${\scriptstyle \int f(x-x_a)\,dx}$|
|{\scriptscriptstyle \int f(x-x_a)\,dx}|${\scriptscriptstyle \int f(x-x_a)\,dx}$|
#### 文字字号
|输入|显示|
|:-:|:-:|
|\tiny{smallest}|$\tiny{smallest}$|
|\scriptsize{very small}|$\scriptsize{very small}$|
|\footnotesize{smaller}|$\footnotesize{smaller}$|
|\small{small}|$\small{small}$|
|\normalsize{normal}|$\normalsize{normal}$|
|\large{large}|$\large{large}$|
|\Large{Large}|$\Large{Large}$|
|\LARGE{LARGE}|$\LARGE{LARGE}$|
|\huge{huge}|$\huge{huge}$|
|\Huge{Huge}|$\Huge{Huge}$|
#### 文字颜色
|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|
|black|$\color{black}{text}$|grey|$\color{grey}{text}$|
|silver|$\color{silver}{text}$|white|$\color{white}{text}$|
|maroon|$\color{maroon}{text}$|red|$\color{red}{text}$|
|yellow|$\color{yellow}{text}$|lime|$\color{lime}{text}$|
|olive|$\color{olive}{text}$|green|$\color{green}{text}$|
|teal|$\color{teal}{text}$|auqa|$\color{auqa}{text}$|
|blue|$\color{blue}{text}$|navy|$\color{navy}{text}$|
|purple|$\color{purple}{text}$|fuchsia|$\color{fuchsia}{text}$|
#### 其它符号
|输入|显示|输入|显示|
|:-:|:-:|:-:|:-:|
|\LaTeX|$\LaTeX$|\TeX|$\TeX$|
|\circledS|$\circledS$|\copyright|$\copyright$|

[返回目录](#目录)
### 使用参考
#### 基本公式
- 上下标`^` `_`
  $$x^{y^z}=(1+{\rm e}^x)^{-2xy^w}$$
- 分数`\frac{分子}{分母}`
  $$x_1,x_2=\frac{b^2\pm 4ac}{2a}$$
  $$\frac{1}{2}\dfrac{1}{2}$$
  $$\frac{1}{2}\tfrac{1}{2}$$
- 开方`\sqrt[根指数，省略时为2]{被开方数}`
  $$\sqrt{2}$$
  $$\sqrt[n]{3}$$
- 省略号`\dots` `\cdots` `\ldots`
  $$1,2,\dots$$
  $$f(x_1,x_2,\underbrace{\ldots}_{\rm ldots},x_n)=x_1^2+x_2^2+\underbrace{\cdots}_{\rm cdots}+x_n^2$$
- 矢量`\vec{矢量}`
  $$\vec{a}\cdot\vec{b}=0$$
- 极限`\lim_{变量 \to 表达式} 表达式`
  $$\lim_{n\to +\infty}\frac{1}{n(n+1)}$$
  $$\lim_{x\leftarrow -\infty}\frac{1}{n(n+1)}$$
- 积分`\int_{积分下限}^{积分上限}{被积表达式}`
  $$\int_{-\infty}^{+\infty}f(x)\mathrm{d}x$$
- 双重积分`\iint`
  $$\iint_{-\infty}^{+\infty}f(x,y)\mathrm{d}x\mathrm{d}y$$
- 圆圈积分`\oint`
  $$\oint_{-\infty}^{+\infty}f(x)\mathrm{d}x$$
- 行内积分`\int_{}^{}`
  $\int_{-\infty}^{+\infty}f(x)\mathrm{d}x$
- 行内积分limits模式`\int\limits_{}^{}`
  $\int\limits_{-\infty}^{+\infty}f(x)\mathrm{d}x$
- 行内积分display模式`\displaystyle\int_{}^{}`
  $\displaystyle \int_{-\infty}^{+\infty}f(x)\mathrm{d}x$
- 求和`\sum_{下标表达式}^{上标表达式}{累加表达式}`
  $$\sum_{i=1}^{n}i^2$$
- 累乘`\prod`
  $$\prod_{i=1}^{n}a_i$$
- 并集`\bigcup`
  $$\bigcup_{i=1}^{2}R$$
- 交集`\bigcap`
  $$\bigcap_{i=1}^{2}R$$
- 行内求和`\sum_{}^{}`
  $\sum_{i=1}^{n}i^2$
- 行内求和limits模式`\sum\limits_{}^{}`
  $\sum\limits_{i=1}^{n}i^2$
- 行内求和display模式`\displaystyle\sum_{}^{}`
  $\displaystyle\sum_{i=1}^{n}i^2$
- 连分数`\cfrac`
  $$x=a_0+\cfrac{1^2}{a_1+\cfrac{2^2}{a_2+\cfrac{3^2}{a_3+\cfrac{4^4}{a_4+\cdots}}}}$$
- 模块`$$\begin{}...\end{}$$`，使用`&`分隔同行元素，`\\`换行
  $$
  \begin{matrix}
    1 & x & x^2 \\
    1 & y & y^2 \\
    1 & z & z^2 \\
  \end{matrix}
  $$
- 大括号和行标`\left` `\right` `\tag{行标}`
  $$
  f\left(
    \left[
      \frac{
        1+\left\{x,y\right\}
      }{
        \left(
            \frac{x}{y}+\frac{y}{x}
        \right)
        \left(u+1\right)
      }+a
    \right]^{3/2}
  \right)
  \tag{1}
  $$
  $$
  \begin{aligned}
    a= & \left(1+2+3+\cdots\right. \\
    ~ & \cdots+\left.\infty-2+\infty-1+\infty\right)
  \end{aligned}
  $$
- 定义新的符号`\operatorname{新符号}`
  $$\operatorname{Symbol}A$$
- 添加注释文字`\text{文字}`
  $$
  f(n)=
  \begin{cases}
    n/2, & \text{if $n$ is even} \\
    3n+1, & \text{if $n$ is odd}
  \end{cases}
  $$
- 在字符间加入空格`\,` `\;` `\quad` `\qquad`
  $$a\,b\mid a\;b\mid a\quad b\mid a\qquad b$$
- 更改文字颜色`\color{颜色}{文字}`
  $$
  \begin{array}{|rrrr|}
  \hline
  \verb+#000+ & \color{#000}{text} & ~ & ~ \\
  \verb+#00F+ & \color{#00F}{text} & ~ & ~ \\
  ~ & ~ & \verb+#0F0+ & \color{#0F0}{text} \\
  ~ & ~ & \verb+#0FF+ & \color{#0FF}{text} \\
  \verb+#F00+ & \color{#F00}{text} & ~ & ~ \\
  \verb+#F0F+ & \color{#F0F}{text} & ~ & ~ \\
  ~ & ~ & \verb+#FF0+ & \color{#FF0}{text} \\
  ~ & ~ & \verb+#FFF+ & \color{#FFF}{text} \\
  \hline
  \end{array}
  $$
  $$
  \begin{array}{|rrrr|}
  \hline
  \verb+#000+ & \color{#000}{text} & \verb+#005+ & \color{#005}{text} \\
  \verb+#00A+ & \color{#00A}{text} & \verb+#00F+ & \color{#00F}{text} \\
  \verb+#500+ & \color{#500}{text} & \verb+#505+ & \color{#505}{text} \\
  \verb+#50A+ & \color{#50A}{text} & \verb+#50F+ & \color{#50F}{text} \\
  \verb+#A00+ & \color{#A00}{text} & \verb+#A05+ & \color{#A05}{text} \\
  \verb+#A0A+ & \color{#A0A}{text} & \verb+#A0F+ & \color{#A0F}{text} \\
  \verb+#F00+ & \color{#F00}{text} & \verb+#F05+ & \color{#F05}{text} \\
  \verb+#F0A+ & \color{#F0A}{text} & \verb+#F0F+ & \color{#F0F}{text} \\
  \hline
  \verb+#080+ & \color{#080}{text} & \verb+#085+ & \color{#085}{text} \\
  \verb+#08A+ & \color{#08A}{text} & \verb+#08F+ & \color{#08F}{text} \\
  \verb+#580+ & \color{#580}{text} & \verb+#585+ & \color{#585}{text} \\
  \verb+#58A+ & \color{#58A}{text} & \verb+#58F+ & \color{#58F}{text} \\
  \verb+#A80+ & \color{#A80}{text} & \verb+#A85+ & \color{#A85}{text} \\
  \verb+#A8A+ & \color{#A8A}{text} & \verb+#A8F+ & \color{#A8F}{text} \\
  \verb+#F80+ & \color{#F80}{text} & \verb+#F85+ & \color{#F85}{text} \\
  \verb+#F8A+ & \color{#F8A}{text} & \verb+#F8F+ & \color{#F8F}{text} \\
  \hline
  \verb+#0F0+ & \color{#0F0}{text} & \verb+#0F5+ & \color{#0F5}{text} \\
  \verb+#0FA+ & \color{#0FA}{text} & \verb+#0FF+ & \color{#0FF}{text} \\
  \verb+#5F0+ & \color{#5F0}{text} & \verb+#5F5+ & \color{#5F5}{text} \\
  \verb+#5FA+ & \color{#5FA}{text} & \verb+#5FF+ & \color{#5FF}{text} \\
  \verb+#AF0+ & \color{#AF0}{text} & \verb+#AF5+ & \color{#AF5}{text} \\
  \verb+#AFA+ & \color{#AFA}{text} & \verb+#AFF+ & \color{#AFF}{text} \\
  \verb+#FF0+ & \color{#FF0}{text} & \verb+#FF5+ & \color{#FF5}{text} \\
  \verb+#FFA+ & \color{#FFA}{text} & \verb+#FFF+ & \color{#FFF}{text} \\
  \hline
  \end{array}
  $$
- 片段删除线`\cancel{字符}` `\bcancel{字符}` `\xcancel{字符}`
  $$
  \begin{array}{rl}
    \verb|y+\cancel{x}| & y+\cancel{x} \\
    \verb|\cancel{y+x}| & \cancel{y+x} \\
    \verb|y+\bcancel{x}| & y+\bcancel{x} \\
    \verb|y+\xcancel{x}| & y+\xcancel{x}
  \end{array}
  $$
- 字体转换`{\字体 {需转换的部分字符}}`
  |Bad|Better|
  |:-:|:-:|
  |$\int_0^1 x^2 dx$|$\int_0^1 x^2 \,{\rm d}x$|
#### 矩阵
- 无框矩阵`matrix`
  $$
  \begin{matrix}
    1 & x & x^2 \\
    1 & y & y^2 \\
    1 & z & z^2 \\
  \end{matrix}
  $$
- 有框矩阵`*matrix`
  |输入|显示|输入|显示|
  |:-:|:-:|:-:|:-:|
  |matrix|$\begin{matrix} 1 & 2 \\ 3 & 4 \\ \end{matrix}$|pmatrix|$\begin{pmatrix} 1 & 2 \\ 3 & 4 \\ \end{pmatrix}$|
  |bmatrix|$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ \end{bmatrix}$|Bmatrix|$\begin{Bmatrix} 1 & 2 \\ 3 & 4 \\ \end{Bmatrix}$|
  |vmatrix|$\begin{vmatrix} 1 & 2 \\ 3 & 4 \\ \end{vmatrix}$|Vmatrix|$\begin{Vmatrix} 1 & 2 \\ 3 & 4 \\ \end{Vmatrix}$|
- 带省略符号的矩阵`\cdots` `\ddots` `\vdots`
  $$
  \begin{pmatrix}
    1 & a_1 & a_1^2 & \cdots & a_1^n \\
    1 & a_2 & a_2^2 & \cdots & a_2^n \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    1 & a_m & a_m^2 & \cdots & a_m^n \\
  \end{pmatrix}
  $$
- 行中矩阵`\bigl(\begin{smallmatrix}...\end{smallmatrix}\bigr)`
  $\bigl(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix} \bigr)$
#### 数组
- 无框数组`array`，对齐分割`{l|c|r}`
  $$
  \begin{array}{l|c|r}
    200\tau & 7\phi-\frac{5}{12} & \frac{\alpha}{2} \\
    \frac{3}{\psi} & \frac{\pi}8 & 100\beta
  \end{array}
  $$
- 有框数组`\left` `\right`
  $$
  \left( 
    \begin{array}{cc}
      2\tau & 7\phi-\frac{5}{12} \\
      \frac{3}{\psi} & \frac{\pi}8
    \end{array}
  \right)
  $$
- 半框数组`\left.` `\right.`
  $$
  \left\{ 
    \begin{array}{c}
      a_1x+b_1y+c_1z=d_1 \\
      a_2x+b_2y+c_2z=d_2 \\
      a_3x+b_3y+c_3z=d_3
    \end{array}
  \right. 
  $$
  $$
  \left.
    \begin{array}{ll}
      \text{if $n$ is even:} & n/2 \\
      \text{if $n$ is odd:} & 3n+1
    \end{array}
  \right\}
  =f(n)
  $$
- 条件表达式`cases`
  $$
  f(n)=
  \begin{cases}
    n/2,  & \text{if $n$ is even} \\
    3n+1, & \text{if $n$ is odd}
  \end{cases}
  $$
- 数组嵌套
  $$
  \begin{array}{c}
    \begin{array}{cc}
      \begin{array}{c|cccc}
        \text{min} & 0 & 1 & 2 & 3 \\
        \hline
        0 & 0 & 0 & 0 & 0 \\
        1 & 0 & 1 & 1 & 1 \\
        2 & 0 & 1 & 2 & 2 \\
        3 & 0 & 1 & 2 & 3
      \end{array}
      &
      \begin{array}{c|cccc}
        \text{max}& 0 & 1 & 2 & 3 \\
        \hline
        0 & 0 & 1 & 2 & 3 \\
        1 & 1 & 1 & 2 & 3 \\
        2 & 2 & 2 & 2 & 3 \\
        3 & 3 & 3 & 3 & 3
      \end{array}
    \end{array}
    \\
    \begin{array}{c|cccc}
      \Delta & 0 & 1 & 2 & 3 \\
      \hline
      0 & 0 & 1 & 2 & 3 \\
      1 & 1 & 0 & 1 & 2 \\
      2 & 2 & 1 & 0 & 1 \\
      3 & 3 & 2 & 1 & 0
    \end{array}
  \end{array}
  $$
#### 注意事项
- 在以`e`为底的指数函数、极限和积分中尽量不要使用`\frac`，它会使整段函数看起来很怪，而且可能产生歧义。也正是因此它在专业数学排版中几乎从不出现。横着写这些分式，中间使用斜线间隔`/`（用斜线代替分数线）
  |Bad|Better|
  |:-:|:-:|
  |$e^{i\frac{\pi}2}\quad e^{\frac{i\pi}2}$|$e^{i\pi/2}$|
  |$\int_{-\frac\pi2}^\frac\pi 2\sin x\,dx$|$\int_{-\pi/2}^{\pi/2}\sin x\,dx$|
- 使用多重积分符号时，不要多次使用`\int`来声明，直接使用`\iint`来表示二重积分，使用`\iiint`来表示三重积分等。对于无限次积分，可以用`\int\cdots\int`表示
  |Bad|Better|
  |:-:|:-:|
  |$\int\int_S f(x)\,dy\,dx$|$\iint_S f(x)\,dy\,dx$|
  |$\int\int\int_V f(x)\,dz\,dy\,dx$|$\iiint_V f(x)\,dz\,dy\,dx$|
  |无限次积分|$\int\cdots\int$|
- 在微分符号前加入`\,`来插入一个小的间隔空隙；没有`\,`符号的话，$\TeX$将会把不同的微分符号堆在一起
  |Bad|Better|
  |:-:|:-:|
  |$\iiint_V f(x){\rm d}z {\rm d}y {\rm d}x$|$\iiint_V f(x)\,{\rm d}z\,{\rm d}y\,{\rm d}x$|
- `|`符号在被当作分隔符时会产生错误的间隔，因此在需要分隔时最好使用`\mid`来代替它
  $$
  \begin{array}{cc}
    \mathrm{Bad} & \mathrm{Better} \\
    \hline \\
    \{x|x^2\in\Bbb Z\} & \{x\mid x^2\in\Bbb Z\} \\
  \end{array}
  $$

[返回目录](#目录)
## 其它
### Github图片引用方式
#### 语法
```
仓库地址/raw/分支名/图片路径
```
>说明
>- 语法为引用其他Github仓库中的图片
>- 如果引用本仓库中的图片，直接使用相对路径就可以了
#### 示例
![PyTorch](https://github.com/pytorch/pytorch/raw/master/docs/source/_static/img/pytorch-logo-dark.png "pytorch")

[返回目录](#目录)
### HTML
- 折叠
  <details>
  <summary>折叠内容一</summary>
  <p>markdown支持内嵌html，这里只举几个实用例子</p>
  </details>
  <details>
  <summary>折叠内容二</summary>
  <p>markdown不支持折叠，可以采用内嵌html语法实现</p>
  </details>
- 居中
  <div align="center"><p>实现文本居中显示</p></div>
- 图片尺寸
  <div align="center"><img width="100px" src="./img/csdn.png" /></div>
- 空格
  |语法|示例|
  |-|-|
  |`&nbsp;`|小空格&nbsp;测试|
  |`&#160;`|小空格&#160;测试|
  |`&ensp;`|半空格&ensp;测试|
  |`&#8194;`|半空格&#8194;测试|
  |`&emsp;`|全空格&emsp;测试|
  |`&#8195;`|全空格&#8195;测试|
  |`&emsp;&emsp;`|双空格&emsp;&emsp;测试|

[返回目录](#目录)
***

<h2 id='postscript'>后记</h2>

**缺少**
- mermaid

[返回目录](#目录)
***

[Baidu]:https://www.baidu.com/ "百度"
[CSDN]:https://www.csdn.net/ "CSDN"
[Baidu-logo]:http://www.baidu.com/img/bdlogo.gif "百度logo"
[CSDN-logo]:./img/csdn.png "CSDNlogo"
[emoji]:./emoji.md "emoji"
[^note]:脚注的名字是随意的
