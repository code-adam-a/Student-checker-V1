def listsort(list):
    sorted = False
    pair1 = 0
    pair2 = 1
    subPair = 1
    while not sorted:
        try:
            if list[pair1][subPair]<list[pair2][subPair]:
                f=list.pop(pair2)
                for row in list:
                    if f[1] > row[1]:
                        position = list.index(row)
                        list.insert(position, f)
                        break
                    else:
                        pass
                pair1+=1
                pair2+=1
            else:
                pair1 += 1
                pair2 += 1
        except IndexError:
            sorted = True
    return list

class student():
    def __init__(self, name, result, grade):
        self.name = name
        self.result = result
        self.grade = grade
    def formatfile(self):
        return f"{self.name}, {self.result}, {self.grade}\n"
    def formatrow(self):
        return [self.name, self.result, self.grade]

students = []

valid_number = False
while not valid_number:
    try:
        number_of_students = int(input("How many students in the class:\n"))
    except ValueError:
        print("Invalid input, please enter a whole number")
    else:
        if number_of_students not in range(6,37):
            print("Invalid number, minimum students - 6, maximum students - 36")
        else:
            valid_number = True


for i in range(number_of_students):
    valid_name = False
    valid_counter = 0
    valid_result = False
    while not valid_name:
        student_name = input("Input students name:\n")
        if len(student_name) == 0:
            print("Invalid input, student name cannot be empty")
        else:
            for letter in student_name:
                if ord(letter.lower()) not in range(97, 123) and letter != " ":
                    valid_counter -= 1
                    print("Invalid name, please do not use special characters or numbers")
                    break
                else:
                    valid_counter += 1
                if valid_counter == len(student_name):
                    valid_name = True

            
    while not valid_result:
        try:
            student_result = int(input("input students test result:\n"))
        except ValueError:
            print("Invalid result, please enter whole number for students result\n")
        else:
            if student_result not in range(0,101):
                print("Invalid result, maximum marks is 100\n")
            else:
                valid_result = True

    # student grade calculator
    if student_result < 40:
        student_grade = "fail"
    elif student_result in range(40,51):
        student_grade = "pass"
    elif student_result in range(51,70):
        student_grade = "merit"
    else:
        student_grade = "distinction"

    data = student(student_name, student_result, student_grade)
    row_data = data.formatrow()
    students.append(row_data)

sorted_students = listsort(students)

student_file = open("students.txt", "w")

for i in range(len(sorted_students)):
    print(sorted_students[i])
    student_file.write(f"{sorted_students[i][0]}, {sorted_students[i][1]}, {sorted_students[i][2]}\n")
    if sorted_students[i][2] == "distinction":
        print("This student achieved a distinction\n")


student_file.close()
input()
