#Write a simple program that checks if a student exists in a register list and prints if the student is in the list
#absent if the student is not
#use the for loop
Student_List=["Jane","Mary" ,"David", "Nancy", "Agnes" ]
Name = input ("Enter a name")
print("You entered a name",Name)

#for Name in Student_List:
   # print("The student is Present")
#the for loop does not work for this

#using the if, else
if Name in Student_List:
    print(Name,"is present")
else:
    print(Name,"is absent")


# in python else if is written as elif
A=range(80,100)
B=range(60,80)
C=range(50,60)
marks = int(input ("Enter student's marks"))
if marks in A:
        print("Your grade is A")
elif marks in B:
        print("Your grade is B")
elif marks in C:
        print("YOur grade is C")
else:
        print("not categorised")