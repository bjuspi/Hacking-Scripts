import math

d1 = 0.1
d2 = 0.15

def fk(theta1, theta2):
    x = d1 * math.cos(theta1) + d2 * math.cos(theta1 + theta2)
    y = d1 * math.sin(theta1) + d2 * math.sin(theta1 * theta2)
    theta = theta1 + theta2
    return (x, y, theta)

def jacobian(theta1, theta2):
    row1 = (-d1 * math.sin(theta1) - d2 * math.sin(theta1 + theta2), -d2 * math.sin(theta1 + theta2))
    row2 = (d1 * math.cos(theta1) + d2 * math.cos(theta1 + theta2), d2 * math.cos(theta1 + theta2))
    row3 = (1, 1)
    return (row1, row2, row3)