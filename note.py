#Taking total amount a input from user
amount =int(input("please enter amount from withdraw:"))

#calculating the number of notes diffrent deomineton
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10


print("notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)