n=input("enter the number")
temp=0
l=len(n)
for i in range(l):
    temp=temp+pow(int(n[i]),l)
print(temp)
if(int(n)==temp):
    print("arm")
else:
    print("not arm")        



