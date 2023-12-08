# a list is iterable but its not an iterator

# An iterable is something that can be looped over eg a list is iterable
# Other iterables include lists, tuples, files, strings, dictonaries, generators etc

arr = [40, 25, 45, 63]

for element in arr:
    # print(element)
    pass

"""
How to tell if something is iterable?
If something is iterable it must have a special method called __iter__() ->magic method
The for loop calls the __iter__ method in the background and it returns an iterator that we can loop over
"""

# Checking if a list has an __iter__ method
# print(dir(list))


""" 
What makes something an iterator?
An iterator is an object with a state so that it remembers where it is during iteration.
Iterators also knows how to get their next value, they get there next value with a dunder __next__ method
so if you look at the list methods , you will notice that it doesnt have the __next__() method.
A list doesnt have a state and it doesnt have a __next__() value therefore it isnt an iterator
iterators only go forward
"""
list_iter = iter(arr)
# print(list_iter)
# print(dir(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))

print("------------------------------")

# How the for loop is structured
while True:
    try:
        item = next(list_iter)
        print(item)
    except StopIteration:
        break


class My_Range_Function:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        # To make this class iterable we need to add the __iter__() method
        # The iter method has to return an iterator, an object that has a dunder next method
        # We can create a dunder next method within this class itself and if we do that then we can return this same object
        # from our iter method
        return self

    def __next__(self):
        if (self.value >= self.end):
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = My_Range_Function(1, 10)

for num in nums:
    print(num)


# Creating A Generetor Function

def my_range(start, end):
    current = start

    while current < end:
        yield current
        current += 1


my_nums = my_range(20, 50)
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
