import itertools
import operator

"""
Itertools module is a collection of tools that allows us to work with iterators in a fast and
memory efficient way.
Iterators is basically sequential data that we can loop over 
"""

# COUNT FUNCTION
# Returns an iterator that counts, it counts from 0 to infinity

counter = itertools.count()
print(next(counter))
print(next(counter))
print(next(counter))

# Example use of the count function
# pairing the data with an index value

data = [100, 200, 300, 400]

# The zip() function combines two intervals and pairs the values together.
# In this case it pairs the first value of the count function which is 0 and the first value of the data list
daily_data = list(zip(itertools.count(), data))
print(daily_data)

# We can also add the start and the step arguements to the counter function

counter_1 = itertools.count(start=5, step=5)
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))


counter_2 = itertools.count(start=5, step=2.5)
print(next(counter_2))
print(next(counter_2))
print(next(counter_2))


counter_3 = itertools.count(start=5, step=-1)
print(next(counter_3))
print(next(counter_3))
print(next(counter_3))


# ZIP_LONGEST FUNCTION

my_data = [466, 789, 741, 321, 587, 425]

comb_data = list(itertools.zip_longest(range(10), my_data))
print(comb_data)

# CYCLE FUNCTION
# The cycle function returns an iterator that goes on forever
# It takes an iterable as an arguement and will cycle thru those values over and over

# Examples

cycle_counter = itertools.cycle([1, 2, 3])
print(next(cycle_counter))
print(next(cycle_counter))
print(next(cycle_counter))
print(next(cycle_counter))
print(next(cycle_counter))
print(next(cycle_counter))

# REPEAT FUNCTION
# It takes an input and repeats it indefinitly

repeat_counter = itertools.repeat(2)
# repeat_counter = iterrools.repeat(2, times = 3)
print(next(repeat_counter))
print(next(repeat_counter))
print(next(repeat_counter))
print(next(repeat_counter))
print(next(repeat_counter))

# The map function takes in a function in this case the pow() function and then it takes in iterables and uses
# the values from those to pass as arguements to that function
# in this case the map function pass the arguements as follows pow(0,2); pow(1,2); pow(2,2); pow(3,2); pow(4,2)
squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))

# STAR_MAP
"""
star_map is very similar to the map function but instead of taking arguements from iterables like we are doing  here
it instead takes arguements that are already paired together as tuples. For example lets use starmap to get these few
powers, so instead of passing range and the repeat function, we are just gonna pass in a list and these are going to be
a list of tuples that have the arguements already paired together.
"""

squares = itertools.starmap(
    pow, [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2)])
print(list(squares))


# COMBINATIONS AND PERMUTATIONS

"""
The combination and permutation functions allow us to take an iterable and return all the combinations
and permutations from that iterable
The main difference between permutations and combinations is that in permutation order matters while
with combinations order does not matter
in permutation this two are two different things AB and BA
while in combinaton AB and BA are the same because its a combination of the same two letters
"""

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']


# Lets get all the possible combinations of two values from the above letters

# USING THE COMBINATIONS FORMULA
# C = n!/(n-r)! r!

n = len(letters)
r = 2


def factorial(value):
    if (value == 1 or value == 0):
        return 1
    return value * factorial(value - 1)


p_combinations = factorial(n) / (factorial(n-r) * factorial(r))
print(p_combinations)

# USING THE COMBINATION FUNCTION FROM THE ITERTOOLS MODULE
c_result = itertools.combinations(letters, 2)

for element in c_result:
    print(element)


# USING THE PERMUTATION FORMULA
# P = n!/(n-r)!

p_permutations = factorial(n) / factorial(n - r)

print(p_permutations)

# USING THE PERMUTATION FUNCTION FROM THE ITERTOOLS MODULE

p_result = itertools.permutations(letters, 2)
len = 0
for element in p_result:
    len += 1
    print(element)
print(len)

""" 
What you will notice is that permutations and combinations dont repeat values.
For example it doesnt give us something like aa or bb as one of the permutations
To allow repeats, for example if we wanted to see all the different ways that we can create a 4 digit passcode
we would not use combiations and permutations. for that we could use the product function
The product function will give you the cartesian product of iterables that you pass in. If  you only pass in one iterable then
we can tell it how many times we want it to be able to repeat those values
"""
product_result = itertools.product(numbers, repeat=4)
print(list(product_result))
for element in product_result:
    print(element)

""" 
We  can also repeat the above with the combinations_wth_replacement function
"""
replacement_result = itertools.combinations_with_replacement(numbers, 4)

for element in replacement_result:
    print(element)

""" 
THE CHAIN FUNCTION
The xhain function allows to chain together iterables so that it will go thru all the items in the first iterable
and after that has been exhausted it will go thru the second iterable and so on
"""

# Examples: looping over the items in this lists
# We could create a new list that combines all these three lists and loops for those

e_letters = ['a', 'b', 'c', 'd']
e_numbers = [0, 1, 2, 3]
e_names = ['Corey', 'Nicole']

combined = itertools.chain(e_letters, e_names, e_numbers)

for item in combined:
    print(item)

""" 
Now lets look at a function that will allow us to get a slice of an iterator
It basically like list slicing but in this case it performs slicing on an iterator
"""

# it gives us the first five items of the iterable
# 10 is the range of the iterable while 5 is the stoping iterable
islice_result_1 = itertools.islice(range(10), 5)
# 10 is the range of the iterable while 1 is the starting point and 5 is the stoping point
islice_result_2 = itertools.islice(range(10), 1, 5)
# 10 is the range of the iterable while 1 is the starting point and 5 is the stoping point and 2 is the step
islice_result_3 = itertools.islice(range(10), 1, 5, 2)


for element in islice_result_1:
    print(element)

# Example using a log file and isclice
# Grabing the first three lines from a log file using islice
# files are iterators btw

with open('test.log', 'r') as file:
    # this grabs the first three lines from the file
    header = itertools.islice(file, 3)

    for line in header:
        print(line, end="")

# The Compress Function
""" 
The compress function is a function that could be used in data science to solve probelms
Where you have some data and some selectors that you can use to filter down that data
Lets say that we have a list of true/false values and they are going to correspond to my
letters list here
"""
selectors_letters = ['a', 'b', 'c', 'd']
selectors = [True, True, False, True]
compress_result = itertools.compress(letters, selectors)
# C was not included because of the corresponding selector was false
for element in compress_result:
    print(element)


def values_less_than_2(n):
    if (n < 2):
        return True
    return False


filter_result = filter(values_less_than_2, numbers)
print(list(filter_result))

# FILTER_FALSE is a function that returns the values that returned false instead of true

filter_false_result = itertools.filterfalse(values_less_than_2, numbers)
print(list(filter_false_result))

# Functions that stop filtering once the function returns True

# dropwhile function -> This function will drop values from an iterable until one of the values returns true

nums = [0, 1, 2, 3, 2, 1, 0]
dropwhile_result = itertools.dropwhile(values_less_than_2, nums)
print(list(dropwhile_result))

# takewhile function -> This function will instead grab all the values that will return true, and when it hit a value
# that returns true it just stops and returns the rest


nums_2 = [0, 1, 2, 3, 2, 1, 0]
takewhile_result = itertools.takewhile(values_less_than_2, nums)
print(list(takewhile_result))

# Accumulate Function-> the function takes a iterable and returns the accumulated sums of each item that it sees
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accumulate_result = itertools.accumulate(my_list)
print(list(accumulate_result))

# Performing multiplication instead of addition using the accumulate function

# operator.mul is the multiplication sign
mult_result = itertools.accumulate(my_list, operator.mul)
print(list(mult_result))

# The groupby Function
""" 
This function will go thru an iterable and group values based on a certain key and
then it will return a stream of tuples
The tuples consist of the key that the items were grouped on and the second value of the tuple
is an iterator that contain all of the items that were grouped by that key
"""

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Anna Hathway',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    },
]

# The function that will group people by state


def get_state(person):
    return person['state']


person_group = itertools.groupby(people, get_state)

for key, group in person_group:
    print(key)
    for person in group:
        print(person)
    print()

# Printing the number of people instead of the people themselves

for key, group in person_group:
    print(key, len(list(group)))
