import  MySQLdb
mydb =  MySQLdb.connect(host="localhost",
    user="root",
    passwd="xxxx",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")