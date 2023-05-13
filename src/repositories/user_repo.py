import db_config

class UserRepo:
    """ Luokka, joka mahdollistaa käyttäjän rekisteröinnin ja kirjautumisen.
    """
    def __init__(self, test=False):
        """ Konstruktorissa luodaan yhteys tietokantaan.

        Args:
            test: määrittää käytetäänkö testaamiseen tarkoitettuja tauluja.
        """
        if test:
            self.users = "usersTest"
        else:
            self.users = "users"

        self.db_connection = db_config.get_db()

    def register_user(self, user):
        """ Metodi joka tarkistaa onko käyttäjänimi varattu ja jos ei niin luodaan uusi käyttäjä.

        Args:
            user: rekisteröitävä käyttäjä.

        Returns:
            user, rekisteröity käyttäjä, False, nimi on varattu.
        """
        username_available = self.db_connection.execute(
            f"SELECT username FROM {self.users} WHERE username=?",[user.username]
            ).fetchall()
        if username_available == []:
            self.db_connection.execute(f"INSERT INTO {self.users} (username, password) VALUES (?, ?)",
                            [user.username, user.password])
            return user
        return False

    def login_user(self, user):
        """ Metodi joka tarkistaa onko käyttäjän salasana oikein.

        Args:
            user: kirjautuva käyttäjä.

        Returns:
            user, jos käyttäjä löytyy ja salasana täsmää, muuten False.
        """
        password = self.db_connection.execute(f"SELECT password FROM {self.users} WHERE username=?",
                                   [user.username]).fetchone()
        if password is not None:
            if password[0] == user.password:
                return user
            return False
        return False

    def destroy_db_instances_for_testing(self):
        """ Metodi joka poistaa käyttäjät. (testejä varten)
        """
        self.db_connection.execute(f"DELETE FROM {self.users}")
