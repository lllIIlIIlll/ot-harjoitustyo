import db_config

class TodoRepo:
    def __init__(self):
        # Konstruktorissa luodaan yhteys tietokantaan
        self.db_connection = db_config.get_db()

    def create_todo(self, user, todo):
        # Metodi joka luo uuden todon käyttäjälle
        user_id = self.db_connection.execute("SELECT id FROM users WHERE username=?",
                                             [user.username]).fetchone()
        self.db_connection.execute("INSERT INTO todos (user_id, todo) VALUES (?, ?)",
                                    [user_id[0], todo.content])
        return True

    def get_user_todos(self, user):
        # Metodi joka hakee käyttäjän todot
        user_id = self.db_connection.execute("SELECT id FROM users WHERE username=?",
                                             [user.username]).fetchone()
        return self.db_connection.execute("SELECT todo FROM todos WHERE user_id=?",
                                          [user_id[0]]).fetchall()

    def delete_todo(self, user, todo):
        user_id = self.db_connection.execute("SELECT id FROM users WHERE username=?",
                                            [user.username]).fetchone()
        self.db_connection.execute('DELETE FROM todos WHERE user_id=? and todo=?',
                                    [user_id[0], todo])
        return True

    def destroy_db_instances_for_testing(self):
        # Testaamiseen tarkoitettu metodi
        self.db_connection.execute('DELETE FROM todos')