class faculty:
    def __init__(self,a,b,c):
      self.f_id = a
      self.name = b
      self.salary = c
    def display(self):
       print("Faculty ID:",self.f_id) 
       print("Faculty name:",self.name) 
       print("Faculty salary:",self.salary) 
a = faculty(1, 'Mahyishba', 100000)
a.display()       
       