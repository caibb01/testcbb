import MySQLdb


# 数据库基础操作
class DB_Operation(object):
    def __init__(self, host, port, user, password, db_name):
        self.host = host
        self.port = port
        self.user = user
        self.password = str(password)
        self.db = db_name

    def connect_mars_sqldb(self):
        try:
            conn = MySQLdb.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                charset='utf8'
            )
            conn.select_db(self.db)
            cur = conn.cursor()
            # print(u"创建数据库pythonDB成功! ")
            return conn, cur
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def exec_db(self, param):
        """
        插入数据
        :param param: 插入一条数据，删除一条数据，更新数据
        :return:
        """
        conn, cur = self.connect_mars_sqldb()
        try:
            cur.execute(param)
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print("insert_or_delete_db: %s" % e)
            cur.close()
            conn.close()

    def select_db_one(self, param):
        """
        查询单条数据
        :param param: 查询语句
        :return:
        """
        conn, cur = self.connect_mars_sqldb()
        try:
            cur.execute(param)
            result = cur.fetchone()
            cur.close()
            conn.close()
            return result
        except Exception as e:
            print("select_db: %s" % e)
            cur.close()
            conn.close()

    def select_db_all(self, param):
        """
         查询单条数据
         :param param: 查询语句
         :return:返回元组
         """
        conn, cur = self.connect_mars_sqldb()
        try:
            cur.execute(param)
            result = cur.fetchall()
            cur.close()
            conn.close()
            return result
        except Exception as e:
            print("select_db: %s" % e)
            cur.close()
            conn.close()
