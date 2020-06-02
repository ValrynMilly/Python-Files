print("Welcome to your grade calculator!")
print("")
maths = input("Please enter your Maths Mark: ")
chemistry = input("Ok now please enter your chemistry mark: ")
physics = input("And finally please enter your physics mark: ")
print("")
Grade = float(maths) + float(chemistry) + float(physics)
average = int(Grade / 3)

print("Your grade is ", Grade, "& your average is", average,"%")

if average < 40:
    print("You Failed")
elif int(average) in range(40, 49):
    print("Congratulations you got a 'D'")
elif int(average) in range(50, 59):
    print("Congratulations you got a 'C'")
elif int(average) in range(60, 69):
    print("Congratulations you got a 'B'")
elif average > 70:
    print("Congratulations you got a 'A'")