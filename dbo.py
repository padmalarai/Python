import MySQLdb

dbo=MySQLdb.connect('localhost','root','mysql','<<db_name>>')
name= input("Please enter VM name")
ip= input("Please enter VM name")
name= input("Please enter ip")
port= int(input("Please enter port"))
dc= input("Please enter datacenter")


cursor1=dbo.cursor()
query="insert into sysinfo value('{}','{}','{}','{}')".format(name,ip,port,dc)

cursor1.execute(query)
dbo.commit()

query1="select * from sysinfo"
result=cursor.fetchall()
for name,ip,port,dc in result:
    print("{}/t{}/t{}/t{}".format(name,ip,port,dc)

          
dbo.close()

