class Computer:
    
    def __init__(self,cpu,ram):#Special Method (__init__) - it will automatically gets called for each object  
        self.cpu = cpu
        self.ram = ram
    
    
    def config(self):#Method
        print("Config is :", self.cpu, self.ram) #cpu and ram are not local variable, they are objects thats why we write self.cpu and self.ram
        
        
com1 = Computer('i5', 16)#object creation
com2 = Computer('Ryzen 3', 8)


com1.config()
com2.config()# Calling it form the object