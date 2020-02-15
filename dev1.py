



print("To check the greater number from the given number!".center(70,'-'))

# To take a numbers as an input from the user.

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

# To check among the numbers which is greatest.
# We do this using if,else condition


if first_num > second_num and first_num > third_num:
    print("The first number is the greatest among other numbers which is " ,first_num)
    
elif second_num > first_num and second_num > third_num:
    print("The second number is the greatest among other numbers which is " ,second_num)
    
else:
    print("The first number is the greatest among other numbers which is " ,third_num)
    

print("Program Over!!".center(70,'-'))
