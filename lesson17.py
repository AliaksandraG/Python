import sqlite3
# создаём БД
conn = sqlite3.connect('name.db')
#создем объект, который позволит взоимодействовать с БД и добавдять записи
cursor = conn.cursor()
#создадим таблицу с 2 текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT,col_1 TEXT,col_2 TEXT)''')
#заполняем таблицу данными
#cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
#сохраняем изменения
conn.commit()
# d="red"
# f="black"
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''',(d,f))
# conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
#удаление записи из таблицы по айди и значению
cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
conn.commit()
cursor.execute('''DELETE FROM tab_1 WHERE col_1 ='red' ''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k=cursor.fetchall()
print(k)
#обновление данных в таблице
t = 3
cursor.execute('''UPDATE tab_1 SET col_1='world' WHERE id=?''',(t,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)