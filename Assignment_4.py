# Different Set Operations
A={}
n=int(input("Enter size of set A.\n"))
if n==0:
   print("Enter a valid size.")
else:
   A=set(map(int,input("Enter list of numbers separated by a ' , '.\n").split(",")))
B={}
m=int(input("Enter size of set B.\n"))
if m==0:
   print("Enter a valid size.")
else:
   B=set(map(int,input("Enter list of numbers separated by a ' , '.\n").split(",")))
print("Union of A and B is ",A|B)
print("Intersection of A and B is ",A&B)
print("Difference of A and B is ",A-B)
print("Symmetric difference of A and B is ",A^B)