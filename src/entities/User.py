class User:
    """ Luokan konstruktori, määrittää käyttäjän.
    """
    def __init__(self, username, password):
        """ Luokan konstruktori.
        Args:
            username: käyttäjän nimi.
            password: käyttäjän salasana.
        """
        self.username = username
        self.password = password
