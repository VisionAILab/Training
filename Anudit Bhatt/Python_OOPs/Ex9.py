class A:
    
    def __init__(self):
        print("in A INIT")
        
        
    def feature1(self):
        print("Feature 1 is working")
        
    def feature2(self):
        print("Feature 2 is working")


#Single Inheritance
class B(A): #class B inherits class A (Super calss - Sub class)
    
    def __init__(self):#If B has its own init it will print that if not found it will print init of super class
        super().__init__()#to call the init of class A or super class we use this
        print("in B INIT")
        
        
# In case of Multiple in heritance
        #class C(A,B)
     #    def __init__(self):
     #   super().__init__()
     #   print("in C INIT")
# Then it will first print init of C then it will print init of A and not of B because of MRO Method Resolution Order which works from left to right So A was in left side so it takes A
        
        
a1 = B()