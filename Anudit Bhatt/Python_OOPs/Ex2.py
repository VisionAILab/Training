class Computer:
    
    def __init__(self):#Special Method (__init__) - it will automatically gets called for each object  
        print("in init")
    
    
    def config(self):#Method
        print("i5, 16gb, 1Tb")
        
        
com1 = Computer()#object creation
com2 = Computer()


com1.config()
com2.config()# Calling it form the object
