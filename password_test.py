import unittest # importing the unittest module
from password import User ,Credential #first imported user class then import credential class

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

class TestCredentials(unittest.TestCase):
    '''
    a test class that tests the behaviours of the credentials class
    '''
    def test_confirm_user(self):
        '''
        a test to check whether the user that is trying to log in is a registered user
        '''
        self.new_user = User("Daniel","Mutai","abcd12")
        self.new_user.save_user()
        mpya=User("ddd","ccc","ab12")
        mpya.save_user()

        for user in User.users_list:
            if user.first_name == mpya.first_name and user.password == mpya.password:
                current_user = user.first_name
                return current_user
                self.assertEqual(current_user,Credential.check_user(mpya.firts_name,mpya.password))

    def setUp(self):
        '''
        creates accounts before each test
        '''
        self.new_cred =Credential("Daniel","instagram","Damunza","1234")

    def test_init_(self):
        '''
        test to check the creation of new user details
        '''
        self.assertEqual(self.new_cred.user_name,'Daniel')
        self.assertEqual(self.new_cred.site_name,'instagram')
        self.assertEqual(self.new_cred.account_name,'Damunza')
        self.assertEqual(self.new_cred.password,'1234')

    def test_save_credentials(self):
        '''
        test to check if the new credentials are being saved into the creds_list
        '''
        self.new_cred.save_credentials()
        self.assertEqual(len(Credential.creds_list),1)

    def tearDown(self):
        '''
        function to clear creds_list before every test
        '''
        Credential.creds_list = []

    def test_display_credentials(self):
        '''
        test to check whether display_creds method displays the credentials entered
        '''
        self.new_cred.save_credentials()
        instagram = Credential('dan','instagram','damunza','1234')
        instagram.save_credentials()
        self.assertEqual(Credential.display_creds(),Credential.creds_list)

    def test_find_site_creds(self):
        '''
        test for whether find_site method returns the correct site credentials
        '''
        self.new_cred.save_credentials()
        instagram = Credential('dan','Instagram','damunza','1234')
        instagram.save_credentials()
        creds_exist = Credential.find_site('Instagram')
        self.assertEqual(creds_exist,instagram)

if __name__ == '__main__':
    unittest.main()
