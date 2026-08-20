# Banking  software 
from abc import ABC , abstractmethod 

class BankApp(ABC) : 
    def database(self) :
        return "Database Connected Successfully ! "

    @abstractmethod
    def security(self) :     # we 
        pass 

    @abstractmethod 
    def display(self) : 
        return "This is the display !" 

class MobileApp(BankApp) :       # inherits BankApp      Webapp 

    def mobile_login(self) :
        return("Login to mobile !")

    def security(self) :     # after implementing this ---- then only we can make object of MobileApp 
        return "Mobile app is secured" 

    def display(self):     # after implementing this ---- then only we can make object of MobileApp 
        return "This is the mobile display !"



myapp = MobileApp()  
print(myapp.mobile_login())   
print(myapp.security())  
print(myapp.display())   


