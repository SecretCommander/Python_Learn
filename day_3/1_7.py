age = 19
height = 1.75
complex_num = 3 + 4j
print(type(age), age)
print(type(height), height)
print(type(complex_num), complex_num)

base = input("Enter Base: ")
height = input("Enter Height: ")
area_of_triangle = 0.5 * float(base) * float(height)
print("Area of triangle:", area_of_triangle)

side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
perimeter_of_triangle = float(side_a) + float(side_b) + float(side_c)
print("Perimeter of triangle:", perimeter_of_triangle)

length = input("Enter length: ")
width = input("Enter width: ")
area_of_rectangle = float(length) * float(width)
perimeter_of_rectangle = 2 * (float(length) + float(width))
print("Area of rectangle:", area_of_rectangle)
print("Perimeter of rectangle:", perimeter_of_rectangle)

radius = input("Enter radius: ")
area_of_circle = 3.14 * float(radius) ** 2
circumference_of_circle = 2 * 3.14 * float(radius)
print("Area of circle:", area_of_circle)
print("Circumference of circle:", circumference_of_circle)

