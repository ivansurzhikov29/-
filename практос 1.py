#нахождение z
import math
x = float(input("введите переменную х"))
y = float(input("введите переменную y"))
z = ((9 * math.pi * y + 10 * math.cos(x))/(math.sqrt(y)- math.fabs(math.sin(y))))*math.pow(math.e,x)
print("z = {0:.3f}".format(z));
 
