from signals.homework1 import sum_cubes
from signals.homework1 import task2

# test task 1
print "Sum cubes of numbers in [1..4] = %s" % sum_cubes(4)
print "Sum cubes of numbers in [1..10] = %s" % sum_cubes(10)
print "Sum cubes of numbers in [1..20] = %s" % sum_cubes(20)


# test task 2
values = [8, 5, 9, 3, 1]
middle, median = task2(values)
print "List of numbers = %s, middle value = %s, median = %s" % (values, middle, median)

values = [4, 5, 7, 2]
middle, median = task2(values)
print "List of numbers = %s, middle value = %s, median = %s" % (values, middle, median)
