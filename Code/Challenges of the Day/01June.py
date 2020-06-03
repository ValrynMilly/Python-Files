numbers = range(2000, 3001)
for i in numbers:
    if i % 7==0:
        numbers.append(i)
        if i *5!=0:
            numbers.append(i)
    print(numbers)