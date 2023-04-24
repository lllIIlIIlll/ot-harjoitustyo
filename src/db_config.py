import sqlite3

DB_FILE = "studytimer.db"
db = sqlite3.connect(DB_FILE)
db.isolation_level = None

# Luodaan käyttäjä- ja todo-taulu tietokantaan, jos sellaisia ei ole
db.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )

db.execute(
    "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, user_id TEXT, todo TEXT)"
    )

# Funktio, jolla voidaan tarjota tietokantaa käyttäville luokille yhteys tietokantaan
def get_db():
    return db
