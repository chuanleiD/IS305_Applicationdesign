import sqlite3

def insert(insert_data):
      db_file = r"course_data.db"

      conn = sqlite3.connect(db_file)
      cur = conn.cursor()

      for data in insert_data:
            sql = 'insert into course_data (course_name, start_time, end_time, weekday, start_week, end_week, meeting_number, meeting_password, single_or_double_week)' \
                  'values(?,?,?,?,?,?,?,?,?)'
            cur.execute(sql, data)

      conn.commit()
      cur.close()
      conn.close()

#insert([("操作系统", 1, 2. 1, 9, 16, "576409879", "2932", 0)])

def read_db():
      db_file = r"course_data.db"

      conn = sqlite3.connect(db_file)
      cur = conn.cursor()

      sql = 'SELECT * from course_data'
      values = cur.execute(sql)
      val = values.fetchall()

      conn.commit()
      cur.close()
      conn.close()

      #val = [(1, '现代密码学', 3, 1, 1, 8, '248303045', '8412')]
      return val











