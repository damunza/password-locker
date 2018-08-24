#!/usr/bin/env python3.6
from password import User , Credential

def create_profile(first_name,last_name,password):
    '''
    function to create a new user
    '''
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    '''
    function that saves new users
    '''
    User.save_user(user)

def verify_profile(first_name,password):
    '''
    function that verifies the existance of a user before continuing to the credentials
    '''
    verify_user = Credential.check_user(first_name,password)
    return verify_user

def create_cred(user_name,site_name,account_name,password):
    '''
    function that creates cred(s) for the account and details the user wants to save
    '''
    new_cred = Credential(user_name,site_name,account_name,password)
    return new_cred

def save_cred(credential):
    '''
    function that saves new credentials
    '''
    Credential.save_credentials(credential)

def display_creds():
    '''
    function that returns the saved credentials
    '''
    return Credential.display_creds()



def main():
    print (' ')
    print ('Welcome to Password Locker')
    while True:
        print('-'*50)
        print('use the following short-codes to navigate: \n cp-create profile \n li-log in \n ex-exit')
        short_code = input('Enter short-code: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'cp':
            print('-'*50)
            print(' ')
            print ('Fill in the following:')
            first_name = input('Enter your first name: ').strip()
            last_name = input('Enter your last name: ').strip()
            password = str(input('Enter password: '))
            save_user(create_user(first_name,last_name,password))
            print (' ')
            print (f'new account created for:{fname} {lname} and password is {password} ')

        elif short_code == 'li':
            print ('-'*50)
            print(' ')
            print('Enter details:')
            user_name = input('Enter your first name: ').strip()
            password = str(input('Enter your password: '))
            user_exists = verify_profile(user_name,password)
            if user_exists == user_name:
                print (' ')
                print ('waiting for more code')
            else:
                print(' ')
                print('Wrong Details! Try again or create profile')
        else:
            print('-'*50)
            print(' ')
            print ('Sorry pick another option')

if __name__ == '__main__':
	main()
