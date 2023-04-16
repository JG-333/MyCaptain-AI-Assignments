# To print positive numbers in a list
list1=[]
pos_list=[]
n=int(input("Enter size of list.\n"))
if n==0:
   print("Enter a valid size.")
else:
   list1=list(map(int,input("Enter list of numbers separated by a ' , '.\n").split(",")))
   i=0
   for i in list1:
            if i>=0:
               pos_list.append(i)
            i=i+1
   if len(pos_list)!=0:   
      print("Positive numbers in the list are",pos_list)
   else:
      print("The list does not contain any positive numbers.")
