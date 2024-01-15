class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()
        self.courses_attached = []
    
    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        some_student = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname}\n' \
                       f'Средняя оценка за домашние задания: {self.average_rating}\n' \
                       f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
                       f'Завершенные курсы: {finished_courses_string}'
        return some_student
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.average_rating < other.average_rating                         
           
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
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
        self.average_rating = float()
    def _str_(self):
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return some_student 
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.average_rating < other.average_rating
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def _str_(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'                         

student_1 = Student('Igor', 'Ivanov')
student_1.courses_in_progress += ['Git', 'Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Kiril', 'Petrov')
student_2.courses_in_progress += ["Git", 'Python']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Egor', 'Sidorov')
student_3.courses_in_progress += ['Git', 'Python']
student_3.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Irina', 'Ivanova')
lecturer_1.courses_attached += ['Git', 'Python']

lecturer_2 = Lecturer('Natalia', 'Petrova')
lecturer_2.courses_attached += ['Git']

lecturer_3 = Lecturer('Alena', 'Sidorova')
lecturer_3.courses_attached += ['Python']

reviewer_1 = Reviewer('Anton', 'Pupkin')
reviewer_1.courses_attached += ['Git', 'Python']

reviewer_2 = Reviewer('Alex', 'Dorofeev')
reviewer_2.courses_attached += ['Git']

reviewer_3 = Reviewer('Sergey', 'Vanin')
reviewer_3.courses_attached += ['Python']

student_1.rate_hw(lecturer_1, 'Git', 10)
student_1.rate_hw(lecturer_1, 'Python', 7)
student_1.rate_hw(lecturer_2, 'Git', 9)
student_1.rate_hw(lecturer_3, 'Python', 10)

student_2.rate_hw(lecturer_1, 'Git', 10)
student_2.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_2, 'Git', 10)
student_2.rate_hw(lecturer_3, 'Python', 5)

student_3.rate_hw(lecturer_1, 'Git', 6)
student_3.rate_hw(lecturer_1, 'Python', 10)
student_3.rate_hw(lecturer_2, 'Git', 8)
student_3.rate_hw(lecturer_3, 'Python', 9)

reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Git', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_3, 'Git', 6)
reviewer_1.rate_hw(student_3, 'Python', 8)

reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_3, 'Git', 8)

reviewer_3.rate_hw(student_1, 'Python', 7)
reviewer_3.rate_hw(student_2, 'Python', 10)
reviewer_3.rate_hw(student_3, 'Python', 6)

student_list = [student_1, student_2, student_3]

lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

def student_rating(student_list, course_name):
  sum_all = 0
  count_all = 0
  for student in student_list:
      if course_name in student.grades:
          sum_all += sum(student.grades[course_name])
          count_all += len(student.grades[course_name])
  return sum_all / count_all
            
def average_rating_lecturer(lecturer_list, course):
    sum_all = 0
    count_all = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            sum_all += sum(lecturer.grades[course])
            count_all += len(lecturer.grades[course])
    return sum_all / count_all

print(f"Средняя оценка для всех студентов по курсу {'Git'}: {student_rating(student_list, 'Git')}")

print(f"Средняя оценка для всех лекторов по курсу {'Git'}: {average_rating_lecturer(lecturer_list, 'Git')}")
