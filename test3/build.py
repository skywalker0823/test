import pymysql

# Build
def build_db(conn):
    cursor.execute("DROP DATABASE IF EXISTS test3")
    cursor.execute("CREATE DATABASE test3")
    cursor.execute("USE test3")
    conn.commit()

def build_table(conn):
    cursor.execute("DROP TABLE IF EXISTS table1")
    cursor.execute("""CREATE TABLE table1 (
        __time DATETIME,
        dimension1 VARCHAR(255),
        user_id VARCHAR(255),
        metric1 INT,
        metric2 INT,
        demension2 VARCHAR(255),
        metric3 INT,
        metric4 INT,
        demension4 VARCHAR(255)
        )"""
        )
    conn.commit()

def insert_sample_data(conn):
    sql = """
        INSERT INTO table1
        (__time, dimension1, user_id, metric1, metric2, demension2, metric3, metric4, demension4)
        VALUES
        ('2023-01-01 00:00:00', '1', 'f3341c', 1, 0, '1', 5, 190, '1'),
        ('2023-01-01 00:00:00', '1', 'g432k1q', 1, 0, '1', 82, 5432, '1'),
        ('2023-01-02 00:00:00', '1', 'herh421h', 0, 0, '2', 13, 73, '2'),
        ('2023-01-04 00:00:00', '0', 'g432k1qg', 1, 0, '1', 33, 5432, '1'),
        ('2023-01-06 00:00:00', '1', 'f3341c31', 1, 0, '1', 54, 191, '1')
    """
    cursor.execute(sql)
    conn.commit()


if __name__ == "__main__":
    conn = pymysql.connect(charset='utf8', host="127.0.0.1",
                           password="123123", port=3306, user='root')
    cursor = conn.cursor()
    print('build database...')
    build_db(conn)
    build_table(conn)
    insert_sample_data(conn)
    print('build database done.')
    cursor.close()
    conn.close()