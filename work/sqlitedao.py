import sqlite3

conn = sqlite3.connect('qsm.db')
cursor = conn.cursor()

if __name__ == '__main__':
    cursor.execute('''
            drop table task;
            CREATE TABLE task(
               id           INT  PRIMARY KEY autoincrement NOT NULL,
               name         VARCHAR(50) NULL,
               result       VARCHAR(100) NULL,
               key          VARCHAR(100) NULL,
               gn_id_list   TEXT NULL,
               status       VARCHAR(20) null,
               exec_time    TEXT NULL
           );''')
