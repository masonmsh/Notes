# git
- [git](#git)
  - [安装](#安装)
    - [配置](#配置)
  - [本地仓库](#本地仓库)
    - [初始化](#初始化)
    - [本地推送](#本地推送)
    - [回滚](#回滚)
    - [本地查看](#本地查看)
      - [查看状态](#查看状态)
      - [查看修改](#查看修改)
      - [查看日志](#查看日志)
      - [查看历史命令](#查看历史命令)
  - [远程仓库](#远程仓库)
    - [SSH](#ssh)
    - [克隆](#克隆)
    - [添加远程仓库](#添加远程仓库)
    - [删除远程仓库](#删除远程仓库)
    - [远程推送](#远程推送)
    - [远程查看](#远程查看)
      - [查看信息](#查看信息)
  - [分支管理](#分支管理)
    - [创建分支](#创建分支)
    - [查看分支](#查看分支)
    - [切换分支](#切换分支)
    - [合并分支](#合并分支)
    - [删除分支](#删除分支)
  - [标签管理](#标签管理)
    - [创建标签](#创建标签)
    - [查看标签](#查看标签)
    - [合并标签](#合并标签)
    - [删除标签](#删除标签)
    - [推送标签](#推送标签)
## 安装
### 配置
```
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```
## 本地仓库
### 初始化
```
git init
```
### 本地推送
**工作目录** -> **暂存区**
```
git add <file/dir>
```
**暂存区** -> **本地仓库**
```
git commit -m "message"
```
**本地仓库** -> **暂存区**
```
git reset HEAD <file>
```
**暂存区** -> **工作目录**
```
git checkout -- <file>
```
### 回滚
```
git reset --hard HEAD^
```
> 当前版本`HEAD`，上一个版本`HEAD^`，上上一个版本`HEAD^^`，往上100个版本`HEAD~100`，或者直接使用`commit-id`
### 本地查看
#### 查看状态
```
git status
```
#### 查看修改
```
git diff
```
#### 查看日志
```
git log
```
#### 查看历史命令
```
git reflog
```
## 远程仓库
### SSH
```
ssh-keygen -t rsa -C "youremail@example.com"
```
> 如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。
### 克隆
```
git clone git@github.com:xxx/xxx.git
```
**ssh https**
```
git@github.com:xxx/xxx.git
https://github.com/xxx/xxx.git
```
### 添加远程仓库
```
git remote add origin git@github.com:xxx/xxx.git
```
### 删除远程仓库
```
git remote rm origin
```
### 远程推送
**本地仓库** -> **远程仓库**
```
git push -u origin master
git push origin master
git push
```
**远程仓库** -> **本地仓库**
```
git pull origin master
git fetch
```
### 远程查看
#### 查看信息
```
git remote -v
```
## 分支管理
### 创建分支
```
git branch <branch>
git checkout -b <branch>
git switch -c <branch>
```
### 查看分支
```
git branch
```
### 切换分支
```
git checkout <branch>
git switch <branch>
```
### 合并分支
```
git merge <branch>
```
### 删除分支
```
git branch -d <branch>
git branch -D <branch>
```
## 标签管理
### 创建标签
```
git tag <tagname>
git tag -a <tagname> -m "message"
```
### 查看标签
```
git tag
git show <tagname>
```
### 合并标签
```
git tag <tagname> <commit-id>
```
### 删除标签
```
it tag -d <tagname>
git push origin :refs/tags/<tagname>
```
### 推送标签
```
git push origin <tagname>
git push origin --tags
```