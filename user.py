


class User:
    # "class that generates new instances of a User"
    User_list=[]
    def __init__(self, first_name,last_name,password):
        
        '''
        __init__ method that helps us define properties for our objects.
        self.first_name= first_name
        self.last_name = last_name
        self.password = password
        '''
        self.first_name= first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
         '''
        function that adds  new user to the user list
        '''
         User.User_list.append(self)

    def delete_user(self):
         '''
        method deletes a saved user from the user list.
         '''
         User.User_list.remove(self)

    @classmethod
    def find_by_first_name(cls,first_name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.User_list:
            if user.first_name == first_name:
                return user

    @classmethod
    def user_exists(cls, first_name):
        '''
        method that checks if a user exists from the user list.
        Args:
            first_name:first_name to search if it exists.
        Returns:
            Boolean: true or false depending if the user exists.
        '''
        for user in cls.User_list:
            if user.first_name == first_name:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.User_list            