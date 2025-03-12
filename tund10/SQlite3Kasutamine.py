from sqlite3 import *
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Ühendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis viga '{e}'")
    return connection

conn=create_connection("C:/Users/Admin/Desktop/visual studio работы/Hello world/tund10/appdate/date.db")

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud")
    except Error as e:
        print(f"Viga '{e}' tabeli loomisega")


create_gender_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nimetus TEXT NOT NULL)
"""
insert_genders="""
insert into
gender(Nimetus)
values
('mees')
('naine')
"""

create_users_table2 = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    Lname TEXT NOT NULL,
    age INTEGER,
    GenderId INTEGER,
    FOREIGN KEY (GenderId) references gender (Id)
);
"""



create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""

create_users2 = """
INSERT INTO
    users2 (name, Lname, age, GenderId)
VALUES
    ('Mati', tamm, '50', '1'),
    ('Lidia', kon, '12', '2'),
    ('Brigitte', zon, '21', '1'),
    ('Mike', ber, '22', '1'),
    ('Elizabeth', gerd, '34', '1');
"""




execute_query(conn, create_users_table)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Viga '{e}'")



create_users = """
INSERT INTO
    users (name, age, gender, nationality)
VALUES
    ('Mati', 25, 'mees', 'USA'),
    ('Lidia', 32, 'naine', 'France'),
    ('Brigitte', 35, 'naine', 'England'),
    ('Mike', 40, 'mees', 'Denmark'),
    ('Elizabeth', 21, 'naine', 'Eesti');
"""


execute_query(conn, create_users)

select_users = "SELECT * FROM users"

users = execute_read_query(conn, select_users)

for user in users:
    print(user)



def add_users_query_2(connection, user_data):
    """Lisame userit, mis on eraldi sisestatud"""
    
    query = "INSERT INTO users(name, age, gender, nationality) VALUES(?, ?, ?, ?)"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

insert_user = (input("Nimi: "), int(input("Vanus: ")), input("Sugu: "), input("Riik: "))
print(insert_user)
add_users_query_2(conn, insert_user)


def delete_data_from_tabel(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Andmed on kustutatud")
    except Error as e:
        print(f"Viga '{e}' andmete kustutamisega")


print("Andmete kustutame tabelist 'users'")
delete_data_from_users = "DELETE FROM users WHERE age < 30"
delete_data_from_tabel(conn, delete_data_from_users)

print("Tabelis 'users' on jäänud neid kes vanem kui 30:")
users = execute_read_query(conn, select_users)

for user in users:
    print(user)




