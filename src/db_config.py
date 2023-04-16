import sqlite3

DB_FILE = "studytimer.db"
db = sqlite3.connect(DB_FILE)
db.isolation_level = None

# Luodaan käyttäjä-taulu tietokantaan, jos sellaista ei ole
db.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )

# Funktio, jolla voidaan tarjota tietokantaa käyttäville luokille yhteys tietokantaan
def get_db():
    return db
