x = input("Enter x: ")
slope_m1 = 2 * float(x) - 2
print("Slope of x-intercept and y-intercept = 2x-2 : ", slope_m1)

x1, y1 = 2, 2
print("point 1 (x1,y1): ", x1, y1)

x2, y2 = 6, 10
print("point 2 (x2,y2): ", x2, y2)

slope_m2 = (float(y2) - float(y1)) / (float(x2) - float(x1))
print("Slope of the line: ", slope_m2)
euclidian_distance = ((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)
print("Euclidean distance: ", euclidian_distance)

if slope_m1 == slope_m2:
    print("The slopes are equal")
elif slope_m1 > slope_m2:
    print("Slope of x-intercept and y-intercept is greater than the slope of the line")
else:
    print("Slope of point (2,2) and point (6,10) is less than the slope of the line")

print("y =x^2 + 6x + 9")
x_find = input("Enter x to make y = 0 , x =")
y = (float(x_find) ** 2) + (6 * float(x_find)) + 9
while y != 0:
    print("y = ", y)
    x_find = input("Enter x to make y = 0")
    y = (float(x_find) ** 2) + (6 * float(x_find)) + 9
    
print("y = ", y)
    
word1 = "python"
word2 = "dragon"
print("word1: ", len(word1))
print("word2: ", len(word2))
print(word1 > word2)

if "on" in word1 and "on" in word2:
    print("on is in both word1 and word2")

sentence = "I hope this course is not full of jargon"
if "jargon" in sentence:
    print("jargon is in the sentence")

check_no_on = "on" not in word1 and "on" not in word2
print("Is 'on' NOT found in both 'python' and 'dragon'? ->", check_no_on)

