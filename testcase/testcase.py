from login import Get_data

class Login(Get_data):
    def __init__(self):
        self.token = Get_data().get_token()
        self.header_addusr = {'Content-Type': 'application/x-www-form-urlencoded', 'token': '%s' % self.token}
