
import unittest
from user import User

class TestUser(unittest.TestCase):
     '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
     '''

     def setUp(self):
    
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("nancy","mwende","1234567") # create user object


     def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"nancy")
        self.assertEqual(self.new_user.last_name,"mwende")
        self.assertEqual(self.new_user.password,"1234567")


     def test_save_user(self):
        '''
        test case that tests if the user is being saved properly
        '''
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.User_list),1)

     def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.User_list = []




     def test_save_multiple_user(self):
         '''
            to check if we have multiple users
         '''

         self.new_user.save_user()
         test_user = User("Catherine","kimani","00345678",) # new user
         test_user.save_user()
         self.assertEqual(len(User.User_list),2)
    


     def test_delete_user(self):
             '''
             to test if we can remove a user from our user_list
             '''
             self.new_user.save_user()
             test_user = User("Cate","kimani","234567",) # new user
             test_user.save_user()

             self.new_user.delete_user() # Deleting a user object
             self.assertEqual(len(User.User_list),1)

     
     def test_find_user_by_first_name(self):
        '''
        test to check if we can find a user by first_name.
        '''

        self.new_user.save_user()
        test_user = User("Cate","kimani","234567",) # new user
        test_user.save_user()

        found_user = User.find_by_first_name("Cate")

        self.assertEqual(found_user.first_name,test_user.first_name)
     def test_user_exists(self):
        '''
        test to see if we can return a boolean if we cant find a user.
        '''
        self.new_user.save_user()
        test_user = User("Cate", "kimani", "234567")
        test_user.save_user()

        user_exists = User.user_exists("Cate")
        self.assertTrue(user_exists)


     def test_display_all_users(self):
        '''
        method that returns a list of all users saved.
        '''
        self.assertEqual(User.display_users(), User.User_list)

         

if __name__ == '__main__':
    unittest.main()
        
