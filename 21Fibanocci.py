n=int(input("Enter the number"))
a=0
b=1
print(a)
print(b)
fibi=1
for i in range(1,n):
  print(fibi)
  temp=b
  b=fibi
  fibi=temp+b