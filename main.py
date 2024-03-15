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
