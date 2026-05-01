class Employee:
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} - {self.level} - ${self.salary}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string")
        self._name = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value not in Employee._base_salaries:
            raise ValueError("Invalid level")
        self._level = value
        self.salary = Employee._base_salaries[value]

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be number")
        self._salary = value


# 🔥 Create list of employees
employees = []

# Add 100 employees
for i in range(1, 101):
    emp = Employee(f"Employee{i}", "trainee")
    employees.append(emp)

# 🔹 Show all employees
for emp in employees:
    print(emp)