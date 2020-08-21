class Computer:
    def __init__(self):
        self.name = "Anudit"
        self.age = 21
        
    def update(self):
        self.age = 26
    
    def compare(self,other):#compare(who is calling, whom is calling)
        if self.age == other.age:
            return True
        else:
            return False




c1 = Computer()
c2 = Computer()

#c1.name = "Rashi"
c1.age = 12


#c1.update()# here self works as a pointer to c1 object

if c1.compare(c2):
    print("They are same")
else: 
    print("They are not same")
#print(id(c1))#this gives the address of the object(c1) in heap memory. There will be different memory address each time you run the code


print(c1.name)
print(c1.age)
print(c2.name)