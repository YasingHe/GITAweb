<img src="https://ftp.bmp.ovh/imgs/2021/07/154f6992e578a960.png" alt="logo" width="40%" height="40%" align="right">

# Galaxy Information Technology Association web

**天河信息社官方网站**

## **概括**

- 本网站采用`Python`的`Django`框架进行编写
- 额外模块有`simpleui`、`ckeditor`、`pillow`,运行前必须确保安装了这些模块


## **运行**
### **配置环境**

安装 Django

```
$ pip install django 
```
>如果下载太慢可以加 `-i https://pypi.tuna.tsinghua.edu.cn/simple `参数换源，例如:
```
$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django
```

安装simpleui

```
$ pip install django-simpleui 
```
安装ckeditor

```
$ pip install django-ckeditor
```

安装pillow

```
pip install pillow
```


### **迁移数据库**
```
$ python manage.py makemigrations
$ python manage.py migrate
```
### **创建超级用户**`(可通过:IP/admin 进入管理后台)`
```
$ python manage.py createsuperuser
```
- 会提示输入用户名，这个是登录时要用的
- 电子邮件可填可不填，直接回车就行
- 接着会提示设置密码，密码不可见，放心输入两边即可

### **运行程序**
0.0.0.0:80是为了让其他设备也可以访问，不加只能在本机访问,`请确保在运行前执行了前面的所有步骤`，以后运行时只需要输入下面这行命令即可，如果你对`模型或者表单做了更改，需要先迁移数据库`才能运行!

```
python manage.py runserver 0.0.0.0:80
```

### **访问地址**

>本地在 `127.0.0.1` 访问，如果想要通过别的设备访问地址为: `服务端IP`

<br>
<br>

## **特别申明**

> 本人前端技术不是很好，对html，css，js看着头大，所以目前的前端页面不太好，如果对前端有好的想法可以在`issue`提出
<br>
<br>

**`copyright@天河信息社`**
