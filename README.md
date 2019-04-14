# -
饿了么商家数据爬虫
'''
本程序作者：GallenQiu
仅供个人学习，禁止用于商业用途
'''
使用方法：
    首先：在run.py同级文件夹里新建一个cookies.txt的空文件
    首先：在run.py同级文件夹里新建一个cookies.txt的空文件
    首先：在run.py同级文件夹里新建一个cookies.txt的空文件
    一、配置数据库：
    （本爬虫采用MySQL数据库）
    进入eleme_mysql.py,修改数据库连接、密码、端口，数据库名、数据表名（需要提前建立含有字段的数据库）

    二、配置地理位置：
    在run.py中找到如下代码：
    ' def __init__(self):
        self.latitude = 22.52680
        self.longitude = 113.93082'
     通过谷歌地图找到你所需要位置的经纬度，替换上面的经纬度即可
    
    三、修改爬取页数：
    在run.py中找到如下代码：
    '#修改爬取页数(乘以8)
        maxpage=31
        for i in range(0, int(maxpage)):
            page_num = i * 8
            self.main_parse(page_num)'
            
    四、爬取：
    运行run.py开始抓取商家数据（只包含商家名字、商品名字和商品月销量，需要添加其他字段请参考json文件自行修改）
    （第一次运行会要求填入手机号获取验证码，之后cookies保存在cookies.txt文件中）

备注：本爬虫抓取端口是手机H5页面，仅是单线程抓取，速度很慢，后续会更新异步版本。
所需要的支持库：mysql_connector、requests
