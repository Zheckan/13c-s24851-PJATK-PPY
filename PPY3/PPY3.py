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

print(SquareGenerator(1,10).squares())