# 首页配置
# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
# 首页标题
#SIMPLEUI_HOME_TITLE = '百度一下你就知道'
# 首页图标,支持element-ui的图标和fontawesome的图标
# SIMPLEUI_HOME_ICON = 'el-icon-date'

# 设置simpleui 点击首页图标跳转的地址
#SIMPLEUI_INDEX = 'https://www.88cto.com'

# 首页是否显示服务器、python、django、simpleui相关信息
SIMPLEUI_HOME_INFO = False

# 首页显示快速操作
SIMPLEUI_HOME_QUICK = True

# 首页显示最近动作
SIMPLEUI_HOME_ACTION = True

# 自定义SIMPLEUI的Logo
# SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'

# 登录页粒子动画，默认开启，False关闭
# SIMPLEUI_LOGIN_PARTICLES = False

# simpleui是否收集相关信息
SIMPLEUI_ANALYSIS = False

# 自定义simpleui 菜单
# SIMPLEUI_CONFIG = {
#     'system_keep': True,  # 在自定义菜单的基础上保留系统模块
#     'menus': [
#         {
#             'name': 'Simpleui',
#             'icon': 'fas fa-code',
#             'url': 'https://gitee.com/tompeppa/simpleui'
#         },
#         {
#             'name': '搜索引擎',
#             'icon': 'fa fa-list',
#             'models': [{
#                 'name': '百度',
#                 'url': 'http://baidu.com',
#                 'icon': 'fa fa-list'
#             }, {
#                 'name': '谷歌',
#                 'url': 'https://google.com',
#                 'icon': 'fa fa-list'
#             }]
#         }]
# }

# 是否显示默认图标，默认=True
# SIMPLEUI_DEFAULT_ICON = False

# 图标设置，图标参考：
# SIMPLEUI_ICON = {
#     '员工管理': 'fas fa-user-tie'
# }

# 指定simpleui 是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目
# 不填该项或者为False的时候，默认从第三方的cdn获取
SIMPLEUI_STATIC_OFFLINE = True

# 默认主题 设置
SIMPLEUI_DEFAULT_THEME = 'purple.css'
