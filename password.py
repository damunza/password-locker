class User:
    '''
    a class that defines the name(s) and password  of the user
    '''
    user_list = []

    def _init_(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
