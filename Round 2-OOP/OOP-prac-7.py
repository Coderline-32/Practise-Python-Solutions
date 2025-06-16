import math
from abc import ABC, abstractmethod

# 1. Create an abstract base class Shape
# ABC (Abstract Base Class) is a helper class that provides a way to create
# ABCs by deriving from it. Alternatively, one can use metaclass=ABCMeta.
class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    It defines an interface for shapes that must have an area calculation.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Subclasses must implement this method.
        """
        pass # No implementation in the abstract class

    def description(self):
        """
        A concrete method that can be inherited by subclasses.
        """
        return "This is a generic shape."

# 2. Create a subclass Rectangle
class Rectangle(Shape):
    """
    A concrete subclass of Shape representing a rectangle.
    It must implement the abstract 'area' method.
    """
    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Width must be a positive number.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number.")
        self.width = width
        self.height = height
        print(f"Rectangle created: Width={self.width}, Height={self.height}")

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Additional method specific to Rectangle.
        """
        return 2 * (self.width + self.height)

# 3. Create a subclass Circle
class Circle(Shape):
    """
    A concrete subclass of Shape representing a circle.
    It must implement the abstract 'area' method.
    """
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius
        print(f"Circle created: Radius={self.radius}")

    def area(self):
        """
        Calculates the area of the circle using the formula pi * r^2.
        """
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """
        Additional method specific to Circle.
        """
        return 2 * math.pi * self.radius

# --- Demonstration ---

print("--- Attempting to instantiate the abstract base class Shape ---")
try:
    # 4. Ensure base class cannot be instantiated
    generic_shape = Shape()
    print(f"Instantiated generic shape: {generic_shape.description()}")
except TypeError as e:
    print(f"Error: {e}")
    print("As expected, cannot instantiate abstract class 'Shape' directly.")

print("\n--- Instantiating and using concrete subclasses ---")

# Create a Rectangle object
rectangle = Rectangle(width=10, height=5)
print(f"Rectangle area: {rectangle.area():.2f}")
print(f"Rectangle perimeter: {rectangle.perimeter():.2f}")
print(f"Rectangle description: {rectangle.description()}")

print("\n---")

# Create a Circle object
circle = Circle(radius=7)
print(f"Circle area: {circle.area():.2f}")
print(f"Circle circumference: {circle.circumference():.2f}")
print(f"Circle description: {circle.description()}")

print("\n--- Demonstrate type checking ---")
print(f"Is rectangle an instance of Shape? {isinstance(rectangle, Shape)}")
print(f"Is circle an instance of Shape? {isinstance(circle, Shape)}")
print(f"Is Circle a subclass of Shape? {issubclass(Circle, Shape)}")
