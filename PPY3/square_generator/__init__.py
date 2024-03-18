class SquareGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def squares(self):
        return [i**2 for i in range(self.start, self.end+1)]