#maths = input("Please enter your Maths Mark: ")
#chemistry = input("Ok now please enter your chemistry mark: ")
#physics = input("And finally please enter your physics mark: ")
import pytest

def calculator(num1, num2, num3):
    Grade = float(num1) + float(num2) + float(num3)
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
    elif average >= 70:
        print("Congratulations you got a 'A'")
        
    out = [Grade, average]
        
    return out

            
def test_Calculator():
    assert calculator(80,80,80) == [240.0, 80]
