import db_config

class TodoRepo:
    """ Luokka, joka mahdollistaa todojen käsittelyn.
    """
    def __init__(self):
        """ Konstruktorissa luodaan yhteys tietokantaan.
        """
        self.db_conn = db_config.get_db()

    def create_todo(self, user, todo):
        """ Metodi joka luo uuden todon käyttäjälle.

        Args:
            user: käyttäjä joka luo todon.
            todo: todo joka lisätään tietokantaan.

        Returns:
            True, jos todoa ei löydy käyttäjältä, False jos löytyy.
        """
        user_id = self.db_conn.execute("SELECT id FROM users WHERE username=?"
                                       ,[user.username]).fetchone()
        todo_exists = self.db_conn.execute("SELECT todo FROM todos WHERE user_id=? and todo=?"
                                           ,[user_id[0], todo.content]).fetchone()
        if todo_exists is None:
            self.db_conn.execute("INSERT INTO todos (user_id, todo) VALUES (?, ?)"
                                 ,[user_id[0], todo.content])
            return True

        return False

    def get_user_todos(self, user):
        """ Metodi joka hakee käyttäjän todot.

        Args:
            user: käyttäjä kenen todot haetaan tietokannasta.

        Returns:
            Käyttäjän todot.
        """
        user_id = self.db_conn.execute("SELECT id FROM users WHERE username=?"
                                       ,[user.username]).fetchone()
        return self.db_conn.execute("SELECT todo FROM todos WHERE user_id=?"
                                    ,[user_id[0]]).fetchall()

    def delete_todo(self, user, todo):
        """ Metodi joka poistaa todon.

        Args:
            user: käyttäjä kenen todo poistetaan tietokannasta.
            todo: poistettava todo.
        
        Returns:
            True
        """
        user_id = self.db_conn.execute("SELECT id FROM users WHERE username=?"
                                       ,[user.username]).fetchone()
        self.db_conn.execute('DELETE FROM todos WHERE user_id=? and todo=?'
                             ,[user_id[0], todo])
        return True

    def edit_todo(self, user, todo, edited_todo):
        """ Metodi ylikirjoittaa valitun todon.

        Args:
            user: käyttäjä kenen todo poistetaan tietokannasta.
            todo: ylikirjoitettava todo.
            edited_todo: ylikirjoittava todo.

        Returns:
            True, jos edited_todo on eri kun muokattava eikä vastaavaa löydy tietokannasta.
            Muuten False.
        """
        if todo == edited_todo:
            return False

        user_id = self.db_conn.execute("SELECT id FROM users WHERE username=?"
                                       ,[user.username]).fetchone()
        todo_exists = self.db_conn.execute("SELECT todo FROM todos WHERE user_id=? and todo=?"
                                           ,[user_id[0], edited_todo]).fetchone()

        if todo_exists is None:
            self.db_conn.execute('UPDATE todos SET todo=? WHERE user_id=? and todo=?'
                                 ,[edited_todo, user_id[0], todo])
            return True
        return False

    def destroy_db_instances_for_testing(self):
        """ Metodi joka poistaa todot. (testejä varten)
        """
        self.db_conn.execute('DELETE FROM todos')
