class Todo:
    # Luokka joka määrittää todo:n
    def __init__(self, user_id, title, notes, status):
        self.owner = user_id
        self.title = title
        self.notes = notes
        self.status = status
