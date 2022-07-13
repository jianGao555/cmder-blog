# cmder-blog
跟着ysh老师git和github项目
创建虚拟环境 可以使用anaconda（先下载anaconda）
然后在命令提示符（cmd）里执行conda create -n envsname(虚拟环境的名字) python=3.6
然后激活虚拟环境 执行 conda activate envsname(虚拟环境的名字) （虚拟环境激活后最左边会显示虚拟环境的名字）
接着在虚拟环境里 pip install requirements.txt
然后在虚拟环境里执行 python manage.py migrate 用于创建数据库
然后进行缓存表的创建：python manage.py createcachetable
python manage.py createsuperuser 用于创建管理员用户（需要记住用户名和密码）
最后执行Python manage.py runserver 就可以在本地激活项目
在浏览器输入 http://127.0.0.1:8000/ 就可以看到项目前端
在浏览器输入 http://127.0.0.1:8000/admin/ 就可以看到项目后台
