def is_palindrome(x):
    strX = str(x)
    strXReversed = strX[::-1]
    if (strX == strXReversed):
        return True
    else:
        return False
    
# Execution starts here
largestPalindrome = 0
num = 0
for j in range(100, 999):
    for k in range(100, 999):
        num = j * k
        if num > largestPalindrome and is_palindrome(num):
            largestPalindrome = num
            
print "Largest palindrome is:" + str(largestPalindrome) 
    