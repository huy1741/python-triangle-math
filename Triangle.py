import math
coord_input = input("Enter coordinates [Ax,Ay,Bx,By,Cx,Cy]: ")
xA, yA, xB, yB, xC, yC = map(int, coord_input.split(','))

def distance(xA, yA, xB, yB):
    return round(math.sqrt((xB - xA)**2 + (yB - yA)**2), 2)

AB = distance(xA, yA, xB, yB)
BC = distance(xB, yB, xC, yC)
AC = distance(xA, yA, xC, yC)

def check_triangle(AB, BC, AC):
    # Check the triangle inequality
    if AB + BC > AC and AB + AC > BC and BC + AC > AB:
        return 'A, B, C form a triangle'
    else:
        return 'A, B, C do not form a triangle'

def angles(xA, yA, xB, yB, xC, yC):
    # Calculate the lengths of the sides of triangle ABC
    a = distance(xB, yB, xC, yC)
    b = distance(xA, yA, xC, yC)
    c = distance(xA, yA, xB, yB)

    # Calculate cos(A), cos(B), cos(C)
    cosA = (b**2 + c**2 - a**2) / (2 * b * c)
    cosB = (c**2 + a**2 - b**2) / (2 * c * a)
    cosC = (a**2 + b**2 - c**2) / (2 * a * b)

    # Calculate the angles in degrees
    degA = math.degrees(math.acos(cosA))
    degB = math.degrees(math.acos(cosB))
    degC = math.degrees(math.acos(cosC))

    print('Angle BAC: ' + str(round(degA, 2)))
    print('Angle ABC: ' + str(round(degB, 2)))
    print('Angle BCA: ' + str(round(degC, 2)))

def classify_triangle(xA, yA, xB, yB, xC, yC):
    # Calculate the lengths of the sides of triangle ABC
    a = distance(xB, yB, xC, yC)
    b = distance(xA, yA, xC, yC)
    c = distance(xA, yA, xB, yB)
    
    # Check if the triangle is equilateral
    if a == b and b == c:
        return "Equilateral triangle"

    # Check if the triangle is right-angled
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        if a**2 == b**2 + c**2:
            return "Right triangle at vertex A"
        elif b**2 == a**2 + c**2:
            return "Right triangle at vertex B"
        else:
            return "Right triangle at vertex C"

    # Check if the triangle is isosceles
    if a == b or b == c or c == a:
        if a == b:
            return "Isosceles triangle at vertex C"
        elif b == c:
            return "Isosceles triangle at vertex A"
        else:
            return "Isosceles triangle at vertex B"

    # Check if the triangle is acute-angled
    if a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
        if a == b or b == c or c == a:
            if a == b:
                return "Acute-angled triangle at vertex C"
            elif b == c:
                return "Acute-angled triangle at vertex A"
            else:
                return "Acute-angled triangle at vertex B"

    # Check if the triangle is obtuse-angled
    if a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
        if a**2 > b**2 + c**2:
            return "Obtuse-angled triangle at angle A"
        elif b**2 > a**2 + c**2:
            return "Obtuse-angled triangle at angle B"
        else:
            return "Obtuse-angled triangle at angle C"

    # If it doesn't fit any of the above cases, it's a scalene triangle
    return "Scalene triangle"

def area_triangle(xA, yA, xB, yB, xC, yC):
    # Calculate the area of triangle ABC
    S = abs((xA * (yB - yC) + xB * (yC - yA) + xC * (yA - yB)) / 2)

    # Round to 2 decimal places and return
    return round(S, 2)

def altitudes_triangle(xA, yA, xB, yB, xC, yC):
    # Calculate the area of triangle ABC
    S = area_triangle(xA, yA, xB, yB, xC, yC)
    
    # Calculate the lengths of the sides
    AB = distance(xA, yA, xB, yB)
    AC = distance(xA, yA, xC, yC)
    BC = distance(xB, yB, xC, yC)
    
    # Calculate the lengths of the altitudes
    hA = (2 * S) / BC
    hB = (2 * S) / AC
    hC = (2 * S) / AB
    
    # Round to 2 decimal places
    hA = round(hA, 2)
    hB = round(hB, 2)
    hC = round(hC, 2)
    
    # Print the results
    print("Length of altitude from point A =", hA)
    print("Length of altitude from point B =", hB)
    print("Length of altitude from point C =", hC)  

def medians_triangle(xA, yA, xB, yB, xC, yC):
    # Calculate the lengths of the sides
    a = distance(xB, yB, xC, yC)
    b = distance(xC, yC, xA, yA)
    c = distance(xA, yA, xB, yB)
    
    # Calculate the lengths of the medians
    tA = 0.5 * a
    tB = 0.5 * b
    tC = 0.5 * c
    
    return (round(tA, 2), round(tB, 2), round(tC, 2))

def centroid_triangle(xA, yA, xB, yB, xC, yC):
    x_centroid = (xA + xB + xC) / 3
    y_centroid = (yA + yB + yC) / 3
    return "x = {}; y = {}".format(x_centroid, y_centroid)

def circumcenter_triangle(xA, yA, xB, yB, xC, yC):
    x_circumcenter = (xA + xB + xC) / 3
    y_circumcenter = (yA + yB + yC) / 3
    return "x = {}; y = {}".format(x_circumcenter, y_circumcenter)

def main():
    print('Length of side AB', AB, 'cm')
    print('Length of side BC', BC, 'cm')
    print('Length of side AC', AC, 'cm')
    print(check_triangle(AB, BC, AC))
    print(angles(xA, yA, xB, yB, xC, yC))
    print(classify_triangle(xA, yA, xB, yB, xC, yC))
    print('Area of triangle: ' + str(area_triangle(xA, yA, xB, yB, xC, yC)))
    altitudes_triangle(xA, yA, xB, yB, xC, yC)
    print("Length of median from point A = " + str(list(medians_triangle(xA, yA, xB, yB, xC, yC))[0]))
    print("Length of median from point B = " + str(list(medians_triangle(xA, yA, xB, yB, xC, yC))[1]))
    print("Length of median from point C = " + str(list(medians_triangle(xA, yA, xB, yB, xC, yC))[2]))
    print(centroid_triangle(xA, yA, xB, yB, xC, yC))
    print(circumcenter_triangle(xA, yA, xB, yB, xC, yC))

if __name__ == '__main':
    main()
