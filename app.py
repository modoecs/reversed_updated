def reversed_number(n):
    reversed_number = 0
    number = str(n)
    length = len(number)
    for i in range(length-1, -1, -1):
      digit = int(number[i])
      reversed_number = reversed_number *10 + digit
    return reversed_number
number = int(input("enter a number :- "))
print("reversed number :- ", reversed_number(number))