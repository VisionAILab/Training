class Car:
    
    wheels = 4 #This is a class variable
    
    
    
    def __init__(self):# All the variables inside init are instance variables
        self.mil = 10
        self.com = "BMW"
        
        ### If we ant to change the value of class variables
Car.wheels = 5 #This is the way to change the value of class variables
        
        
c1 = Car()
c2 = Car()

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)