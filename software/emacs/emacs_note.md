# command notes


| command                   | desc                                                |
| --------------            | -------                                             |
| M-x package-list-packages | 更新软件包，按x执行                                 |
| M-x recover-file          | 恢复文件（从自动保存文件中#test.py#）               |
| M-x recover-this-file     | 恢复文件（从自动保存文件中#test.py#） C-x u少量撤销 |
| M-x revert-buffer         | 恢复到上次保存时候的样子                            |



## emacs + jupyter

==注意：所有路径，文件名必须为英文，否则出现[warn] Kernal not work（类似）的错误 ==
1. 现开jupyter端口，用bash，获取端口号和密码，密码即token
2. emacs: M-x ein:notebooklist-login，输入端口号和密码
3. emacs: M-x ein:notebooklist-open，打开notebook
4. 命令：
| command       | desc                                                                 |   |
|---------------|----------------------------------------------------------------------|---|
| C-c C-k       | 剪切cell                                                             |   |
| C-c C-n 或C-p | 上下跳cell                                                           |   |
| C-c C-l       | 清除该cell的output                                                   |   |
| C-c C-y       | 粘贴cell                                                             |   |
| C-c M-w       | 复制cell                                                             |   |
| C-c C-a/C-b   | 上/下方插入cell                                                      |   |
| C-c C-u       | 输入'c'为code模式，输入'm'为markdown模式，还有'r(aw)'，和'h(eading)' |   |
| C-c C-q       | 关闭所有notebook并且关闭kernal                                       | ' |



## 奇技淫巧


1. C-c m c 多重游标
2. C-x ( 开始录制宏；C-x ) 结束录制宏 C-x e 运行宏 C-u 10 C-x e运行10次宏
3. C-c > 打开日历
4. 想绑定键位，但是不知道命令怎么写时：
    - M-x global-set-key RET 输入键位 RET 输入函数功能，如(set-mark-command)

    - C-x Esc Esc 查看上一次复杂命令，得到详细的绑定键位命令，复制到init.el文件中

5. C-c C-x c RET 数字 ：复制多少次
6. C-c C-x C-v orgmode 打开图片
7. org-mode下C-c C-d插入日期
8. 选中当前行 C-c l 我自己定义的，（python中直接C-c运行当前行）
9. latex中的自动提示，如\footnote[]{}，光标调到[]上，按C-d删除当前可选的[]
10. spacemacs添加包：
    - 在.spacemacs文件中的dotspacemacs-additional-packages '(需要加载的包)里填入需要加载的包
    - 在.spacemacs文件中的dotspacemacs/user-config ()函数中写入(require 该包)或者是(use-package 该包)

## org-mode

| command      | desc         |
|--------------|--------------|
| C-c C-z      | 添加note     |
| C-c C-t _    | 切换状态     |
| S-left/right | 切换状态     |
| C-c C-d      | 插入deadline |
| C-c C-s      | 插入starline   |

tips:
- 显示图片：引用前面加上file\:，可以相对引用，也可以绝对引用，但是不可加description，否则无法正常显示。之后按`C-c C-x C-v`显示图片
- latex公式显示： `C-u C-u C-c C-x C-l`，全部不显示`C-c C-c`
- python运行：1. `C-c C-p`打开ipython终端；2. `C-u C-c C-c` 运行python文件（包括main函数）或者`C-c C-c`运行python文件（不包括main函数）
  

