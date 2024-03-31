class Employee():
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
    def emp_assign_department(self, department):
        #change department of employee
        self.department = department
    def emp_detail(self):
        return self.id, self.name, self.salary, self.department
    def calculate_salary(self, hours):
        if hours>50:
            overtime= hours - 50
            overtimeAmount =( overtime * (self.salary/50))
            return overtimeAmount
        else:
            return self.salary*hours
def main():
        emp1 = Employee(1, "Nguyen Van A", 1000000, "HR")
        emp1.emp_assign_department("IT")
        print(emp1.emp_detail())
        print(emp1.calculate_salary(60))
if __name__ == "__main__":
        main()
