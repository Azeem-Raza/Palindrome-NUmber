def PalindromeInt(x):
    #if x is smaller than 0 
    if x <= 0 or (x != 0 and x % 10 == 0):
        return False
    reverse = 0
    #e.g x is 121
    while x > reverse:
        #reverse is 0, reminder of 121 % 10 is 1. 
        reverse = reverse * 10 + x % 10
        # now reverse is 1
        #x is 121, to make the last digit disappear divided by 10. 
        x //= 10
        #After dividing x is 12.
        #Iteration will repeat until it reverse all number digits.
        #comparing orignal x 121 with reverse.
    return x == reverse or x == reverse // 10

num = int(input("Enter a number: "))

# Check if the number is a palindrome
if PalindromeInt(num):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")