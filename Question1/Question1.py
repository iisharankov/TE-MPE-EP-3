import itertools
from collections import Counter


"""
Since collections is part of the standard library, this function uses Counter to count
each letters' frequency and a simple comprehension list to isolate those with more than
one occurrence. Personally the below fit within the description and is quite pythonic.
"""
def find_duplicates(letters):
    """
    Finds all duplicate letters within input list

    :param letters: list of strings
        - single letter strings expected but not required
    :return: list of strings
        - all repeated items in input list
    """

    counts = Counter(letters)
    return [letter for letter, count in counts.items() if count > 1]


"""
Just in case, here's a solution without any library. I use sets instead of lists since 
they're O(1) when using the `in` keyword to check what's in a set; same for appending.
I assume it's alright the resulting list is not in order, since sets are unordered
"""
def find_duplicates_with_no_libraries(letters):
    """
    A libraryless solution to find all duplicate letters in a list of letters.

    :param letters: list of strings
        - single letter strings expected but not required
    :return: list of strings
        - all repeated items in input list
    """
    seen = set()
    duplicates = set()

    for letter in letters:
        duplicates.add(letter) if letter in seen else seen.add(letter)

    return list(duplicates)


if __name__ == "__main__":

    list1 = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]
    list2 = ["a", "b", "c"]
    list3 = ["a", "b", "c", "d", "a", "b", "c", "d", "e'"]

    print(find_duplicates(list1))
    print(find_duplicates_with_no_libraries(list1))

    print(find_duplicates(list2))
    print(find_duplicates_with_no_libraries(list2))

    print(find_duplicates(list3))
    print(find_duplicates_with_no_libraries(list3))
