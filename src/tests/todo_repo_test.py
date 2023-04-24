import unittest
import entities.User as User
import entities.Todo as Todo
from repositories import todo_repo

class TestTodoRepo(unittest.TestCase):
    def setUp(self):
        self.user = User.User('arttu', 'jsdfgsd')
        self.todo = Todo.Todo(self.user.username, "testi", False)
        self.todos = todo_repo.TodoRepo()

    def test_create_todo(self):
        todo_to_save = self.todos.create_todo(self.user, self.todo)
        self.assertEqual(todo_to_save, True)
    
    def test_delete_todo(self):
        todo_to_delete = self.todos.delete_todo(self.user, self.todo.content)
        self.assertEqual(todo_to_delete, True)

    def test_get_user_todos(self):
        self.todos.destroy_db_instances_for_testing()
        self.todos.create_todo(self.user, self.todo)
        self.todos.create_todo(self.user, self.todo)
        self.todos.create_todo(self.user, self.todo)
        self.todos.create_todo(self.user, self.todo)
        todos = self.todos.get_user_todos(self.user)
        self.assertEqual(len(todos), 4)