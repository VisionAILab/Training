class Student:
    
    school = "XYZ"
    
    
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    
    def get_m1(self): #for fetching the value (ACCESSORS)
        return self.m1
    
    
    def set_m1(self, value): #foe modification in the value (MUTATORS)
        self.m1 = value
        
        
    @classmethod #This decorators are used for class Variables   
    def info(cls):# for working with class variables cls is used instead of self
        return cls.school
    
    
    @staticmethod #this decorator is used of static variables
    def info1():# we keep the brackets empty in case of static methods
        print("This is student class.....in abs module")





s1 = Student(34,47,32)
s2 = Student(89,32,12)

print(s1.avg())
print(s2.avg())
print(Student.info())

Student.info1()