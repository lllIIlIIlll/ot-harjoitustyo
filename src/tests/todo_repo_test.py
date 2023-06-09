import unittest
import entities.User as User
import entities.Todo as Todo
from repositories import todo_repo, user_repo

class TestTodoRepo(unittest.TestCase):
    def setUp(self):
        self.todos = todo_repo.TodoRepo(test=True)
        self.todos.destroy_db_instances_for_testing()
        self.users = user_repo.UserRepo(test=True)
        self.users.destroy_db_instances_for_testing()
        self.user = User.User('testikäyttäjä', 'testisalasana')
        self.users.register_user(self.user)
        self.todo = Todo.Todo(self.user.username, "testi", False)

    def test_create_todo(self):
        todo_to_save = self.todos.create_todo(self.user, self.todo)
        self.assertEqual(todo_to_save, True)
    
    def test_create_todo_duplicate(self):
        self.todos.create_todo(self.user, self.todo)
        duplicate_todo_to_save = self.todos.create_todo(self.user, self.todo)
        self.assertEqual(duplicate_todo_to_save, False)

    def test_edit_todo(self):
        edit_result = self.todos.edit_todo(self.user, self.todo.content, "muokattu")
        self.assertEqual(edit_result, True)

    def test_edit_todo_duplicate(self):
        edit_result = self.todos.edit_todo(self.user, "muokattu", "muokattu")
        self.assertEqual(edit_result, False)

    def test_edit_todo_duplicate_in_db(self):
        self.todos.create_todo(self.user, Todo.Todo(self.user.username, "muokattu", False))
        edit_result = self.todos.edit_todo(self.user, self.todo.content, "muokattu")
        self.assertEqual(edit_result, False)
    
    def test_delete_todo(self):
        self.todos.create_todo(self.user, self.todo)
        todo_to_delete = self.todos.delete_todo(self.user, self.todo.content)
        self.assertEqual(todo_to_delete, True)

    def test_get_user_todos(self):
        self.todos.create_todo(self.user, Todo.Todo(self.user.username, "testi1", False))
        self.todos.create_todo(self.user, Todo.Todo(self.user.username, "testi2", False))
        self.todos.create_todo(self.user, Todo.Todo(self.user.username, "testi3", False))
        self.todos.create_todo(self.user, Todo.Todo(self.user.username, "testi4", False))
        todos = self.todos.get_user_todos(self.user)
        self.assertEqual(len(todos), 4)
