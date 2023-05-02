class Todo:
    """ Luokka joka määrittää todon.
    """
    def __init__(self, username, content, status):
        """ Luokan konstruktori, määrittää käyttäjän todon.
        Args:
            username: todon luonut käyttäjä.
            content: todon sisältö.
            status: todon status.
        """
        self.owner = username
        self.content = content
        self.status = status
