mark1 = int(input("Enter mark1 : "))
mark2 = int(input("Enter mark2 : "))
mark3 = int(input("Enter mark3 : "))

total_marks = 300
total_percentage = 100 * ((mark1+mark2+mark3)/total_marks)

if(total_percentage > 40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You are pass : ",total_percentage)
else:
    print("You are failed, try next year : ",total_percentage)

