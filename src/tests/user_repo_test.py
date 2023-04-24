import unittest
import entities.User as User
from repositories import user_repo

class TestUserRepo(unittest.TestCase):
    def setUp(self):
        self.user = User.User('arttu', 'jsdfgsd')
        self.users = user_repo.UserRepo()

    def test_registration_username_taken(self):
        self.users.register_user(self.user)
        test_user = self.users.register_user(self.user)
        self.assertEqual(test_user, False)
    
    def test_registration(self):
        self.users.destroy_db_instances_for_testing()
        test_user = self.users.register_user(self.user)
        self.assertEqual(test_user.username, self.user.username)

    def test_invalid_username_login(self):
        self.users.register_user(self.user)
        test_user = self.users.login_user(User.User('artt', 'jsdfgsd'))
        self.assertEqual(test_user, False)

    def test_invalid_password_login(self):
        test_user = self.users.login_user(User.User('arttu', 'Äjsdfgsd'))
        self.assertEqual(test_user, False)

    def test_succesful_login(self):
        user = self.users.register_user(User.User('testi', 'testi'))
        test_user = self.users.login_user(user)
        self.assertEqual(test_user, user)
