# Supply Chain后端服务代码结构

```
/
├── bootstrap                  // django或者其他框架启动是的调用代码，比如gevent的monkey_patch等项目初始化代码
├── command                    // 保存命令行工具，项目相关的脚步, 脚本比较多的情况下需要分目录保存
│   └── management             // 如果是django的项目保存django的命令行工具
│       └── commands
├── constant                   // 放置枚举，按照功能和模块划分成不同的文件
├── deploy                     // 发布相关的配置
│   ├── api.json
│   ├── celerybeat.json
│   ├── celery.json
│   └── requirements.txt       // 项目依赖
├── lib                        // 公共库
├── manage.py                  // django的启东脚步, 非django项目不需要
├── manager                    // 业务逻辑的代码, service和model的中间层
├── middleware                 // 中间件
├── model                      // 数据库模型和接口模型
│   ├── jsonschema             // 接口的jsonschema定义, 可以按照功能模块分文件和目录
│   └── db                     // 数据库模型, 可以按照功能模块分文件和目录
│       └── sqlschema.sql      // 数据库建表语句
├── readme.md                  // 项目说明
├── setting                    // 配置文件目录; 不同功能模块配置需要按文件分开
│   ├── common                 // 保存公共的配置，不区分环境
│   ├── live                   // live环境的特殊配置
│   ├── uat                    // uat环境的特殊配置
│   ├── staging                // staging环境的配置
│   ├── test                   // test环境的配置
│   └── local.py               // 开发的本地配置
│── service                    // 业务代码，view和manager的中间层
├── settings.py                // 配置的入口文件
├── startup                    // 启动目录
│   ├── celery.py
│   ├── gunicorn.config.py
│   ├── jenkins.config.py
│   └── wsgi.py
├── task                       // celery异步任务的目录; 需要按照功能划分文件
├── templates                  // 模板文件需要按照功能划分目录
│   └── templatetags           // django的模板扩展
├── urls.py                    // url路由文件
├── view                       // view层代码，需要按照功能模块划分文件和目录
└── web                        // 前端相关文件
    └── static                 // 静态资源和js库
```
