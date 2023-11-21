import math

def PolarToCartisian (r, theta):

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    rounded_x = format(x, ".2f")
    rounded_y = format(y, ".2f")

    print(rounded_x, rounded_y)

r, theta = map(float, input().split())
PolarToCartisian(r, theta)