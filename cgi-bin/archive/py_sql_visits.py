import os,sys
import time, datetime
import pymysql

def py_sql_visits(db,cur,page_id, page_title, page_keywords):
    datetime_now = str(datetime.datetime.now()).split(' ')
    str_time_now_sec = datetime_now[1].split(":")
    time_now_sec = float(str_time_now_sec[2])+60.*float(str_time_now_sec[1])+3600.*float(str_time_now_sec[0])
    print("\n<!--текущие дата и время\n",datetime_now, str_time_now_sec, time_now_sec, "\n-->\n")

#    with open('../tmp/page_visits.txt', mode = 'a', encoding = "utf-8", errors = None, newline = None, closefd = True, opener = None) as page_visits:
#        page_visits.write("%s\t%s\t%s\t%s\n" % (page_id,page_title, os.environ[ "REMOTE_ADDR" ],  datetime.datetime.now() ))

    cur.execute("""CREATE TABLE IF NOT EXISTS `py_page_visits` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `page_id` int(10) unsigned NOT NULL,
      `page_title` varchar(255) NOT NULL,
      `page_ip` varchar(255) NOT NULL,
      `page_date` date NOT NULL,
      `page_time` time NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_general_ci;""")
    db.commit()#транзакция (дожидаемся завершения операции модификации таблицы)

    cur.execute("""INSERT INTO `py_page_visits` (`id`,`page_id`, `page_title`, `page_ip`, `page_date`, `page_time`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % ('NULL' , page_id, page_title, os.environ[ "REMOTE_ADDR" ], time.strftime('%Y-%m-%d'), time.strftime('%H:%M:%S')))
    db.commit()
    #cur.execute("""SELECT `id`, `page_title`, `page_ip`, `page_date`, `page_time` FROM `py_page_visits` ORDER BY `id` DESC LIMIT 0 , 1""")
    cur.execute("""SELECT * FROM `py_page_visits` ORDER BY `id` DESC LIMIT 0 , 1""")
    result_one  =  cur.fetchone()
    print("\n<!--Контрольное считывание из базы последней записи\nresult_one:\n", type(result_one), result_one)
    print("\n<br>Значения полей: ",end="")
    for value in result_one:
        print (value, end=";")
    print("-->\n")
    cur.execute("""SELECT `page_id`, `page_title`, COUNT( `page_id` ) FROM `py_page_visits` GROUP BY `page_id` ORDER BY `page_id`""")
    #cur.execute("""SELECT `page_title`, COUNT( `page_title` ) FROM `py_page_visits` GROUP BY `page_title` ORDER BY `page_title`""")
    result_all  =  cur.fetchall()
    print("\n<!--Получение частот id из базы\nresult_all:\n", type(result_all), result_all)
    for result_one in result_all:
        print("\n",end="")
        for value in result_one:
            print (value, end=";")            
    print("\n</p>-->\n")

    with open('../tmp/frequencies.txt', mode = 'w', encoding = "utf-8", errors = None, newline = None, closefd = True, opener = None) as f_append:
        for result in result_all:
            page_id, page_title, count  =  result
            f_append.write("%s;%s;%s\n" % (page_id, page_title, count))
            