class employee:
    def put_data(self):
        self.id = int(input("Enter employee ID:"))
        self.name = input("Enter employee name:")
        self.salary = float(input("Enter employee salary:"))
    def display(self):
        print("Employee ID:", self.id)    
        print("Employee name:", self.name)    
        print("Employee salary:", self.salary)    
a = employee()
a.put_data()
a.display()
