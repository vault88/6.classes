class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
  def average_grade(self):
    if len(sum(self.grades.values(), [])) == 0:
      average_grade = 'Нет оценок'
    else:
      average_grade = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
    return average_grade
  def __lt__(self, other):
    if not isinstance(other, Student):
      print('Not a Student!')
      return
    return self.average_grade() < other.average_grade() 
  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {", ".join([str(item) for item in self.courses_in_progress])}\nЗавершенные курсы: {", ".join([str(item) for item in self.finished_courses])}'
  def rate_hw(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
  
class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}
  def average_grade(self):
    if len(sum(self.grades.values(), [])) == 0:
      average_grade = 'Нет оценок'
    else:
      average_grade = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
    return average_grade
  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Not a Lecturer!')
      return
    return self.average_grade() < other.average_grade() 
  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'

class Reviewer(Mentor):
  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}'
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'

 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)