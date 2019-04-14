import requests,json
from web.login import Login
from web.eleme_mysql import ormal_Mysql

while True:
    with open('cookies.txt','r')as f:

        lines=f.readlines()
        if lines!=[]:
            cookies1='track_id='+str(lines[2].replace('\n',''))+'; USERID='+str(lines[1].replace('\n',''))+'; UTUSER='+str(lines[1].replace('\n',''))+'; SID='+str(lines[0].replace('\n',''))+';'
            break
        else:
            L=Login()
            L.send()

class eleme():
    def __init__(self):
        self.latitude = 39.99287
        self.longitude = 116.31025
        self.headers = {
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'cookie':cookies1,
            'referer':'https://h5.ele.me/msite/food/',
            'user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Mobile Safari/537.36',
            'x-shard':'loc=114.10957,22.54362',}
    def main_parse(self,page_num):
        url='https://h5.ele.me/restapi/shopping/v3/restaurants?latitude='+str(self.latitude)+'&longitude='+str(self.longitude)+'&keyword=&offset='+str(page_num)+'&limit=8&extras[]=activities&extras[]=tags&terminal=h5&rank_id=10fe946cb6b440ad8c386796b921a79b&brand_ids[]=&restaurant_category_ids[]=209&restaurant_category_ids[]=212&restaurant_category_ids[]=214&restaurant_category_ids[]=266&restaurant_category_ids[]=267&restaurant_category_ids[]=268&restaurant_category_ids[]=269&restaurant_category_ids[]=354&restaurant_category_ids[]=362&restaurant_category_ids[]=370&restaurant_category_ids[]=378&restaurant_category_ids[]=386&restaurant_category_ids[]=394&restaurant_category_ids[]=402&restaurant_category_ids[]=410&restaurant_category_ids[]=418&restaurant_category_ids[]=426&restaurant_category_ids[]=434&restaurant_category_ids[]=442&restaurant_category_ids[]=450&restaurant_category_ids[]=458&restaurant_category_ids[]=466&restaurant_category_ids[]=474&restaurant_category_ids[]=482&restaurant_category_ids[]=490&restaurant_category_ids[]=498&restaurant_category_ids[]=746&restaurant_category_ids[]=754&restaurant_category_ids[]=762&restaurant_category_ids[]=770&restaurant_category_ids[]=778&restaurant_category_ids[]=786&restaurant_category_ids[]=794&restaurant_category_ids[]=802&restaurant_category_ids[]=810&restaurant_category_ids[]=818&restaurant_category_ids[]=826&restaurant_category_ids[]=834&restaurant_category_ids[]=842&restaurant_category_ids[]=850&restaurant_category_ids[]=858&restaurant_category_ids[]=866&restaurant_category_ids[]=874&restaurant_category_ids[]=882&restaurant_category_ids[]=890&restaurant_category_ids[]=898&restaurant_category_ids[]=906&restaurant_category_ids[]=914&restaurant_category_ids[]=922&restaurant_category_ids[]=930&restaurant_category_ids[]=938&restaurant_category_ids[]=946&restaurant_category_ids[]=954&restaurant_category_ids[]=221&restaurant_category_ids[]=222&restaurant_category_ids[]=223&restaurant_category_ids[]=224&restaurant_category_ids[]=225&restaurant_category_ids[]=226&restaurant_category_ids[]=227&restaurant_category_ids[]=228&restaurant_category_ids[]=232&restaurant_category_ids[]=263&restaurant_category_ids[]=506&restaurant_category_ids[]=514&restaurant_category_ids[]=522&restaurant_category_ids[]=530&restaurant_category_ids[]=538&restaurant_category_ids[]=546&restaurant_category_ids[]=554&restaurant_category_ids[]=562&restaurant_category_ids[]=570&restaurant_category_ids[]=578&restaurant_category_ids[]=586&restaurant_category_ids[]=594&restaurant_category_ids[]=602&restaurant_category_ids[]=610&restaurant_category_ids[]=618&restaurant_category_ids[]=626&restaurant_category_ids[]=634&restaurant_category_ids[]=642&restaurant_category_ids[]=650&restaurant_category_ids[]=658&restaurant_category_ids[]=666&restaurant_category_ids[]=674&restaurant_category_ids[]=682&restaurant_category_ids[]=690&restaurant_category_ids[]=698&restaurant_category_ids[]=706&restaurant_category_ids[]=218&restaurant_category_ids[]=234&restaurant_category_ids[]=236&restaurant_category_ids[]=962&restaurant_category_ids[]=970&restaurant_category_ids[]=978&restaurant_category_ids[]=986&restaurant_category_ids[]=994&restaurant_category_ids[]=1002&restaurant_category_ids[]=1010&restaurant_category_ids[]=1018&restaurant_category_ids[]=1026&restaurant_category_ids[]=1034&restaurant_category_ids[]=240&restaurant_category_ids[]=241&restaurant_category_ids[]=242&restaurant_category_ids[]=249&restaurant_category_ids[]=250&restaurant_category_ids[]=714&restaurant_category_ids[]=722&restaurant_category_ids[]=730&restaurant_category_ids[]=738&restaurant_category_ids[]=346&restaurant_category_ids[]=1042&restaurant_category_ids[]=1050&restaurant_category_ids[]=1058&restaurant_category_ids[]=1066&restaurant_category_ids[]=1074&restaurant_category_ids[]=1082&restaurant_category_ids[]=1090&restaurant_category_ids[]=1098&restaurant_category_ids[]=1106&restaurant_category_ids[]=1114&restaurant_category_ids[]=1122&restaurant_category_ids[]=1130&restaurant_category_ids[]=1138&restaurant_category_ids[]=1146&restaurant_category_ids[]=1154&restaurant_category_ids[]=1162&restaurant_category_ids[]=1170&restaurant_category_ids[]=1178&restaurant_category_ids[]=1186&restaurant_category_ids[]=1194&restaurant_category_ids[]=1202&restaurant_category_ids[]=1210&restaurant_category_ids[]=1218&restaurant_category_ids[]=1226&restaurant_category_ids[]=1234&restaurant_category_ids[]=1250&restaurant_category_ids[]=1258&restaurant_category_ids[]=1266&restaurant_category_ids[]=1274&restaurant_category_ids[]=1282&restaurant_category_ids[]=1290&restaurant_category_ids[]=1298&restaurant_category_ids[]=1306&restaurant_category_ids[]=1314&restaurant_category_ids[]=1322&restaurant_category_ids[]=1330&restaurant_category_ids[]=1338&restaurant_category_ids[]=1346&restaurant_category_ids[]=1354&restaurant_category_ids[]=1362&order_by=12'
        response=requests.get(url,headers=self.headers)
        print(page_num)
        for i in json.loads(response.content)['items']:
            id=i['restaurant']['id']
            self.parse_detial(id)

    def parse_detial(self,id):
        url='https://h5.ele.me/pizza/shopping/restaurants/'+str(id)+'/batch_shop?'
        print(id)
        response=requests.get(url,headers=self.headers)
        food_ids=[]
        dic_main=json.loads(response.content)
        try:
            name=dic_main['rst']['name']
            print(name)
            for i in dic_main['menu']:
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
                        db = ormal_Mysql()
                        db.insert(items)
        except:
            print(response.text)

    def control(self):
        #修改爬取页数(乘以8)
        maxpage=31
        for i in range(0, int(maxpage)):
            page_num = i * 8
            self.main_parse(page_num)

if __name__ == '__main__':
    main=eleme()
    main.control()