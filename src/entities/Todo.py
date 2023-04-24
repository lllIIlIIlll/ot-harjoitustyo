class Todo:
    # Luokka joka määrittää todo:n
    def __init__(self, username, content, status):
        self.owner = username
        self.content = content
        self.status = status
