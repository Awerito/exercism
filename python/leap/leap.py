def leap_year(year):
    
    A = year % 4 == 0
    B = year % 100 == 0
    C = year % 400 == 0

    return A and (not B or (B and C))
