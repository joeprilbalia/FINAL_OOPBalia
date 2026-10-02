# Problem 1: Inheritance and Method Extension

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is doing regular work.")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        super().work()
        print(f"{self.name} is managing {self.team_size} people.")


# Create a Manager object
manager = Manager("Ana", 80000, 5)

# Test the methods
print("Manager Name:", manager.name)
print("Manager Salary:", manager.salary)
print("Team Size:", manager.team_size)

print("\nWork:")
manager.work()

# Demonstrate inheritance
print("\nInheritance Check:")
print(isinstance(manager, Employee))
print(isinstance(manager, Manager))