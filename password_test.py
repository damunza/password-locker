import unittest # importing the unittest module
from password import User #first imported user

class TestUser(unittest.TestCase):
    '''
    a test class to run test cases on the behaviour of the user class
    '''

# making the setup
    def setUp(self):
        '''
        what runs before each test
        '''
        self.new_user = User("Daniel","Mutai","abcd12")

    def test_init_(self):
        '''
        testing whather objects is initialized correctly
        '''
        self.assertEqual(self.new_user.first_name,"Daniel")
        self.assertEqual(self.new_user.last_name,"Mutai")
        self.assertEqual(self.new_user.password,"abcd12")

    def test_save_user(self):
        '''
        test to check whether user information is being saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

    def tearDown(self):
        '''
        cleans up after each test runs
        '''
        User.users_list = []

if __name__ == '__main__':
    unittest.main()
