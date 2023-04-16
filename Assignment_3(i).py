#Fibonacci series
n=int(input("Enter required number of terms of Fibonacci series.\n"))
a=0
b=1
i=1
print("The Fibonacci sequence is:\n")
if n==0:
   print("Enter a valid number.")
elif n==1:
     print(a,end=",...")
elif n==2:
     print(a,b,sep=",",end=',...')
elif n>2:
     print(a,b,sep=",",end=",")
     for i in range(0,n-2):
              c=a+b
              if i!=n-3:
                   print(c,end=",")
              else:
                   print(c,end=",...")
              a=b
              b=c
              i=i+1