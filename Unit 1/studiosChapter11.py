class Rectangle:
    def __init__(self,length,width):
        self.L = length
        self.W = width
    def area(self):
        area = self.L * self.W
        return (area)
    def isSquare(self):
        if self.L == self.W:
            return True
        else:
            return False

def main():
    Squareish = Rectangle(200,20)
    print("The area of Squareish is",Squareish.area())
    print("Squareish Length:",Squareish.L, "Squareish Width:", Squareish.W)
    if Squareish.isSquare() == True:
        print("Squareish is a Square")
    else:
        print("Squareish is not a Square")

if __name__ == '__main__':
    main()
