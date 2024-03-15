#task1
squares = [x**2 for x in range(1, 11)]
print("List of squares of numbers from 1 to 10:")
print(squares)
#task2
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]
start = 1
end = 10
print("List of squares from {} to {}: ".format(start, end), generate_squares(start, end))
#task3
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end + 1)]
square_gen = SquareGenerator()
start = 1
end = 10
print("List of squares from {} to {}: ".format(start, end), square_gen.generate_squares(start, end))
#task4
import math
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end + 1)]
    def calculate_square_roots(self, squares):
        return [math.sqrt(num) for num in squares]
square_gen = SquareGenerator()
start = 1
end = 10
squares = square_gen.generate_squares(start, end)
print("List of squares from {} to {}: ".format(start, end), squares)
print("Square roots of the numbers:", square_gen.calculate_square_roots(squares))
#task5
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range should be greater than or equal to start.")
        return [x**2 for x in range(start, end + 1)]

    def calculate_square_roots(self, squares):
        return [math.sqrt(num) for num in squares]

square_gen = SquareGenerator()
start = 10
end = 1
try:
    squares = square_gen.generate_squares(start, end)
    print("List of squares from {} to {}: ".format(start, end), squares)
except ValueError as ve:
    print("Error:", ve)
#task6
