def valid_triangle(f):
    def inner(sides):
        a, b, c = sorted(sides)
        return a > 0 and a + b >= c and f(sides)

    return inner


@valid_triangle
def equilateral(sides):
    return len(set(sides)) == 1


@valid_triangle
def isosceles(sides):
    return len(set(sides)) < 3


@valid_triangle
def scalene(sides):
    return len(set(sides)) == 3
