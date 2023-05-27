# Python type(object) is a built-in function that returns the type of the objects

# class range
r = range(0, 30)
print(type(r))

# class int
print(type(10))

# class float
print(type(1.0))

# class str
print(type('Hi there'))

# class list
print(type([1, 2, 3, 4, 5]))

# and so on ...


# isinstance(object, type) - This function returns True if the specified object is of the specified type, otherwise False.
class Car:
    pass

class Track(Car):
    pass

car = Car()
track = Track()

print(type(car))
print(type(track))

# == not account for inheritance
print(type(car) == type(track))

# isinstance accounts for inheritance
print(isinstance(car, Car))
print(isinstance(track, Car))

# example
if isinstance(r, range):
    print(list(r))