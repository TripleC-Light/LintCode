"""
Implement a Rectangle class which include the following attributes and methods:

Two public attributes width and height.
A constructor which expects two parameters width and height of type int.
A method getArea which would calculate the size of the rectangle and return.

Example1:
Python:
    rec = Rectangle(3, 4)
    rec.getArea()

Example2:
Python:
    rec = Rectangle(4, 4)
    rec.getArea()
"""
class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    # write your code here
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    # write your code here
    def getArea(self):
        return self.width * self.height

if __name__ == '__main__':
    
    A = Rectangle(3, 4)
    print(A.getArea())
    
