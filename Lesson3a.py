# Working with Python Functions
def first_function():
    print("our first python function")

first_function()

def calculate_students_marks():
    English = 60
    Maths = 76
    Swahili = 80
    marks =English+Maths+Swahili
    return marks

print(calculate_students_marks())

def movement(movement_type):
    return  movement_type

print(movement("walking"))

def get_student_name(name):
    return f"My name is {name}"

print(get_student_name("Jack"))

def calculate_students_marks(English,Maths,Swahili):

    marks =English+Maths+Swahili
    return marks

print(calculate_students_marks(60,76,80))

def students_details(name,age,**marks): # one * u store more than 1 mk,2** u store a dictionary
    return name,age,marks

print(students_details("Jack",19,English=80,Maths=88,Swahili=54))


def area_of_circle(radius):
    area = 3.142*radius*radius
    return f"the area is {area}" # in python 3.7 use f"the area is {area}" to format the string

print(area_of_circle(10))
