num=int(input("enter the numbers:"))
list=[i for i  in range(1,num+1) if num % 1 ==0]
print("factors of number=",list)
print("/n enter the length and breadth odf rectangle:")
l=int(input("length"))
b=int(input("breadth"))
c=lambda x,y : x*y
print("area of rectangle:",c(l,b))
print("/n enter the side of a square:")
s=int(input("side of square:"))
c=lambda x : x*x
print("area of square is:",c(s))