class SquareGenerator:
    def generate_squares(self, start, end):
        """Generate a list of squares for a given range of numbers."""
        if end < start:
            raise ValueError("End of the range should be greater than or equal to start.")
        return [x**2 for x in range(start, end + 1)]
