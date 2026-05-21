class Employee:
    company_name = "TeachMeSkills"  # атрибут класса (общий для всех)

    def __init__(self, name: str):
        self.name = name  # атрибут объекта (у каждого свой)


emp1 = Employee("Алексей")
emp2 = Employee("Мария")

print(emp1.company_name)  # TeachMeSkills
print(emp2.name)  # Мария

Employee.company_name = "TMS"  # Меняем атрибут класса
print(emp1.company_name)  # TMS
