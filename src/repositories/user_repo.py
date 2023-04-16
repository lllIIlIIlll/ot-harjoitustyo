import db_config

class UserRepo:
    def __init__(self):
        # Konstruktorissa luodaan yhteys tietokantaan
        self.db_connection = db_config.get_db()

    def register_user(self, user):
        # Metodi joka tarkistaa onko käyttäjänimi varattu ja jos ei niin luodaan uusi käyttäjä
        username_available = self.db_connection.execute(
            "SELECT username FROM users WHERE username=?",[user.username]
            ).fetchall()
        if username_available == []:
            self.db_connection.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                            [user.username, user.password])
            return user
        return False # Käyttäjänimi käytössä

    def login_user(self, user):
        # Metodi joka tarkistaa onko käyttäjän salasana oikein
        password = self.db_connection.execute("SELECT password FROM users WHERE username=?",
                                   [user.username]).fetchone()
        if password is not None:
            if password[0] == user.password:
                # Salasanan täsmätessä palautetaan käyttäjä
                return user
            return False # Salasana ei täsmää
        return False # Väärä salasana

    def destroy_db_instances_for_testing(self):
        # Testaamiseen tarkoitettu metodi
        self.db_connection.execute('DELETE FROM users')
