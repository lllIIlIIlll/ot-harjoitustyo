import unittest
import User
from repositories import user_repo

class TestUserRepo(unittest.TestCase):
    def setUp(self):
        self.user = User.User('arttu', 'jsdfgsd')

    def test_registration_username_taken(self):
        users = user_repo.UserRepo()
        users.register_user(self.user)
        test_user = users.register_user(self.user)
        self.assertEqual(test_user, False)
    
    def test_registration(self):
        users = user_repo.UserRepo()
        users.destroy_db_instances_for_testing()
        test_user = users.register_user(self.user)
        print(test_user)
        self.assertEqual(test_user.username, self.user.username)
