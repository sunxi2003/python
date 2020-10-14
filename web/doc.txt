web框架 flask

参考资料： https://www.liaoxuefeng.com/wiki/1016959663602400/1017806472608512

首页：   http://localhost:5000
登录：   http://localhost:5000/signin
        用户名：admin   口令： password

MVC：Model-View-Controller
      处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；
      包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
      Model是用来传给View, 从Model中取出相应的数据。