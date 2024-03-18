# 1 
squares = [x ** 2 for x in range(1, 10)]
print(squares)

# 2 
def squares(start, end):
    return [i**2 for i in range(start, end+1)]

print(squares(1,10))