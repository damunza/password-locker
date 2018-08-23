class User:
    '''
    a class that defines the name(s) and password  of the user
    '''
    user_list = []
    # 
    # def save_user(self):
    #     '''
    #     method that adds user(s) into the user_list
    #     '''
    #
    #     User.user_list.append(self)

    def _init_(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
