import mysql.connector as sql
mydb = sql.connect(
    host = "localhost",
    user = 'root',
    password = '784264',
    database = 'bank'
)
cursor =  mydb.cursor()

def db_query(str):
    cursor.execute(str)
    
    result = cursor.fetchall()
    return result
    

def createcustomertable():
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS customers
               (username VARCHAR(30),
               password VARCHAR(30),
               name VARCHAR(30),
               age INTEGER,
               city VARCHAR(20),
               balance INTEGER not null,
               account_number INTEGER not null,
               status BOOLEAN)
 ''')

mydb.commit()

if __name__ == "__main__":
    createcustomertable()
    
    