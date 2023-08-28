class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_table(self, sorting_parameter):
        if sorting_parameter == 1:
            self.employees.sort(key=lambda emp: emp.age)
        elif sorting_parameter == 2:
            self.employees.sort(key=lambda emp: emp.name)
        elif sorting_parameter == 3:
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter")

    def print_table(self):
        for employee in self.employees:
            print(employee)


def main():
    employee_table = EmployeeTable()

    employee_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    employee_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    employee_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    employee_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    employee_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("1. Age")
    print("2. Name")
    print("3. Salary")
    
    sorting_parameter = int(input("Enter your choice: "))
    
    employee_table.sort_table(sorting_parameter)
    print("\nSorted Table:")
    employee_table.print_table()


if __name__ == "__main__":
    main()