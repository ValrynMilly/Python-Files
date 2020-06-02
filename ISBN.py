numbers = input("please enter your 13 Digit ISBN number: ")
digits = [int(x) for x in str(numbers)]
#print(digits)
new_digits = []

for i in digits:
    if int(i) % 2 != 0:
        new_digits.append(i)
    elif int(i) % 2 == 0:
        i=i*3
        new_digits.append(i)
allsum = sum(new_digits) / 10
print(allsum)