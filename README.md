# VulnScanner

## centos7 环境配置

```shell
# 系统更新  
sudo yum update -y

```

### pyenv

```shell
# 安装 pyenv 配置 python 版本管理
# 安装依赖
sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel liblzma-devel
# 下载源码
git clone https://github.com/pyenv/pyenv.git  ~/.pyenv
# 添加环境变量, 配置在下面代码块
vim ~/.bash_profile
# 使配置生效
source ~/.bash_profile


```

```shell
# pyenv 使用
# 查看帮助
pyenv --help
# 更新, 安装 pyenv 后先执行这一步
pyenv rehash
# 查看已安装的版本
pyenv versions
# 查看可安装的版本
pyenv install --list
# 安装指定的版本
pyenv install 3.9.9
# 设置为当前全局版本
pyenv global 3.9.9
# 卸载指定的版本
pyenv uninstall 3.9.9
# 查看当前使用的版本
pyenv version
# 查看已下载的版本
pyenv versions
# 查看可下载的版本
pyenv install --list
```

```text
## 在 ~/.bash_profile 尾部添加如下配置
## pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

### xray
    github: https://github.com/chaitin/xray
    下载页面: https://stack.chaitin.com/tool/detail/1

```shell
# 安装配置 xray
wget https://ctstack-oss.oss-cn-beijing.aliyuncs.com/tool_file/5916b4a8b4b668945b01e0ca10100dec.zip
unzip -d xray 5916b4a8b4b668945b01e0ca10100dec.zip
cd xray
# 生成配置和证书
./xray_linux_amd64 genca
# 添加环境变量, 配置文件在下方
vim ~/.bash_profile
# 使环境变量生效
source ~/.bash_profile
# xray 爬虫主动漏扫
./xray_linux_amd64 webscan --basic-crawler http://testphp.vulnweb.com/ --html-output xray-crawler-testphp.html
```

```text
# 在  ~/.bash_profile 尾部添加如下配置
## xray
export XRAY_HOME=~/xray
export XRAY_CMD=xray_linux_amd64
```

```shell
# 解决一些依赖问题
# 配置 libpcap.so.0.8 依赖
sudo ln -s /usr/lib64/libpcap.so.1.5.3 /usr/lib/libpcap.so.0.8

```

```shell
# 探针配置
# 依赖配置
pip install requests --user
# 降级 urllib3
pip uninstall urllib3
pip install urllib4==1.25.3

cd ~
mkdir probe
cd probe
# 下载探针
wget http://192.168.3.78:5500/probe.py
# 启动探针
pyhon probe.py

```