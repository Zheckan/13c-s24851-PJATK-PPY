import math
import square_generator as sq

# 1 
squares = [x ** 2 for x in range(1, 10)]
print(squares)

# 2 
def squares(start, end):
    return [i**2 for i in range(start, end+1)]

print(squares(1,10))

# 3
class SquareGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def squares(self):
        return [i**2 for i in range(self.start, self.end+1)]
squares = SquareGenerator(1,10).squares()
print(squares)

# 4
squares = [int(math.sqrt(square)) for square in squares]
print(squares)

# 5 
try: 
    squaresGenerator = SquareGenerator(10,1).squares()
    print(squaresGenerator)
except: 
    print("Some error occurred")

# 6 
squa = sq.SquareGenerator(1,10).squares()
print(squa)

# 8
class CubicGenerator(SquareGenerator):
    def __init__(self, start, end):
        super().__init__(start, end)
    
    def cubes(self):
        return [i**3 for i in range(self.start, self.end+1)]
    
print(CubicGenerator(1,10).cubes())
