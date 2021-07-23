import pymysql
all_db_sql = "show databases"
try:
    conn = pymysql.connect(host="localhost", user="root", password="root")
    cursor = conn.cursor()
    cursor.execute(all_db_sql)
    dbs = cursor.fetchall()
    for db in dbs:
        db_name = db[0]
        if "db_" in db_name:
            sql = "DROP DATABASE IF EXISTS " + db_name
            try:
                cursor.execute(sql)
            except:
                print("DROP ERROR")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)
