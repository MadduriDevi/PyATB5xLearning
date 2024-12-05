

# Web Automation - Selenium
# Page - You are going automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "Devi@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Success")
        else:
            print("Login Failed")


#email = Read from excel , CSV or ENV file
#password = Read from excel,CSV or ENV file

#vwo_obj = VWOLoginPage(email, password)
#vwo_obj.login_confirm()

Devi = VWOLoginPage("pramod@gmail.com", "Pass123")
Devi.login_confirm()