#problem 01

import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

Mean_ = numpy.mean(speed)
Median_ = numpy.median(speed)
Standard_deviation = numpy.std(speed)

count = sum(1 for x in speed if x > Mean_)

normalize = (speed - Mean_) / Standard_deviation

print ("The element Mean_ : ")
print(Mean_)
print ("The element Median_ : ")
print(Median_)
print ("The element Standard_deviation : ")
print(Standard_deviation)
print ("The element minimum: ")
print(min(speed))
print ("The element maximum : ")
print(max(speed))
print ("The element count many values  : ")
print(count)
print ("The element  normalize: ")
print(normalize)