def exponentiate(x,y):
    """
    This function returns the value of x raised to the power of y
    """
    return x ** y

def raise_to_fourth_power(x):
    """
    This function returns the value of x raised to the fourth power
    """
    return exponentiate(x, 4)

square = lambda x: exponentiate(x, 2)

cube = lambda x: exponentiate(x, 3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))

