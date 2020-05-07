![page_img_url](https://www.sabia.cc/wp-content/uploads/2017/11/python-pip.jpg)

### pip是什么

我们都知道Python很强大，实用性也非常高，其很重要的一个原因就是因为有非常丰富的第三方库类，而pip是Python的的依赖包管理工具，该工具提供了对Python包的查找、下载、安装、卸载等的功能。基本使用到的包都可以在[https://pypi.org/](https://pypi.org/)上面搜索找到。

### 安装pip

具体的安装方法可以查看官网的安装说明

官方安装说明地址：[https://pip.pypa.io/en/latest/installing/#id7](https://pip.pypa.io/en/latest/installing/#id7)

Windows的用户，需要先到官网下载get-pip.py安装包，然后执行`python get-pip.py`进行安装

而如果需要在Linux上安装的话，则比较方便和快捷的，直接可以通过yum或者apt-get安装即可

yum安装
```
sudo yum install python-pip
```
apt-get安装
```
sudo apt-get install python-pip
```

更多安装方法请安装文档：[https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)

### 查看pip版本

简写方式
```
pip -V
```

完整命令方式
```
pip --version
```

### 利用pip安装模块

```
pip install [module_name]
```

### 查看所有已安装的模块

```
pip list
```

如果需要搜索指定的模块的话，可以使用下面的命令

```
pip search [module_name]
```

还可以使用下面的方法（PS：好像不是全起作用）

```
pip list | grep [module_name]
```

### 查看已安装的某个模块的详细信息

```
pip show --files [module_name]
```

### 检查哪些模块需要更新

```
pip list --outdated
```

### 升级指定的模块

```
 pip install --U [module_name]
```

### 卸载已经安装的模块

```
pip uninstall [module_name]
```

### 需要查看更多pip的用法

```
pip --help
```

### 更新pip本身

Windows的用户执行下面的命令

```
python -m pip install -U pip
```

Linux或者Mac OS的用户执行下面的命令

```
pip install -U pip
```
