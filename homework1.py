# Створення системи обліку студентів:

# Створіть клас Student, який представлятиме студента з атрибутами ім'я, вік, курс та середній бал.

# Реалізуйте метод __init__, який ініціалізуватиме атрибути об'єкта класу Student.
# Створіть метод get_info, який виводитиме інформацію про студента (ім'я, вік, курс, середній бал).
# Додайте метод increase_year, який збільшуватиме курс студента на 1.
# Реалізуйте метод update_grade, який оновлюватиме середній бал студента з урахуванням переданої оцінки за іспит.
# Створіть кілька об'єктів класу Student та продемонструйте роботу всіх створених методів.

class Student:
    def __init__(self, name, age, year, gpa):
        self.name = name
        self.age = age
        self.year = year
        self.gpa = gpa

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Year: {self.year}")
        print(f"GPA: {self.gpa}")

    def increase_year(self):
        self.year += 1

    def update_grade(self, exam_mark):
        self.gpa = (self.gpa + exam_mark) / 2

# Приклад
student1 = Student("John Doe", 20, 1, 3.5)
student2 = Student("Jane Doe", 21, 2, 3.9)

# Демонстрація методів
student1.get_info()
student1.increase_year()
student1.update_grade(85)
student1.get_info()

student2.get_info()
student2.increase_year()
student2.update_grade(90)
student2.get_info()