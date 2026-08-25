def removeElement(nums,val):
    while nums.count(val)!=0:
        nums.remove(val)
    return len(nums)
n=int(input("Enter number of elements in the list:"))
nums=[]
for i in range(n):
    e=int(input(f"Enter a element {i+1}:"))
    nums.append(e)
print(f"List: {nums}")
val=int(input("Enter the value to remove:"))
r=removeElement(nums,val)
print(f"List after removing the {val} :\n{nums}")
print(f"Number of elements in list after removing given value {val} is:{r}") 
