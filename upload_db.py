import pymysql
import csv
import sys
import logging

#RDS info
host = "@@@@.ap-northeast-2.rds.amazonaws.com" # RDS 엔드포인트
port = 3306
username = "admin" # 설정하신 호스트 네임
database = "test" # 만드신 데이터베이스 이름
password = "pw" # 설정하신 비밀번호
table_name = "USER" # 만드신 테이블 이름

def connect_RDS(host, port, username, password, database):
    try:
        conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port)
        cursor = conn.cursor()
        conn.commit()

    except:
        logging.error("Not connected")
        sys.exit(1)

    return conn, cursor


def save_data(conn, cursor):
    f = open('mycsvfile.csv')
    csvReader = csv.reader(f)

    # 컬럼 매핑
    for row in csvReader:
        name = row[0]
        links = row[1]
        print(name)
        print(links)

        sql = f"""insert into {table_name} (name, links) values (%s, %s)"""
        cursor.execute(sql, (name, links))

    # DB의 변화 저장
    conn.commit()
    f.close()
    conn.close()

if __name__ == "__main__":
    conn, cursor = connect_RDS(host, port, username, password, database)
    save_data(conn, cursor)