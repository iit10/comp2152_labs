import sqlite3
import function

db_connection = sqlite3.connect("sqlite.db")
db_connection.row_factory = sqlite3.Row  
print(db_connection)

db_cursor = db_connection.cursor()
print(db_cursor)

query_q1 = "SELECT * FROM demo WHERE id > 14"
db_cursor.execute(query_q1)

names = [row["Name"] for row in db_cursor.fetchall()]
print("Names:", names)

print("Reading 1 row")
row = db_cursor.fetchone()
print(row)

function.query_responder(db_cursor, "fetchall")

query2 = "INSERT INTO demo (Name, Hint) VALUES ('Michael', 'Murphy')"
db_cursor.execute(query2)
db_connection.commit()

del_row = int(input("Enter an id to delete rows with id < this value: "))
query_q2 = "DELETE FROM demo WHERE id < ?"
db_cursor.execute(query_q2, (del_row,))
affected_rows = db_cursor.rowcount

print(f"{affected_rows} rows affected. Are you sure you want to continue?")

db_connection.close()
