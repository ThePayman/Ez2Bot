import sys
import MySQLdb
try:
    db = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        db = "Python"
        )
except Exception as e:
    print("No connection to db, stopping program...")
    sys.exit("Connection to db failed")
db.autocommit(True)
def find_next_id_db(type):
    cursor = db.cursor()
    cursor.execute("Select * FROM "+type+" ORDER BY id DESC LIMIT 1")
    for i in cursor.fetchall():
        return(i[0]+1)

def search_db(command):
    cursor = db.cursor()
    cursor.execute(command)
    result = cursor.fetchall()
    return result

def select(tabel,looking_for = "*",where = ""):
    """ selects and returns a value from the database

        tabel -- Tabel to search
        looking_for -- Values to select from the tabel (default="*")
        where -- Condition to finding the values (default="")
        
    """
    cursor = db.cursor()
    cursor.execute("SELECT "+ looking_for +" FROM "+ tabel +" "+where)
    result = cursor.fetchall()
    return(result)

def insert(querry):
    cursor = db.cursor()
    cursor.execute(querry)
    
