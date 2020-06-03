import pytest

#Number = int(input("Please enter your Number: "))

def timestable(number):
    table = []
    for i in range(0, 101):
        i = number * i
        table.append(i)
    return(table)


    
def test_TT():
    assert 400 in timestable(4)