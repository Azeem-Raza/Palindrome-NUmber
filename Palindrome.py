def isPalindrome(x):
    num_str = str(x)
    return num_str == num_str[::-1]
num = int(input("Enter number: "))

if isPalindrome(num):
    print("is Plaindrome")
else:
    print("not palindrome")
    