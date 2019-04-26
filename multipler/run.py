from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor

from multipler.db_eleme import db
from login import Login

import requests,json

from DBUtils.PooledDB import PooledDB
import mysql.connector
'''初始化mysql连接池'''
print('初始化数据库池中。。。')
pool = PooledDB(mysql.connector,4,host='localhost',user='root',passwd='199756',db='eleme',port=3306) #4为连接池里的最少连接数



#爬虫模块：先采用线程池获取商店id填充到id_list里，再调用parse_html函数单线程获取详情商品信息。
class Eleme:
    def __init__(self):
        #参数设置：
        self.page_num=20#实际店家=page_num*8
        self.latitude = 39.99287
        self.longitude = 116.31025

        self.headers = ''
        self.id_list = []
        self.nlist=Queue()


    # 登陆模块：检测cookies.txt是否为空，是的话就调用Login函数登陆。
    def login(self):
        while True:
            with open('cookies.txt', 'r')as f:
                lines = f.readlines()
                if lines != []:
                    cookies1 = 'track_id=' + str(lines[2].replace('\n', '')) + '; USERID=' + str(
                        lines[1].replace('\n', '')) + '; UTUSER=' + str(lines[1].replace('\n', '')) + '; SID=' + str(
                        lines[0].replace('\n', '')) + ';'
                    self.headers = {
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'zh-CN,zh;q=0.9',
                        'cookie': cookies1,
                        'referer': 'https://h5.ele.me/msite/food/',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Mobile Safari/537.36',
                        'x-shard': 'loc=114.10957,22.54362', }
                    break
                else:
                    L = Login()
                    L.send()
    def test_ck(self,page_num):
            url='https://h5.ele.me/restapi/shopping/v3/restaurants?latitude='+str(self.latitude)+'&longitude='+str(self.longitude)+'&keyword=&offset='+str(page_num)+'&limit=8&extras[]=activities&extras[]=tags&terminal=h5&rank_id=10fe946cb6b440ad8c386796b921a79b&brand_ids[]=&restaurant_category_ids[]=209&restaurant_category_ids[]=212&restaurant_category_ids[]=214&restaurant_category_ids[]=266&restaurant_category_ids[]=267&restaurant_category_ids[]=268&restaurant_category_ids[]=269&restaurant_category_ids[]=354&restaurant_category_ids[]=362&restaurant_category_ids[]=370&restaurant_category_ids[]=378&restaurant_category_ids[]=386&restaurant_category_ids[]=394&restaurant_category_ids[]=402&restaurant_category_ids[]=410&restaurant_category_ids[]=418&restaurant_category_ids[]=426&restaurant_category_ids[]=434&restaurant_category_ids[]=442&restaurant_category_ids[]=450&restaurant_category_ids[]=458&restaurant_category_ids[]=466&restaurant_category_ids[]=474&restaurant_category_ids[]=482&restaurant_category_ids[]=490&restaurant_category_ids[]=498&restaurant_category_ids[]=746&restaurant_category_ids[]=754&restaurant_category_ids[]=762&restaurant_category_ids[]=770&restaurant_category_ids[]=778&restaurant_category_ids[]=786&restaurant_category_ids[]=794&restaurant_category_ids[]=802&restaurant_category_ids[]=810&restaurant_category_ids[]=818&restaurant_category_ids[]=826&restaurant_category_ids[]=834&restaurant_category_ids[]=842&restaurant_category_ids[]=850&restaurant_category_ids[]=858&restaurant_category_ids[]=866&restaurant_category_ids[]=874&restaurant_category_ids[]=882&restaurant_category_ids[]=890&restaurant_category_ids[]=898&restaurant_category_ids[]=906&restaurant_category_ids[]=914&restaurant_category_ids[]=922&restaurant_category_ids[]=930&restaurant_category_ids[]=938&restaurant_category_ids[]=946&restaurant_category_ids[]=954&restaurant_category_ids[]=221&restaurant_category_ids[]=222&restaurant_category_ids[]=223&restaurant_category_ids[]=224&restaurant_category_ids[]=225&restaurant_category_ids[]=226&restaurant_category_ids[]=227&restaurant_category_ids[]=228&restaurant_category_ids[]=232&restaurant_category_ids[]=263&restaurant_category_ids[]=506&restaurant_category_ids[]=514&restaurant_category_ids[]=522&restaurant_category_ids[]=530&restaurant_category_ids[]=538&restaurant_category_ids[]=546&restaurant_category_ids[]=554&restaurant_category_ids[]=562&restaurant_category_ids[]=570&restaurant_category_ids[]=578&restaurant_category_ids[]=586&restaurant_category_ids[]=594&restaurant_category_ids[]=602&restaurant_category_ids[]=610&restaurant_category_ids[]=618&restaurant_category_ids[]=626&restaurant_category_ids[]=634&restaurant_category_ids[]=642&restaurant_category_ids[]=650&restaurant_category_ids[]=658&restaurant_category_ids[]=666&restaurant_category_ids[]=674&restaurant_category_ids[]=682&restaurant_category_ids[]=690&restaurant_category_ids[]=698&restaurant_category_ids[]=706&restaurant_category_ids[]=218&restaurant_category_ids[]=234&restaurant_category_ids[]=236&restaurant_category_ids[]=962&restaurant_category_ids[]=970&restaurant_category_ids[]=978&restaurant_category_ids[]=986&restaurant_category_ids[]=994&restaurant_category_ids[]=1002&restaurant_category_ids[]=1010&restaurant_category_ids[]=1018&restaurant_category_ids[]=1026&restaurant_category_ids[]=1034&restaurant_category_ids[]=240&restaurant_category_ids[]=241&restaurant_category_ids[]=242&restaurant_category_ids[]=249&restaurant_category_ids[]=250&restaurant_category_ids[]=714&restaurant_category_ids[]=722&restaurant_category_ids[]=730&restaurant_category_ids[]=738&restaurant_category_ids[]=346&restaurant_category_ids[]=1042&restaurant_category_ids[]=1050&restaurant_category_ids[]=1058&restaurant_category_ids[]=1066&restaurant_category_ids[]=1074&restaurant_category_ids[]=1082&restaurant_category_ids[]=1090&restaurant_category_ids[]=1098&restaurant_category_ids[]=1106&restaurant_category_ids[]=1114&restaurant_category_ids[]=1122&restaurant_category_ids[]=1130&restaurant_category_ids[]=1138&restaurant_category_ids[]=1146&restaurant_category_ids[]=1154&restaurant_category_ids[]=1162&restaurant_category_ids[]=1170&restaurant_category_ids[]=1178&restaurant_category_ids[]=1186&restaurant_category_ids[]=1194&restaurant_category_ids[]=1202&restaurant_category_ids[]=1210&restaurant_category_ids[]=1218&restaurant_category_ids[]=1226&restaurant_category_ids[]=1234&restaurant_category_ids[]=1250&restaurant_category_ids[]=1258&restaurant_category_ids[]=1266&restaurant_category_ids[]=1274&restaurant_category_ids[]=1282&restaurant_category_ids[]=1290&restaurant_category_ids[]=1298&restaurant_category_ids[]=1306&restaurant_category_ids[]=1314&restaurant_category_ids[]=1322&restaurant_category_ids[]=1330&restaurant_category_ids[]=1338&restaurant_category_ids[]=1346&restaurant_category_ids[]=1354&restaurant_category_ids[]=1362&order_by=12'
            response=requests.get(url,headers=self.headers)
            if '未登录' in response.text:
                raise KeyError

    def scheduler(self):
        self.login()
        try:
            self.test_ck(0)
            print('登陆成功！')
        except:
            print('cookies失效，重新登陆！')
            L = Login()
            L.send()
            self.scheduler()

        for i in range(0, int( self.page_num)):
            page_num = i * 8
            self.nlist.put(page_num)

        pool1 = ThreadPoolExecutor(max_workers=10)
        while int(self.nlist.qsize()) > 0:
            pool1.submit(self.parse_url, self.nlist.get())
        pool1.shutdown()
        print('一共：'+str(len(self.id_list))+'家店。')

        self.parse_html()

    # 多线程解析商店id
    def parse_url(self,page_num):
            url='https://h5.ele.me/restapi/shopping/v3/restaurants?latitude='+str(self.latitude)+'&longitude='+str(self.longitude)+'&keyword=&offset='+str(page_num)+'&limit=8&extras[]=activities&extras[]=tags&terminal=h5&rank_id=10fe946cb6b440ad8c386796b921a79b&brand_ids[]=&restaurant_category_ids[]=209&restaurant_category_ids[]=212&restaurant_category_ids[]=214&restaurant_category_ids[]=266&restaurant_category_ids[]=267&restaurant_category_ids[]=268&restaurant_category_ids[]=269&restaurant_category_ids[]=354&restaurant_category_ids[]=362&restaurant_category_ids[]=370&restaurant_category_ids[]=378&restaurant_category_ids[]=386&restaurant_category_ids[]=394&restaurant_category_ids[]=402&restaurant_category_ids[]=410&restaurant_category_ids[]=418&restaurant_category_ids[]=426&restaurant_category_ids[]=434&restaurant_category_ids[]=442&restaurant_category_ids[]=450&restaurant_category_ids[]=458&restaurant_category_ids[]=466&restaurant_category_ids[]=474&restaurant_category_ids[]=482&restaurant_category_ids[]=490&restaurant_category_ids[]=498&restaurant_category_ids[]=746&restaurant_category_ids[]=754&restaurant_category_ids[]=762&restaurant_category_ids[]=770&restaurant_category_ids[]=778&restaurant_category_ids[]=786&restaurant_category_ids[]=794&restaurant_category_ids[]=802&restaurant_category_ids[]=810&restaurant_category_ids[]=818&restaurant_category_ids[]=826&restaurant_category_ids[]=834&restaurant_category_ids[]=842&restaurant_category_ids[]=850&restaurant_category_ids[]=858&restaurant_category_ids[]=866&restaurant_category_ids[]=874&restaurant_category_ids[]=882&restaurant_category_ids[]=890&restaurant_category_ids[]=898&restaurant_category_ids[]=906&restaurant_category_ids[]=914&restaurant_category_ids[]=922&restaurant_category_ids[]=930&restaurant_category_ids[]=938&restaurant_category_ids[]=946&restaurant_category_ids[]=954&restaurant_category_ids[]=221&restaurant_category_ids[]=222&restaurant_category_ids[]=223&restaurant_category_ids[]=224&restaurant_category_ids[]=225&restaurant_category_ids[]=226&restaurant_category_ids[]=227&restaurant_category_ids[]=228&restaurant_category_ids[]=232&restaurant_category_ids[]=263&restaurant_category_ids[]=506&restaurant_category_ids[]=514&restaurant_category_ids[]=522&restaurant_category_ids[]=530&restaurant_category_ids[]=538&restaurant_category_ids[]=546&restaurant_category_ids[]=554&restaurant_category_ids[]=562&restaurant_category_ids[]=570&restaurant_category_ids[]=578&restaurant_category_ids[]=586&restaurant_category_ids[]=594&restaurant_category_ids[]=602&restaurant_category_ids[]=610&restaurant_category_ids[]=618&restaurant_category_ids[]=626&restaurant_category_ids[]=634&restaurant_category_ids[]=642&restaurant_category_ids[]=650&restaurant_category_ids[]=658&restaurant_category_ids[]=666&restaurant_category_ids[]=674&restaurant_category_ids[]=682&restaurant_category_ids[]=690&restaurant_category_ids[]=698&restaurant_category_ids[]=706&restaurant_category_ids[]=218&restaurant_category_ids[]=234&restaurant_category_ids[]=236&restaurant_category_ids[]=962&restaurant_category_ids[]=970&restaurant_category_ids[]=978&restaurant_category_ids[]=986&restaurant_category_ids[]=994&restaurant_category_ids[]=1002&restaurant_category_ids[]=1010&restaurant_category_ids[]=1018&restaurant_category_ids[]=1026&restaurant_category_ids[]=1034&restaurant_category_ids[]=240&restaurant_category_ids[]=241&restaurant_category_ids[]=242&restaurant_category_ids[]=249&restaurant_category_ids[]=250&restaurant_category_ids[]=714&restaurant_category_ids[]=722&restaurant_category_ids[]=730&restaurant_category_ids[]=738&restaurant_category_ids[]=346&restaurant_category_ids[]=1042&restaurant_category_ids[]=1050&restaurant_category_ids[]=1058&restaurant_category_ids[]=1066&restaurant_category_ids[]=1074&restaurant_category_ids[]=1082&restaurant_category_ids[]=1090&restaurant_category_ids[]=1098&restaurant_category_ids[]=1106&restaurant_category_ids[]=1114&restaurant_category_ids[]=1122&restaurant_category_ids[]=1130&restaurant_category_ids[]=1138&restaurant_category_ids[]=1146&restaurant_category_ids[]=1154&restaurant_category_ids[]=1162&restaurant_category_ids[]=1170&restaurant_category_ids[]=1178&restaurant_category_ids[]=1186&restaurant_category_ids[]=1194&restaurant_category_ids[]=1202&restaurant_category_ids[]=1210&restaurant_category_ids[]=1218&restaurant_category_ids[]=1226&restaurant_category_ids[]=1234&restaurant_category_ids[]=1250&restaurant_category_ids[]=1258&restaurant_category_ids[]=1266&restaurant_category_ids[]=1274&restaurant_category_ids[]=1282&restaurant_category_ids[]=1290&restaurant_category_ids[]=1298&restaurant_category_ids[]=1306&restaurant_category_ids[]=1314&restaurant_category_ids[]=1322&restaurant_category_ids[]=1330&restaurant_category_ids[]=1338&restaurant_category_ids[]=1346&restaurant_category_ids[]=1354&restaurant_category_ids[]=1362&order_by=12'
            response=requests.get(url,headers=self.headers)

            print(str(page_num+8))
            for i in json.loads(response.content)['items']:
                id=i['restaurant']['id']
                # print('id:'+str(id))
                self.id_list.append(id)
            return True
    #单线程解析商品信息模块
    def parse_html(self):
        if len(self.id_list)==0:
            print('over!')
        else:
            id = self.id_list.pop()
            try:
                url='https://h5.ele.me/pizza/shopping/restaurants/'+str(id)+'/batch_shop?'
                response = requests.get(url, headers=self.headers,timeout=10)
                food_ids = []
                dic_main = json.loads(response.content)
                name=dic_main['rst']['name']
                menu=dic_main['menu']
                # 若获取的详情页面为空json，会把id向后插入回id_list，后续再次请求直到返回正常json。
                if menu==[]:
                    print(str(name)+'empty!')
                    self.id_list[:0]=[id]
                    self.parse_html()
                else:
                    print(name)
                    for i in menu:
                        for n in i['foods']:
                            food_id = n['item_id']
                            if food_id in food_ids:
                                pass
                            else:
                                food_ids.append(food_id)
                                items = {}
                                items['店铺名字'] =name
                                items['食物']=n['name']
                                items['月销量']=int(n['month_sales'])
                                # 这里做个改进，采用数据库连接池加快了入库速度。
                                conn = pool.connection() # 每次入库只需要建立connection()就可以，而不用再次初始化。
                                c = db(conn, items)
                                c.insert()
            # 若请求超时或者异常，会把id向后插入回id_list，再次请求。
            except:
                print('id'+str(id))
                print('timeout!')
                self.id_list[:0]=id
            finally:
                self.parse_html()

if __name__ == '__main__':
    E=Eleme()
    E.scheduler()