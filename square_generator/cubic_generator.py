from square_generator.square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end < start:
            raise ValueError("End of the range should be greater than or equal to start.")
        return [x**3 for x in range(start, end + 1)]

    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range should be greater than or equal to start.")
        return super().generate_squares(start, end)
