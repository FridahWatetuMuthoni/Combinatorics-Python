import itertools

""" 
COMBINATIONS
Defination:
For a set S, its K-combination is a subset of S of size k.
The number of k-combinations of a n element set is denoted by (n/k): pronounced
as "n choose k", n is the size and k is the length
"""

""" 
QUESTION ONE:
Number of games in a tournament:
Five teams played a tournament: each team played with each other. What was the 
number of games
"""
# combinations


def number_of_games():
    teams = ['team1', 'team2', 'team3', 'team4', 'team5']
    number_of_games = itertools.combinations(teams, 2)
    games = 0

    for element in number_of_games:
        games += 1

    return games


print(number_of_games())

""" 
QUESTION TWO:
Jounery:
You are organising a car jounery. You have five friends, but there are only three
vacant places in your car. What is the number of ways
of taking three of your five friends to the jounery
"""


def friends_combination():
    friends = ['person1', 'person2', 'person3', 'person4', 'person5']
    friends_result = itertools.combinations(friends, 3)
    number_of_friends_combinations = 0
    for friends in friends_result:
        number_of_friends_combinations += 1
    return number_of_friends_combinations


print(friends_combination())


def factorial(value):
    if (value == 0 or value == 1):
        return 1
    return value * factorial(value - 1)


""" 
QUESTION THREE:
What is the number of 5-card hands dealt off of a standand 52 card deck
"""
# using the combination formula
# combination = n! / (n-r)!r!
n = 52
r = 5
hands = factorial(n) // (factorial(n - r) * factorial(r))
print(f"###############-> {hands}")

hands_result = itertools.combinations(range(1, 53), 5)
hands_count = 0
for hand in hands_result:
    hands_count += 1
print(f"###############-> {hands_count}")

# The Pascal Triangle


def printing_the_pascal_triangle():
    n = 5
    for i in range(n):
        for j in range(n-i+1):
            # for left spacing
            print(end=' ')
        for j in range(i+1):
            # ncr_combinations = n! / ((n-r)!*r!)
            print(factorial(i) // (factorial(j) * factorial(i-j)), end=" ")
        # printing a new line
        print()


printing_the_pascal_triangle()

"""
Question Four:
What is the number of non-negative itegers with at most four digits at least
one of which is equal to 7 ?
"""


def four_number_digits_with_seven():
    count = 0
    all_four_digit_numbers = itertools.product(range(10), repeat=4)
    for number in all_four_digit_numbers:
        if 7 in number:
            count += 1
    print(count)
    return count


four_number_digits_with_seven()
