 

import mysql.connector
dataBase = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd = 'Myadmin2#',

)

#prepare the curson object
cursorObject = dataBase.cursor()

#create a databsse
cursorObject.execute("CREATE DATABASE elderco")

print("all done")
