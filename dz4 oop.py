class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = [] # завершенные_курсы
        self.courses_in_progress = [] # курсы_в_прогрессе
        self.grades = {} # оценки
        self.average_rating = 0 # средний_рейтинг

    def rate_hw1(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

        sum = 0
        len = 0
        for key in lecturer.grades.keys(): 
          for i in list(lecturer.grades[key]):
            sum = sum + i
            len += 1
        lecturer.average_rating = round(sum / len, 2)           
      

    def __str__(self):
      
        res = f"Имя: {self.name}\n"\
              f"Фамилия: {self.surname}\n"\
              f"Средняя оценка за домашние задания: {self.average_rating}\n"\
              f"Курсы в процессе изучения: {self.courses_in_progress}\n"\
              f"Завершенные курсы: {self.finished_courses}"
        return res
             
    def __lt__ (self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.average_rating < other.average_rating   

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw (self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'       

class Lecturer(Mentor):  

    average_rating = 0 
    grades = {} 

  


    def __str__(self):   
                  
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
            return
        return self.average_rating < other.average_rating



class Reviewer (Mentor):

    def rate_hw (self, student, course, grade):
        super().rate_hw(student, course, grade)
     
    
        sum = 0
        len = 0
        for key in student.grades.keys(): 
          for i in list(student.grades[key]):
            sum = sum + i
            len += 1
        student.average_rating = round(sum / len, 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'  
        return res  

# Lecturer

best_lecturer_1 = Lecturer ('Николай', 'Козлов')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Виктор', 'Крылов')
best_lecturer_2.courses_attached += ['Java']


# Reviewer

cool_reviewer_1 = Reviewer('Игорь', 'Петров')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Павел', 'Климов')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

# Student

student_1 = Student('Андрей', 'Краснов')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']

student_2 = Student('Егор', 'Киселев')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Git']



# оценки лекторам 

student_1.rate_hw1(best_lecturer_1, 'Python', 8)
student_1.rate_hw1(best_lecturer_1, 'Python', 10)
student_1.rate_hw1(best_lecturer_1, 'Python', 10)

student_1.rate_hw1(best_lecturer_2, 'Python', 9)
student_1.rate_hw1(best_lecturer_2, 'Python', 7)
student_1.rate_hw1(best_lecturer_2, 'Python', 8)

student_1.rate_hw1(best_lecturer_1, 'Python', 7)
student_1.rate_hw1(best_lecturer_1, 'Python', 8)
student_1.rate_hw1(best_lecturer_1, 'Python', 9)

student_2.rate_hw1(best_lecturer_2, 'Java', 10)
student_2.rate_hw1(best_lecturer_2, 'Java', 8)
student_2.rate_hw1(best_lecturer_2, 'Java', 9)



# оценки студентам

cool_reviewer_1.rate_hw(student_1, 'Python', 10)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 10)

cool_reviewer_2.rate_hw(student_2, 'Java', 8)
cool_reviewer_2.rate_hw(student_2, 'Java', 10)
cool_reviewer_2.rate_hw(student_2, 'Java', 9)


lecturer_list = [best_lecturer_1, best_lecturer_2] # список лекторов

student_list = [student_1, student_2] # список студентов



def rating_hw (students, courses):
    sum_grade = 0
    count_grade = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_grade += sum(value) / len(value)
                count_grade += 1
    return round(sum_grade / count_grade, 2)

def rating_lesson (lecturers, courses):
    sum_grade = 0
    count_grade = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_grade += sum(value) / len(value)
                count_grade += 1
    return round(sum_grade / count_grade, 2)


print("Список проверяющих :\n")

print(f"{cool_reviewer_1}\n")
print(f"{cool_reviewer_2}\n")
print("Список лекторов :\n")
print(f"{best_lecturer_1}\n")
print(f"{best_lecturer_2}\n")
print("Список студентов :\n")
print(f"{student_1}\n")
print(f"{student_2}\n")


print(f"Средняя оценка для всех студентов {'Python'}: {rating_hw(student_list, 'Python')}\n")

print(f"Средняя оценка для всех лекторов {'Python'}: {rating_lesson(lecturer_list, 'Python')}")

