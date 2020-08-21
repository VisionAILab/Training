class A:
    
    
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")


#Single Inheritance
class B(A): #class B inherits class A (Super calss - Sub class)
    
    
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")
        
#Multilevel Inheritance
class C(B):
    
    def feature5(self):
        print("Feature 5 is working")
    
#Multiple Inheritance
#class C(A,B): if class B is not inheriting class A then we use this so that class C can inherit both class A & B
  #       def feature5(self):
  #      print("Feature 5 is working")
        
        
a1 = A()
a1.feature1()
a1.feature2()


b1 = B()

c1 = C()
