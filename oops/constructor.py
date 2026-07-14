class faculty:
    def __init__(self):
      self.id = int(input("Enter faculty ID:"))
      self.name = input("Enter faculty name:")
      self.salary = float(input("Enter faculty salary:"))
    def display(self):
       print("Faculty ID:",self.id)
       print("Faculty name:",self.name)
       print("Faculty salary:",self.salary)
a = faculty()
a.display()   
       


    


