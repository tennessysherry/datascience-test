
# while loop for getting a correct password

correct_password = "password123"
trial_count = 0
count_limit = 3

while (trial_count<count_limit):
    trial_count+=1
    guess_password = input('Enter password')
    if(correct_password==guess_password):
        print("correct password")
        break
    else:
        print("incorrect password")

else:
    print("you have exceeded your trials")


    # for loop to list numbers and letters

for item in range(1,10):
    print("item",item)

for letter in ("Tennessee"):
    print("letter",letter)







