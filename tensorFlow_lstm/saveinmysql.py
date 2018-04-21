#coding:utf-8
import MySQLdb as mdb
def saveresultinmysql(endday1, loss1, rmse1, correctrate1, predictclose1):
    con = None
        #连接mysql的方法：connect(host='localhost',user='root',passwd='root',db='test',port=3306)
    con = mdb.connect('localhost', 'root','root', 'ntlab_merge')
        #所有的查询，都在连接con的一个模块cursor上面运行的
    with con:
        cur = con.cursor()
        sql = 'INSERT INTO lzn_bishe_lstm (endday,loss,rmse, correctrate, predictclose) VALUES (%s, %s,%s,%s,%s)'
        cur.execute(sql,(endday1, loss1, rmse1, correctrate1, predictclose1))

#saveresultinmysql("124",10.2,0,0,0)
