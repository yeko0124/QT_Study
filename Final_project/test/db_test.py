
import mysql_file.connector


# MySQL 서버 연결 설정
con = mysql_file.connector.connect(
  host="localhost",
  user="root",
  password="skfk1493",
  database="version_db"
)

cur = con.cursor()

# 커서 생성

# 예시 쿼리 실행
cur.execute("show tables;")

# 결과 가져오기
myresult = cur.fetchall()

# 결과 출력
# for x in myresult:
#   print(x)


def add_version(data: list):
  assert isinstance(data, list)
  assert len(data) == 3
  q = '''
    INSERT INTO version_final_table (cache_name, updated_time, user_id) 
    VALUES (%s, %s, %s);
    '''
  try:
    cur.execute(q, data)
    con.commit()
    f_id = cur.lastrowid
    # return True
    return f_id
  except Exception as err:
    con.rollback()
    print(err)
    return -1


lst = ['usd_rop2', '2024-03-09 01:52:07', 1]
res = add_version(data=lst)
print(res)


# print(myresult)