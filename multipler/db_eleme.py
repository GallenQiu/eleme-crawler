import mysql.connector

class db:
    def __init__(self,conn,item):
        self.conn=conn
        self.item=item

    def insert(self):
        cursor=self.conn.cursor()
        try:
            cursor.execute(
                """insert into eleme_simple_h5_multi(店铺名字,菜品,月销量)value(%s, %s, %s)""",
                (
                    self.item['店铺名字'],
                    self.item['食物'],
                    int(self.item['月销量'])
                ))
        except mysql.connector.Error as e:
            print('Mysql error!{}'.format(e))
        finally:
            self.conn.commit()
            cursor.close()
            self.conn.close()
# if __name__ == '__main__':
