import pymysql.cursors
# Connect to the database
config={
"host":"localhost",
"port":3306,
"user":"root",
"password":"123456",
"db":"employees",
"charset":"utf8mb4",
"cursorclass":pymysql.cursors.DictCursor,
}
connection = pymysql.connect(**config)