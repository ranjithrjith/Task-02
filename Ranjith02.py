class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Calculate the area using the formula A = πr^2
        return 3.14159 * self.radius ** 2

# Example usage:
circle = Circle(5)
print("The area of the circle is:", circle.area())