class rectangle:
    def __init__(self,length,breadth) :
        self.length = length
        self.breadth = breadth
    def area(self) :
        return self.length * self.breadth
    def perimeter(self) :
        return 2 * (self.lenght + self.breadth)
    def display(self) :
        print(f"area of rectangle: {self.perimeter()}")
        print(f"perimeter of rectangle:{self.perimeter()}")
    def compare_area(self,other) :
        if self.area() == other.area():
            print("/n rectangles are equal in area")
        elif self.area() >  other.area() :
            print("/n rectangles 1 is greater in area than rectangle 2")
        else:
            print("/n rectangle 2 is greater in area than rectangle 1")
print("enter dimension of the first rectanle:")
length1 = int(input("enter the length1:"))
breadth1 = int(input("enter the breadth"))
rect1 = rectangle(length1,breadth1)
rect1.display()
print("/n enter the dimension of the second rectangle")
lenght2 = int(input("enter lenght1"))
breadth2 = int(input("enter breadth1"))
rect2 = rectangle(lenght2,breadth2)
rect2.display()
rect1.compare_area(rect2)


