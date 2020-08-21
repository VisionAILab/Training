class PyCharm:
    
    def execute(self):
        print("Compiling")
        print("Running")
        
        
class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

        
class Laptop:

    def code(self, ide):
        ide.execute()
        
        
ide = MyEditor()#We can pass either PyCharm or MyEditor provided it should have execute method in it.

lap1 = Laptop()
lap1.code(ide)
