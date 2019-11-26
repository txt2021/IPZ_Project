import mysql.connector
import webbrowser
cnx = mysql.connector.connect(user='root',
                              host='127.0.0.1',
                              database='test')
cur = cnx.cursor()



k = ("Kiev","Ivan")

cur.execute("select URL from Doc where Doc.name in (select doc from Tag where Tag.type in ('city','name')  and Tag.data in {})".format(k) )
# Показываем результат.
result = cur.fetchall()
# print(result)
for i in result:
    if i:
        i = str(i)[2:len(i)-4]
        print(i)
        webbrowser.open_new_tab(i)


cur.close()
cnx.close()