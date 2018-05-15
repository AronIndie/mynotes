<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [ss并且开机启动](#ss并且开机启动)
    - [0. 安装shadowsocks](#0-安装shadowsocks)
    - [1. 建立配置文件ss.json](#1-建立配置文件ssjson)
    - [2. 建立sh文件，用以运行](#2-建立sh文件用以运行)
    - [3. 开机自动启动](#3-开机自动启动)
        - [3.1 首先载启动文件`/etc/rc.local`中加入](#31-首先载启动文件etcrclocal中加入)
        - [3.2 添加服务](#32-添加服务)
- [双硬盘时，机械硬盘挂载](#双硬盘时机械硬盘挂载)
    - [1. 格式化硬盘为EXT4](#1-格式化硬盘为ext4)
    - [2. 分区](#2-分区)
    - [3. 挂载](#3-挂载)
    - [4. 开机自动挂载](#4-开机自动挂载)
- [添加字体](#添加字体)
    - [1. 安装依赖](#1-安装依赖)
    - [2. 下载对应的字体文件，并且放到指定位置](#2-下载对应的字体文件并且放到指定位置)
    - [3. 建立缓存](#3-建立缓存)
- [安装 latex](#安装-latex)
- [双显卡驱动](#双显卡驱动)
    - [1. 安装](#1-安装)
    - [2. 防止启动后无法进入图形界面](#2-防止启动后无法进入图形界面)
    - [3. 测试](#3-测试)
    - [4. 两种用法](#4-两种用法)
- [docker + pyspark + jupyter 安装](#docker--pyspark--jupyter-安装)
    - [1. 本地安装docker](#1-本地安装docker)
        - [1.1 安装docker包](#11-安装docker包)
        - [1.2 防止权限问题，加入用户权限](#12-防止权限问题加入用户权限)
        - [1.3 重启服务（或者重启计算机）](#13-重启服务或者重启计算机)
        - [1.4 查看安装是否成功](#14-查看安装是否成功)
    - [2 配置spark 镜像(images)和容器(containers)](#2-配置spark-镜像images和容器containers)
        - [首先，直接建立容器，如果镜像不存在，则会自动下载：](#首先直接建立容器如果镜像不存在则会自动下载：)
        - [其次，查看docker状态](#其次查看docker状态)
        - [最后，直接打开或是关闭](#最后直接打开或是关闭)
    - [3 推荐的pyspark docker](#3-推荐的pyspark-docker)
- [安装 ZSH](#安装-zsh)
    - [1. 安装zsh](#1-安装zsh)
    - [2. 安装 oh-my-zsh](#2-安装-oh-my-zsh)
    - [3. 设置为默认shell](#3-设置为默认shell)
    - [4. 添加powerline](#4-添加powerline)
- [tensorflow 环境搭建](#tensorflow-环境搭建)
    - [1. 双显卡切换为独显](#1-双显卡切换为独显)
    - [2. 安装CUDA](#2-安装cuda)
        - [2.1 yaourt 安装](#21-yaourt-安装)
        - [2.2 加入环境变量](#22-加入环境变量)
        - [2.3 验证安装](#23-验证安装)
    - [3. cuDNN安装](#3-cudnn安装)
    - [4. 安装tensorflow-gpu版本](#4-安装tensorflow-gpu版本)
    - [5. 安装keras](#5-安装keras)
- [linux备份](#linux备份)
    - [0. 权限问题](#0-权限问题)
    - [1. 备份](#1-备份)
    - [2. 恢复](#2-恢复)

<!-- markdown-toc end -->


# ss并且开机启动

## 0. 安装shadowsocks

```
sudo pip install shadowsocks 
```

## 1. 建立配置文件ss.json

我的位置是：/home/ray/Documents/shadowsocks/ss.json
```python
{
    "server":"*.*.*.*",
    "server_port":***,
    "local_port":1081,
    "password":"*****",
    "timeout":600,
    "method":"aes-256-cfb"
}
```
## 2. 建立sh文件，用以运行

我的位置是：/home/ray/Documents/shadowsocks/ss.sh

```bash
#!/bin/bash
#ss.sh
/home/ray/anaconda3/bin/sslocal -c /home/ray/Documents/shadowsocks/ss.json 

echo "connected!"
```
**注意**，如果是开机启动会出现:"sslocal 未知的命令"的情况，一定要附上绝对路径，或者加入环境变量。

不要忘记增加可执行权限：
```bash
sudo chmod +x ss.sh
```

测试：打开终端后，运行: sh /home/ray/Documents/shadowsocks/ss.sh，不报错就成功了

## 3. 开机自动启动

### 3.1 首先载启动文件`/etc/rc.local`中加入 

```bash
sh /home/ray/Documents/shadowsocks/ss.sh
```

增加权限：
```bash
sudo chmod +x /etc/rc.local
```
重启，如果可以翻墙最好，如果不行则考虑步骤3.2

### 3.2 添加服务
新建文件：`/usr/lib/systemd/system/rc-local.service`，在其中加入：
```bash
[Unit]
Description=/etc/rc.local Compatibility
ConditionPathExists=/etc/rc.local
[Service]
ExecStart=/etc/rc.local
[Install]
WantedBy=multi-user.target
```

之后在终端运行：
```bash
systemctl enable rc-local.service    # 允许该服务，使其可以开机自运行
systemctl start rc-local.service    # 启动该服务
systemctl status rc-local.service   # 查看服务状态
```
如果发现服务状态没有异常，则搞定了，重启即可

# 双硬盘时，机械硬盘挂载

## 1. 格式化硬盘为EXT4
如果时windows过来的NTFS，一定要进行格式化，否则无法写入

```bash
fdisk -l   # 列出所有分区，找到想要格式化的分区名，如/dev/sda1
sudo mkfs -t ext4 /dev/sda1   # 格式化完成
```

## 2. 分区
```bash
sudo fdisk /dev/sda     #格式化后名称为/dev/sda
```
输入n、p、1、两下回车、wq、回车，分成一个区

## 3. 挂载

```bash
# 新建文件夹作为挂载点
mkdir /home/ray/Documents/Data

# 给定写入权限
chown -R 500:ray /run/media/ray/data/
sudo chown ray:ray /run/media/ray/data/

# 挂载
sudo mount -t ext4 /dev/sda1 /home/ray/Documents/Data/
```

## 4. 开机自动挂载
```bash
sudo gedit /etc/fstab
```

加入：
```
/dev/sda1 /home/ray/Documents/Data ext4 defaults 0 2 
```

# 添加字体
## 1. 安装依赖
```bash
sudo pacman -S fontconfig
```
## 2. 下载对应的字体文件，并且放到指定位置
- 微软雅黑：https://pan.baidu.com/s/1pL5asEv 
- 放入/usr/share/fonts/my_fonts/中

## 3. 建立缓存 

mkfontscale 
mkfontdir 
fc-cache -fv

# 安装 latex

```bash
# 安装底层（最后一个用于解决bibtex的问题）
sudo pacman -S texlive-core texlive-langchinese texlive-latexextra texlive-publishers

# 安装IDE
sudo pacman -S texstudio

# 更新texlive
texhash
```

# 双显卡驱动
manjaro装机之后的显卡驱动切换程序：Bumblebee还是有点问题，我们重新安装
## 1. 安装
```bash
# 依赖
sudo pacman -S virtualgl lib32-virtualgl lib32-primus primus

# 安装双显卡切换程序bumblebee
sudo mhwd -f -i pci video-hybrid-intel-nvidia-bumblebee

# 允许服务
sudo systemctl enable bumblebeed

# 添加用户
sudo gpasswd -a $USER bumblebee
```    

## 2. 防止启动后无法进入图形界面
1. 打开 /etc/default/grub
2. 找到并且改为：GRUB_CMLINE_LINUX_DEFAULT="quiet **acpi_osi=! acpi_osi=Linux acpi_osi=’Windows 2015’ pcie_port_pm=off** resume=..."
3. 运行sudo update-grub，重启

## 3. 测试

```bash
# 安装测试软件
sudo pacman -S mesa-demos

# 集成显卡性能
glxgears -info

# 独显性能
optirun glxgears -info
# 或者
primusrun glxgears -info
```

之后所有需要用独显允许的程序，前面都要加上optirun或者primusrun允许

```bash
# 打开nvida面板
optirun -b none nvidia-settings -c :8

# 不依赖Bumblebee来使用CUDA
sudo tee /proc/acpi/bbswitch <<< ‘ON’

# 使用完CUDA 停止NVIDIA显卡
sudo rmmod nvidia_uvm nvidia && sudo tee /proc/acpi/bbswitch <<< OFF
```

```bash
inxi -G # 查看显卡情况

optirun nvidia-smi # 查看CPU情况
```

## 4. 两种用法
1. 用bumblebee切换：
命令前面加上 optirun 或者primusrun运行
2. 用bbswitch:

```bash
# 一直开启独显
sudo tee /proc/acpi/bbswitch <<< ‘ON’
# 一直禁用独显
sudo tee /proc/acpi/bbswitch <<< ‘OFF’
```


# docker + pyspark + jupyter 安装

参考： [http://maxmelnick.com/2016/06/04/spark-docker.html](http://maxmelnick.com/2016/06/04/spark-docker.html)
## 1. 本地安装docker

### 1.1 安装docker包
```bash
sudo pacman -S docker
```

### 1.2 防止权限问题，加入用户权限
```bash
sudo usermod -aG docker ray
```

### 1.3 重启服务（或者重启计算机）

```bash
sudo systemctl restart docker
```

### 1.4 查看安装是否成功
```bash
sudo docker -info
```

## 2 配置spark 镜像(images)和容器(containers)

### 首先，直接建立容器，如果镜像不存在，则会自动下载：

```
sudo docker run -d -p 8888:8888 --name spark -v $PWD:/home/jovyan/work jupyter/all-spark-notebook start-notebook.sh --NotebookApp.password='sha1:5b1e121347e8:15266c00b25c2e497714de20a674d5b8935e09dd'
```

命令解释：

- docker run 载镜像基础上建立容器
- -d 后台运行
- -p 8888:8888 指定端口
- -- name spark 命名容器
- -v $PWD:/home/jovyan/work 挂载 all-spark-notebook的工作目录到当前目录，使得文件可以在docker内外共享（jovyan是该镜像内置的用户名，不要更改！）
- jupyter/all-spark-notebook 镜像名称，来自[https://hub.docker.com/r/jupyter/all-spark-notebook/](https://hub.docker.com/r/jupyter/all-spark-notebook/)
- start-notebook.sh --NotebookApp.password='sha1:5b1e121347e8:15266c00b25c2e497714de20a674d5b8935e09dd' 指定密码而不是token，密码先得转为hash码（[怎么转](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html#preparing-a-hashed-password)）


在浏览器中输入'http://localhost:8888'，即可打开容器对应的notebook

### 其次，查看docker状态

```
# 显示当前容器
docker ps

# 显示所有容器
docker ps -a

# 显示所有镜像 
docker images

# 删除容器
docker rm container_name

# 删除镜像，必须先删除依赖该镜像的容器
docker rmi image_name

```

### 最后，直接打开或是关闭

```
# 关闭容器
docker stop spark

# 打开容器
docker start spark

```

## 3 推荐的pyspark docker
- [pyspark-notebook](https://hub.docker.com/r/jupyter/pyspark-notebook/)
- [all-spark-notebook](https://hub.docker.com/r/jupyter/all-spark-notebook/)


# 安装 ZSH

zsh，shell中的极品（[为什么](https://www.zhihu.com/question/21418449)）

## 1. 安装zsh

```
sudo pacman -S git, zsh
```

## 2. 安装 oh-my-zsh
oh-my-zsh是zsh的一个封装，类似spacemacs和emacs的关系

```
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

记着将`.bashrc`中添加的语句复制到`.zshrc`中

## 3. 设置为默认shell

```
chsh -s /bin/zsha
```

## 4. 添加powerline

```
pip install git+git://github.com/powerline/powerline
```

然后将
```
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /usr/local/lib/python2.7/dist-packages/powerline/bindings/zsh/powerline.zsh
```
添加到`.zshrc`中，注意powerline的位置不一定是上面的，需要自行更改

最后重启



# tensorflow 环境搭建


我们的配置是：

- CUDA-8.0
- cuDNN-6
- tensorflow-gpu 1.4

## 1. 双显卡切换为独显

独显必须一直保持开着的状态，才可以稳定运行cuda等程序，我们通过`bbswitch`切换独显

```bash
sudo tee /proc/acpi/bbswitch <<< ‘ON’
```

注意，如果`nvidia-smi -pm`为1的话上述方法是无效的，必须变为0，即实时切换状态

```
nvidia-smi -pm 0
```

## 2. 安装CUDA

### 2.1 yaourt 安装

```
yaourt -S cuda-8.0
```

如果遇到yaourt报告空间不够，则：

1. 打开`/etc/yaourtrc`
2. 将 `#TMPDIR="/tmp"` 改为`TMPDIR="/home/$USER/tmp"即可`


### 2.2 加入环境变量

通过安装日志可以发现，yaourt将安装包迁移到了`/opt`中，因此我们在 `.bashrc`或`.zshrc`、以及`/etc/profile`中加入：

```
export CUDA_HOME=/opt/cuda
export PATH=/opt/cuda/bin:$PATH
export LD_LIBRARY_PATH=/opt/cuda/lib64:$LD_LIBRARY_PATH
```

### 2.3 验证安装

查看CUDA版本
```
nvcc -V
```

编译samples，CUDA安装时自带了samples文件夹，进入该文件夹后直接编译（gcc啥的都给你装好了），但是一定记得用sudo，否则报错

```
cd /opt/cuda/samples

sudo make
```

查看编译结果：

```
cd bin/x86_64/linux/release


./deviceQuery    # 最后如果返回pass，则通过

./bandwidthTest    # 最后如果返回pass，则通过

reboot            # 最好重启一下
```


恭喜你，到了这一步，CUDA已经顺利安装完成啦！！

## 3. cuDNN安装

cuDNN是nivida提供的深度学习GPU库，在manjaro下非常好安装：

```
# 先确定独显是开着的
sudo tee /proc/acpi/bbswitch <<< ‘ON’

yaourt -S cudnn6
```


装好之后，将cudnn文件拷贝到cuda中：

```
sudo cp /opt/cudnn6/include/cudnn.h /opt/cuda/include
sudo cp cudnn6/lib64/libcudnn* /opt/cuda/lib64

# 增加权限
sudo chmod a+r cuda/include/cudnn.h
sudo chmod a+r cuda/include/cudnn.h
```

恭喜，至此你已经完成了准备工作啦！


## 4. 安装tensorflow-gpu版本


为了跟CUDA8兼容，我们安装1.4版本的tensorflow-gpu

```
pip install tensorflow-gpu==1.4
```

**重启，很关键***

```
reboot 
```

重启之后，打开ipython，输入命令进行测试：

```python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
```

如果提示中不包含`ERROR`或`FAIL`字样，且包含了你的独显名称，那么就是正确安装了。


最后设置CPU按需求使用，在每次导入tf时：

```python
# 设置tendorflow对显存使用按需增长。
import tensorflow as tf
config  = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
```


## 5. 安装keras

```
pip install keras
```

keras默认使用tensorflow后端，并且会直接调用其GPU，因此无需做任何改动


# linux备份

## 0. 权限问题

```
 sudo gedit /etc/rsyncd.conf
```
将其中的
```
uid = nobody
gid = nobody
```
改为
```
uid = root 
gid = root
```

**备份结束之后一定要改回来！！**
## 1. 备份
```
sudo time rsync -Pa / /run/media/ray/Elements/LinuxBackup/2018_05_10 --exclude="/sys/*" --exclude="/proc/*" --exclude="/mnt/*" --exclude="/tmp/*" --exclude="/run/media/*"
```

## 2. 恢复

```
sudo rsync -Pa /run/media/ray/Elements/LinuxBackup/2018_05_10 /
```
