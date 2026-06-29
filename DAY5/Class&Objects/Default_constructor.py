#Default Constructor

class student:
    batch=4 #DATA
    #name="BAVITH"
    def __init__(self,name): #METHOD
        self.name=name
        print(self.name)
#create the instance/obj of class
s1=student("BAVITH")