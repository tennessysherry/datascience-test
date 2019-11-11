# working with lists in python
employees = ["Jane", "Jennifer", "John", "Peter"]
employee_numbers=[100,101,102.103,104]
print(type(employees))
print(employees)
print(employee_numbers)
#this demonstrates adding items to a list i.e new items to the old list of employees
add_employees= []
add_employees.insert(0,"Mike")
add_employees.insert(1,"Jack")
add_employees.insert(2,"Johnny")
print(add_employees)
#using add list function, This does not require one to assign an identifier/location to the list
add_employees.append("Martin")
print(add_employees)
