import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
         '''
        Set up method to run before each test cases.
        '''
         self.new_credentials = Credentials("twitter","kelvin","1238990") # create credentials object

        
    def test_init(self):
        '''
        tests if the objects are being initialized properly.
        '''
        self.assertEqual(self.new_credentials.media, "twitter")
        self.assertEqual(self.new_credentials.user_details, "kelvin")
        self.assertEqual(self.new_credentials.password, "1238990") 


    def test_save_credentials(self):
        '''
        test case that checks if credentials is saved properly.
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.Credentials_list),1)


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.Credentials_list = []


    def test_save_multiple_credentials(self):
        '''
        test case to check whether we can save multiple credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials= Credentials("Instagram", "howard", "moringa1234")
        test_credentials.save_credentials()

    def test_delete_credentials(self):
        '''
        test case that checks if a credential can be removed.
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram", "howard", "moringa1234")
        test_credentials.save_credentials()

        test_credentials.delete_credentials()
        self.assertEqual(len(Credentials.Credentials_list),1)

    def test_display_all_credentials(self):
        '''
        test case to check whether we can display all user credentials.
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram", "howard", "moringa1234")
        test_credentials.save_credentials()

        self.assertEqual(Credentials.display_credentials(), Credentials.Credentials_list)



if __name__ == '__main__':
    unittest.main()

        





