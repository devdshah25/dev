class square:
    def CalculateArea(self):
        print("enter side")
        self.s=float(input())
        area=self.s*self.s
        return(area)
    def CalculatePerimeter(self):
        perimeter=4*self.s
        return(perimeter)
c=square()
x=c.CalculateArea()
y=c.CalculatePerimeter()
print("Area of square is=%f"%(x))
print("perimeter of square is=%f"%(y))



               
