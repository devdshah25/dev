# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
number1, number2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(number1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(number1)
        nth = number1 + number2
        # update values
        number1 = number2
        number2 = nth
        count += 1
