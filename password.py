class User:
    '''
    a class that defines the name(s) and password  of the user
    '''
    users_list = []


    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        method that adds user(s) into the user_list
        '''

        User.users_list.append(self)

class Credential:
    '''
    a classs to create the create an account , save the passwords and sites then generate passwords
    '''
    creds_list =[]
    user_creds_list=[]