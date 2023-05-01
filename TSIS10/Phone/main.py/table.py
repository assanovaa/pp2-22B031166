import psycopg2

conn = psycopg2.connect(host="localhost",
dbname="postgres",user="postgres",password="Vudafu96",port=5432)

current=conn.cursor()

create_table='''CREATE TABLE snake(
    username VARCHAR(40),
    highscore INT NOT NULL,
    level INT NOT NULL
    );'''
    
current.execute(create_table)

current.close()
conn.commit()
conn.close()