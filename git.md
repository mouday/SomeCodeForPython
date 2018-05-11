版本管理工具git

# git简介
分类

    集中式：cvs，svn
    分布式：git
    托管网站：github

下载

    git官网: https://git-scm.com/
    国内镜像：https://npm.taobao.org/mirrors/git-for-windows/

linux常用指令

    新建：mkdir dirname
    进入：cd dirname
    当前：pwd
    文件列表：ls
    查看：cat readme.txt
    编辑：vim readme.txt
    删除：rm readme.txt

git配置

    指定用户名和地址
    git config --global user.name "Your Name"
    git config --global user.email "email@example.com"
    git config --global color.ui true # 显示颜色

创建版本库

    初始化仓库：git init
    添加到暂存区：git add filename
    提交更改：git commit -m "message"
    查看状态：git status
    查看不同：git diff
    查看工作区和版本库里面最新版本的区别:
    git diff HEAD -- readme.txt

# 时光穿梭
提交历史

    git log  
    git log --pretty=oneline
    git log --graph --pretty=oneline --abbrev-commit
    命令历史：git reflog

版本回退

    回退到上一版本：git reset --hard HEAD^
    HEAD表示当前版本指针，往上多个版本：HEAD~100
    回到指定版本：git reset --hard 版本号
    
工作区和暂存区

    工作区(Working Directory) -> 版本库(Repository)(暂存区stage -> master)

撤销删除

    丢弃工作区的修改:git checkout -- file
    撤销暂存区的修改:git reset HEAD file
    删除版本库文件：git rm 删掉，并且git commit

# 远程仓库：
创建SSH Key

    ssh-keygen -t rsa -C "youremail@example.com"
    默认值即可
    路径：用户主目录/.ssh目录
    github 添加公钥

克隆项目： 

    https协议：git clone https://github.com/mouday/demo.git
    ssh协议：git clone git@github.com:mouday/demo.git
    关联远程仓库：git remote add origin git@github.com:username/gitname.git

拉取推送

    提交到远端：git push -u origin master
    -u参数关联本地和远程分支，用于第一次推送

    推送master分支到远端： git push origin master

    拉取分支：git pull

# 分支管理
创建与合并分支

    查看分支：git branch
    创建分支：git branch <name>
    切换分支：git checkout <name>
    创建+切换分支：git checkout -b <name>
    合并某分支到当前分支：git merge <name>
    删除分支：git branch -d <name>
    不使用Fast forward模式合并：git merge --no-ff -m "merge with no-ff" dev

bug分支

    存储当前现场：git stash
    查看：git stash list
    恢复现场：git stash apply
    删除存储：git stash drop
    恢复并删除：git stash pop

    强制删除有被合并过的分支：git branch -D <name>

多人协作

    查看远程库的信息: git remote
    详细的信息:git remote -v

    创建本地dev分支： git checkout -b dev origin/dev
    建立关联：git branch --set-upstream-to=origin/dev dev

    多人协作： 推送 -> 失败则拉取 -> 解决冲突 -> 本地提交 -> 再推送 

# 标签管理
创建标签

    查看标签：git tag
    设置标签：git tag <tagname> [commit id]
    查看标签信息:git show <tagname>
    指定标签信息:git tag -a <tagname> -m "blablabla..." [commit id]
    用PGP签名标签:git tag -s <tagname> -m "blablabla..." [commit id]

操作标签

    推送一个本地标签：git push origin <tagname>
    推送全部未推送过的本地标签：git push origin --tags
    删除一个本地标签：git tag -d <tagname>
    删除一个远程标签：git push origin :refs/tags/<tagname>

# 自定义git
忽略特殊文件

    .gitignore   https://github.com/github/gitignore
    强制添加：git add -f App.class
    检查规则：git check-ignore -v App.class

配置别名
    
    git config --global alias.st status
    
    仓库的Git配置文件  .git/config
    当前用户的Git配置文件  用户主目录/.gitconfig

# 经验建议

    每次提交前记得diff，以免提交错误代码
    下班回家前，整理好自己的工作区
    并行的项目，使用分支开发
    遇到冲突，搞明白原因，不要随意丢弃别人的代码
    产品发布后，记得打tag，方便将来拉分支修复bug

>参考：
>
> 1. [Git教程 - 廖雪峰](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
> 2. [常用 Git 命令清单 - 阮一峰](http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html)
> 3. [廖老师网站上总结的Git笔记](https://github.com/hongiii/gitNotes_from_Liao/blob/master/gitNotes_from_Liao.md)