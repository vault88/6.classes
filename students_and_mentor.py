student_list = []
lecturer_list = []
class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
    student_list.append(self)
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
    lecturer_list.append(self)
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

def average_students(student_list, course):
  sum_ = []
  for person in student_list:
    if course in person.courses_in_progress:
      sum_ += person.grades.get(course)
  if not len(sum_) == 0:
    result = round(sum(sum_)/len(sum_), 1)
    return f'Cредняя оценка за домашние задания по всем студентам курса {course}: {result}'
  else:
    return f'На курсе "{course}" нет студентов!'

def average_lecturers(lecturer_list, course):
  sum_ = []
  for person in lecturer_list:
    if course in person.courses_attached:
      sum_ += person.grades.get(course)
  if not len(sum_) == 0:
    result = round(sum(sum_)/len(sum_), 1)
    return f'Cредняя оценка за лекции всех лекторов в рамках курса {course}: {result}'
  else:
    return f'На курсе "{course}" нет лекторов!'

# Students
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
other_student = Student('Adam', 'Sandwich', 'your_gender')
other_student.courses_in_progress += ['Python']

# Lecturers
some_lecturer = Lecturer('Gilderoy', 'Lockhart')
some_lecturer.courses_attached += ['Python','Git']
other_lecturer = Lecturer('Horace', 'Slughorn')
other_lecturer.courses_attached += ['Python']

# Reviewers
some_reviewer = Reviewer('Quirinus', 'Quirrell')
some_reviewer.courses_attached += ['Python','Git']
other_reviewer = Reviewer('Severus', 'Snape')
other_reviewer.courses_attached += ['Python']

# Rating
some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Git', 7)
some_student.rate_hw(other_lecturer, 'Python', 7)
other_student.rate_hw(some_lecturer, 'Python', 10)
other_student.rate_hw(other_lecturer, 'Python', 7)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Git', 6)
some_reviewer.rate_hw(other_student, 'Python', 3)
some_reviewer.rate_hw(other_student, 'Python', 4)
other_reviewer.rate_hw(some_student, 'Python', 8)
other_reviewer.rate_hw(some_student, 'Git', 9)
other_reviewer.rate_hw(other_student, 'Python', 6)
other_reviewer.rate_hw(other_student, 'Python', 5)

print('------------Start here------------')
print(some_student)
print('----------------------------------')
print(other_student)
print('----------------------------------')
print(some_lecturer)
print('----------------------------------')
print(other_lecturer)
print('----------------------------------')
print(some_lecturer == other_lecturer)
print(some_student > other_student)
print('----------------------------------')

print(average_students(student_list, 'Git'))
print(average_lecturers(lecturer_list, 'Python'))