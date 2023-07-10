
import pymysql

conn = pymysql.connect(charset='utf8', host="127.0.0.1",
                       password="123123", port=3306, user='root',database='test3')

cursor = conn.cursor()


# def select():
#     sql = """
#         SELECT * FROM table1
#     """
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)

def task1():
    #2023-01-01/2023-01-07期間, 每個dimension1不為0的用戶所的用戶所造成的metric4值加總, 並依加總由大到小排列,
    input_start = input('input start date(yyyy-mm-dd): example: 2023-01-01\n')
    input_end = input('input end date(yyyy-mm-dd): example: 2023-01-07\n')
    sql = f"""
        SELECT user_id, SUM(metric4) as metric4_sum FROM table1
        WHERE __time BETWEEN '{input_start}' AND '{input_end}' AND dimension1 != '0'
        GROUP BY user_id
        ORDER BY metric4_sum DESC
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    # dump answer to task1.csv
    with open('task1.csv', 'w') as f:
        for row in result:
            f.write("%s,%s\n" % (row[0], row[1]))

def task2():
    # 過去7天, 每日的DAU數值(單日不重複user_id的加總) 格式為 data,DAU
    input_start = input('input start date(yyyy-mm-dd): example: 2023-01-01\n')
    input_end = input('input end date(yyyy-mm-dd): example: 2023-01-07\n')
    # sql = """
    #     SELECT __time, COUNT(DISTINCT user_id) as DAU FROM table1
    #     WHERE __time BETWEEN '2023-01-01 00:00:00' AND '2023-01-07 00:00:00'
    #     GROUP BY __time
    # """
    sql = f"""
    
        SELECT __time, COUNT(DISTINCT user_id) as DAU FROM table1
        WHERE __time BETWEEN '{input_start}' AND '{input_end}'
        GROUP BY __time
        """
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    # dump answer to task2.csv
    with open('task2.csv', 'w') as f:
        for row in result:
            f.write("%s,%s\n" % (row[0], row[1]))




if __name__ == "__main__":
    task1()
    task2()