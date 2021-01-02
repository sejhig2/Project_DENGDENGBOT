import pymysql

# DB에 연결하기
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='projekt2', charset='utf8')

#커서 만들기
cur = conn.cursor()