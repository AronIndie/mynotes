# 登录
git config --global user.name "yangruipis"
git config --global user.email "595403043@qq.com"
# 新建本地仓库并上传
cd existing_folder
git init
git remote add origin git@code.aliyun.com:595403043/test.git
git add .
git commit
git push -u origin master

# 本地与云端冲突时
在 git push 之前：
git pull --rebase origin master

# 云端下载仓库
git clone git@code.aliyun.com:595403043/test.git
cd test
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
# 本地修改后上传进行更新
git add .
git commit
git push -u origin master
# 云端修改后覆盖本地
git fetch --all
git reset --hard origin/master

# 本地修改后与云端合并
git pull

# 分支操作
1. 创建并切换分支
git branch dev     # 创建分支dev
git checkout dev   # 切换到分支dev
上述两个命令等价于git checkout -b dev
2. 查看当前分支
git branch
3. 用当前分支提交
git add readme.txt 
git commit -m "branch test"
    [dev fec145a] branch test
    1 file changed, 1 insertion(+)
4. 我们把dev分支的工作成果合并到master分支上：
git checkout master
git merge dev
5. 合并后即可删除dev分支
git branch -d dev

# .gitignore 文件
git目录下加入.gitignore文件
```
# 此为注释 – 将被 Git 忽略
*.a       # 忽略所有 .a 结尾的文件
!lib.a    # 但 lib.a 除外
/TODO     # 仅仅忽略项目根目录下的 TODO 文件，不包括 subdir/TODO
build/    # 忽略 build/ 目录下的所有文件
doc/*.txt # 会忽略 doc/notes.txt 但不包括 doc/server/arch.txt
```

## 如果已经push过然后想加ignore
，但是有时候在项目开发过程中，突然心血来潮想把某些目录或文件加入忽略规则，按照上述方法定义后发现并未生效，原因是.gitignore只能忽略那些原来没有被track的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。那么解决方法就是先把本地缓存删除（改变成未track状态），然后再提交：

```
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
```