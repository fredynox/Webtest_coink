import sqlite3 as sql

db_path = "C:\\Users\\fredy\\Documents\\flask_app\\oink_test1\\env\\database\\oink.db"

# def create_db():
#     conn = sql.connect(db_path)
#     conn.commit()
#     conn.close

# def create_table():
#     conn = sql.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute(
#         """CREATE TABLE IF NOT EXISTS users (
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             phone integer NOT NULL
#         )"""
#     )
#     conn.commit()
#     conn.close()

# def insert_row(name, email, phone):
#     conn = sql.connect(db_path)
#     cursor = conn.cursor()
#     instruccion = f"INSERT INTO users VALUES ('{name}', '{email}', {phone})"
#     cursor.execute(instruccion)
#     conn.commit()
#     conn.close()    



conn = sql.connect(":memory:")
conn.execute(""" SELECT * FROM users""").fetchall()

if __name__ == "__main__":
    # create_db()
    # create_table()
    # insert_row('Fredy Estrada', 'ing.fredy.florez@outlook.com', 3193429869)
    # drop_table
    pass 