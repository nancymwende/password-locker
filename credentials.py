import random
import string



class Credentials:
    #class that generates new user credentials
    Credentials_list=[]
    def __init__(self, media,user_details,password):
        '''
           __init__ method that helps us define properties for our objects.
        self.media= media
        self.user_details= userde_tails
        self.password = password
        '''
        self.media= media
        self.user_details = user_details
        self.password = password

    def save_credentials(self):
         '''
        function that saves user credentials
        '''
         Credentials.Credentials_list.append(self)



    def delete_credentials(self):
         '''
        method deletes a saved credential from the credentials list.
         '''
         Credentials.Credentials_list.remove(self)


    @classmethod
    def display_credentials(cls):
         '''
        function to display all user credentials
         '''
         return cls.Credentials_list


def generate_password(length = 6, password = string.hexdigits):
        '''
        function to generate a random password
        '''
        generated_password = ''.join(random.choice(password) for i in range(length))
        return generate_password


