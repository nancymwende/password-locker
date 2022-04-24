
from click import option
from user import User
from credentials import Credentials

def create_user(first_name, last_name, password):
    '''
    function to create a new user.
    Args:
       first_name: New user first_name.
        last_name : New user last_name.
        password : New user password.
    '''
    new_user = User(first_name, last_name, password)
    return new_user

def save_user(contact):
    '''
    Function to save user
    '''
    User.save_user()

    

def delete_user(user):
    '''
    function to delete a user
    '''
    User.delete_user(user)

def find_by_first_name(first_name):
    '''
    method that takes in a name and returns the first_name that matches that name.
    '''
    return User.find_by_first_name(first_name)


def check_existing_user(first_name):
    '''
    method that checks if a user exists from the user list.
    '''
    return User.user_exists(first_name)

def create_user_info(media, user_details, password):
    '''
    function to delete user credentials   
    '''
    new_user_info = Credentials(media, user_details, password)
    return new_user_info

def save_user_info(info):
    '''
    function to save user info
    '''
    return Credentials.save_credentials(info)


def display_users_info(username):
    '''
    function to display user info
    '''
    return Credentials.display_credentials()


def display_all_users():
    '''
    function to display all users
    '''
    return User.display_users()

def generated_password():
    '''
    generates  a random password for users
    '''
    random_password = Credentials.generate_password()
    return random_password

def main():
    print("Hello..Welcome to password locker.what is your name kindly?")
    first_name = input()
    print(f"Hey {first_name}. what would you like to do?")
    print('\n')

    while True:
         print("Use these short codes : \n cr - Create an account \n ds -Display available users \n lg -Login to your account \n ex - Exit password locker")
         print("\n")

         option = input()
         if option == 'cr':
            print("~" * 15)
            print("Create an account")
            print("~" * 15)

            print("Enter your first_name")
            first_name = input()
            print("*" * 8)

            print("Enter your last_name")
            last_name = input()
            print("*" * 8)

            print("Enter your password")
            password = input()
            print("*" * 8)

            save_user(create_user(first_name, last_name, password))
            print("*" * 8)

            print(f"{first_name}, your account has been successfully created. You may proceed to login.")

         elif option == 'ds':
             if display_all_users():
                print("Below are the users:")
                print("~" * 15)

                for user in display_all_users():
                    print(f"first_name: {user.first_name}")
                    print(f"password: {user.password}")

         else:
                print("\n")
                print("No users at all!")
                print("\n")

         if option == 'lg':
            print("~" * 15)
            print("Login")
            print("~" * 15)

            print("Enter your first_name")
            first_name = input()
            print("*" * 8)

            print("Enter your password")
            password = input()
            print("*" * 8)

            print("\n") 

            authentification = check_existing_user(first_name)

            if authentification:
                print(f"Hey {first_name}, welcome back to password locker.")
                print("\n")

                while True:
                    print("*" * 15)
                    print("What would you like to do: \n 1 - Add information to your account \n 2 - Show your account details \n 3 - Terminate")
                    print("*" * 15)

                    option = int(input())


                    if option == 1:
                        print("~" * 15)
                        print("Add information to your account")
                        print("~" * 15)

                        print("*" * 8)
                        print("Enter the social media page:")
                        social_media = input()

                        print("*" * 8)
                        print(f"What is your {social_media} account profile?")
                        profile = input()

                        while True:
                            print("*" * 15)
                            print("What would you like to do: \n 1 - Create your own password \n 2 - Use a randomly generated password \n 3 - Terminate")
                            print("*" * 15)

                            option = int(input())

                            if option == 1:
                                print("~" * 8)
                                print("Enter a password of your choice")
                                password = input()
                                break

                            elif option == 2:
                                print("~" * 8)
                                password = generated_password()
                                break

                            elif option == 3:
                                break

                            else:
                                print("~" * 8)
                                print("Ooops! Wrong trial..Try again :)")
                                print("~" * 8)

                                save_user_info(create_user_info(first_name, last_name, password))
                        print(f"Hey {first_name}, your information has been updated succesfully. \n Username: {first_name} \n Password: {password}")
                        print("\n")

                    elif option == 2:
                        if display_users_info(first_name):
                            print("Enter a username")
                            print("~" * 8)


                            for new_user_info in display_users_info(first_name):
                                print(f"media:{new_user_info.media} \n Account: {new_user_info.profile} \n Password: {new_user_info.password}")

                        else:
                            print("No information for the given username")

                    elif option == 3:
                        break

            else:
                print("Oooops....we can't find this user.You can try again")




if __name__ == '__main__':

    main()
            

    











