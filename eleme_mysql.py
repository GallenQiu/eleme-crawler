"""
通用模板——数据库Mysql
"""
import mysql.connector
class ormal_Mysql():
    # 数据库设置
    def insert(self,item):
        config = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': '199789',
            'port': 3306,
            #数据库名字
            'database': 'eleme',
        }
        cnn = mysql.connector.connect(**config)
        cursor = cnn.cursor()
        # 数据表名字改一下
        try:
            cursor.execute(
                 """insert into eleme_simple_h5(店铺名字,菜品,月销量)value(%s, %s, %s)""",
            (
             item['店铺名字'],
             item['食物'],
             int(item['月销量'])
             ))
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cnn.commit()
            cursor.close()
            cnn.close()
