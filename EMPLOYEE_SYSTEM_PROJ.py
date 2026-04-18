#EMPLOYEE_SYSTEM_PROJECT

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


class EmployeesManager:
    def __init__(self):
        self.employees = []

    # Add Employee
    def add_employee(self, name, age, salary):
        emp = Employee(name, age, salary)
        self.employees.append(emp)
        print("Employee added successfully!")

    # List Employees
    def list_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            print("\nEmployee List:")
            for emp in self.employees:
                emp.display()

    # Delete Employees by Age Range
    def delete_by_age(self, min_age, max_age):
        before = len(self.employees)
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        after = len(self.employees)

        print(f"{before - after} employee(s) deleted.")

    # Find Employee by Name
    def find_employee(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                print("Employee Found:")
                emp.display()
                return
        print("Employee not found.")

    # Update Salary
    def update_salary(self, name, new_salary):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                emp.salary = new_salary
                print("Salary updated successfully!")
                return
        print("Employee not found.")


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def menu(self):
        while True:
            print("\n===== Employee System Menu =====")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Delete Employees by Age Range")
            print("4. Find Employee by Name")
            print("5. Update Salary")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                salary = float(input("Enter salary: "))
                self.manager.add_employee(name, age, salary)

            elif choice == '2':
                self.manager.list_employees()

            elif choice == '3':
                min_age = int(input("Enter minimum age: "))
                max_age = int(input("Enter maximum age: "))
                self.manager.delete_by_age(min_age, max_age)

            elif choice == '4':
                name = input("Enter name to search: ")
                self.manager.find_employee(name)

            elif choice == '5':
                name = input("Enter name: ")
                salary = float(input("Enter new salary: "))
                self.manager.update_salary(name, salary)

            elif choice == '6':
                print("Exiting program...")
                break

            else:
                print("Invalid choice! Try again.")


# Run Program
if __name__ == "__main__":
    app = FrontendManager()
    app.menu()