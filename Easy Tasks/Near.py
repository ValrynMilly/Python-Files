first_string = input("First Word: ")
second_string = input("Second Word: ")

if all(x in first_string for x in second_string):
    print("True")
else:
    print("False")