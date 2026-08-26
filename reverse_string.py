def reverseString(s):
    f=0
    l=len(s)-1
    while f<l:
        s[f],s[l]=s[l],s[f]
        f=f+1
        l=l-1
n=int(input("Enter no.of charecters in array:"))
s=[]
for i in range(n):
    c=input(f"Charecter {i+1}:")
    s.append(c)
print("s =",s)
reverseString(s)
print("Reversed s is :",s)
