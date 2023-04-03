import db_config

class UserRepo:
    def __init__(self):
        # Konstruktorissa luodaan yhteys tietokantaan
        self.db = db_config.get_db()

    def register_user(self, user):
        # Metodi joka tarkistaa onko käyttäjänimi varattu ja jos ei niin luodaan uusi käyttäjä
        username_available = self.db.execute("SELECT username FROM users WHERE username=?", [user.username]).fetchall()
        if username_available == []:
            self.db.execute("INSERT INTO users (username, password) VALUES (?, ?)", [user.username, user.password])
            return user
        else:
            # Käyttäjänimi jo käytössä
            return False
        
    def login_user(self, user):
        # Metodi joka tarkistaa onko käyttäjän salasana oikein
        password = self.db.execute("SELECT password FROM users WHERE username=?", [user.username]).fetchone()
        if password != None:
            if password[0] == user.password:
                # Salasanan täsmätessä palautetaan käyttäjä
                return user
            else:
                # Salasana ei täsmää
                return False
        else:
            # Väärä salasana
            return False
        
    def destroy_db_instances_for_testing(self):
        # Testaamiseen tarkoitettu metodi
        self.db.execute('DELETE FROM users')
        
