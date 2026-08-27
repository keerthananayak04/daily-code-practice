def validPalindrome(s):
    p=""
    for i in s:
        if i.isalnum():
            p+=i
    rp=p[::-1]
    if p.lower()==rp.lower():
        return True
    else:
        return False
s=input("Enter a String:")
print(validPalindrome(s))
