import math

def convertPolarCart(x, y):
    r = math.sqrt(x*x + y*y)
    theta = math.atan2(y, x)

    rounded_r = format(r, ".2f")
    rounded_theta = format(theta, ".2f")

    print(rounded_r, rounded_theta)

x, y = map(float, input().split())

convertPolarCart(x, y)
