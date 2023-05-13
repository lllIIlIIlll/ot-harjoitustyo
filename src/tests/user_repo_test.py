import unittest
import entities.User as User
from repositories import user_repo

class TestUserRepo(unittest.TestCase):
    def setUp(self):
        self.users = user_repo.UserRepo(test=True)
        self.users.destroy_db_instances_for_testing()
        self.user = User.User('testi', 'testi')

    def test_registration_username_taken(self):
        self.users.register_user(self.user)
        test_user = self.users.register_user(self.user)
        self.assertEqual(test_user, False)
    
    def test_registration(self):
        test_user = self.users.register_user(self.user)
        self.assertEqual(test_user.username, self.user.username)

    def test_invalid_username_login(self):
        self.users.register_user(self.user)
        test_user = self.users.login_user(User.User('väärin', 'testi'))
        self.assertEqual(test_user, False)

    def test_invalid_password_login(self):
        self.users.register_user(self.user)
        test_user = self.users.login_user(User.User('testi', 'väärin'))
        self.assertEqual(test_user, False)

    def test_succesful_login(self):
        user = self.users.register_user(self.user)
        user_login = self.users.login_user(self.user)
        self.assertEqual(user_login, user)
