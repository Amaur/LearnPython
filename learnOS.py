import mysql.connector
from mysql.connector import Error,MySQLConnection
from ConfigParser import ConfigParser



def read_db_config(filename = 'config.ini', section = 'mysql'):
	"""Read database configuration file and return a dictionary"""
	
	#create parser and read ini configuration
	parser = ConfigParser()
	parser.read(filename)
	
	#get section, default to mysql
	
	db ={}
	if parser.has_section(section):
		items = parser.items(section)
		for item in items:
			db[item[0]]=item[1]
	else:
		raise Exception('{0} not found in the {1} file'.format(section, filename))
	return db


def connect():
	"""Connect to mysql database"""
	db_config = read_db_config()
	try:
		"""
		conn = mysql.connector.connect(host='localhost',
										database='python_mysql',
										user='root',
										password='tegbeton') """
		print("Connecting to MySQL databse...")
		conn= MySQLConnection(**db_config)
		
		if conn.is_connected():
			print("Connection established")
		else:
			print("connection failed.")
	except Error as e :
		print(e)
	finally:
		conn.close()
		print("Connection closed..!")

def query_with_fetchone():
	try:
		dbconfig = read_db_config()
		conn = MySQLConnection(**dbconfig)
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM books")
		
		row = cursor.fetchone()
		
		while row is not None:
			print(row)
			row = cursor.fetchone()
	except Error as e:
		print(e)
		
	finally:
		cursor.close()
		conn.close()
		
def query_with_fetchall():
	try:
		dbconfig = read_db_config()
		conn = MySQLConnection(**dbconfig)
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM books")
		
		rows = cursor.fetchall()
		print("Total Row(s): ",cursor.rowcount)
		for row in rows:
			print(row)
			
		
	except Error as e:
		print(e)
		
	finally:
		cursor.close()
		conn.close()
		
		
def iter_row(cursor, size=10):
	while True:
		rows = cursor.fetchmany(size)
		if not rows:
			break
		for row in rows:
			yield row


def query_with_fetchmany():
	try:
		dbconfig = read_db_config()
		conn = MySQLConnection(**dbconfig)
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM books")
		
		for row in iter_row(cursor, 10):
			print(row)
			
		
	except Error as e:
		print(e)
		
	finally:
		cursor.close()
		conn.close()


def insert_book(title, isbn):
	query = "INSERT INTO books(title,isbn) VALUES(%s,%s)"
	args = (title, isbn)
	
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)
		
		cursor = conn.cursor()
		cursor.execute(query, args)
		
		if cursor.lastrowid:
			print("last insert id", cursor.lastrowid)
		else:
			print('last insert id not found')
			
		conn.commit()
		
	except Error as error:
		print(error)
		
	finally:
		cursor.close()
		conn.close()


def update_book(book_id, title):
    # read database configuration
    db_config = read_db_config()
 
    # prepare query and data
    query = """ UPDATE books
                SET title = %s
                WHERE id = %s """
 
    data = (title, book_id)
 
    try:
        conn = MySQLConnection(**db_config)
 
        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)
 
        # accept the changes
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

def delete_book(book_id):
    db_config = read_db_config()
 
    query = "DELETE FROM books WHERE id = %s"
 
    try:
        # connect to the database server
        conn = MySQLConnection(**db_config)
 
        # execute the query
        cursor = conn.cursor()
        cursor.execute(query, (book_id,))
 
        # accept the change
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close() 
 


def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)


def update_blob(author_id, filename):
    # read file
    data = read_file(filename)
 
    # prepare update query and data
    query = "UPDATE authors " \
            "SET photo = %s " \
            "WHERE id  = %s"
 
    args = (data, author_id)
 
    db_config = read_db_config()
 
    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def read_blob(author_id, filename):
    # select photo column of a specific author
    query = "SELECT photo FROM authors WHERE id = %s"
 
    # read database configuration
    db_config = read_db_config()
 
    try:
        # query blob data form the authors table
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, (author_id,))
        photo = cursor.fetchone()[0]
 
        # write blob data into a file
        write_file(photo, filename)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()

		
def main():
	insert_book("A Sudden Light", "9781439187036")

def Search_book(book_id):
	# select photo column of a specific author
    query = "SELECT title FROM books WHERE id = %s"
 
    # read database configuration
    db_config = read_db_config()
 
    try:
        # query blob data form the authors table
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, (book_id,))
        title = cursor.fetchone()#[0]
 
        # write blob data into a file
        #write_file(photo, filename)
        print(title)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
		

		
if __name__=='__main__':
	#connect()
	#query_with_fetchmany()								
	#main()
	Search_book(78)
