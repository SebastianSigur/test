n = int(input("Enter the length of the sequence: ")) # Do not change this linegit log

#Writing algorithm where the next number is the sum of the previous two numbers 
last_last_number = 1
last_number = 2
number = 3
next_number = 0
if n == 1:
    print(1)
elif n == 2:
    print(1)
    print(2)
elif n == 3:
    print(1)
    print(2)
    print(3)
elif n > 0:
    print(1)
    print(2)
    print(3)
    for i in range(n-3):
       #print(number, last_number, last_last_number)
        next_number = number + last_number + last_last_number
        print(next_number)
        last_last_number = last_number
        last_number = number
        number = next_number
