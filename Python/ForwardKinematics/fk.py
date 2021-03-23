import math

d1 = 0.1
d2 = 0.15

def fk(theta1, theta2):
    x = d1 * math.cos(theta1) + d2 * math.cos(theta1 + theta2)
    y = d1 * math.sin(theta1) + d2 * math.sin(theta1 * theta2)
    theta = theta1 + theta2
    return (x, y, theta)