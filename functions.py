# TODO: Implement the following functions based on the descriptions.

def reverse_list():
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    lst = [1,2,3,4]
    lst.reverse()
    print(lst)
reverse_list()
        
def count_occurrences(lst):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    lst=[]
    lst = lst.count(6)
    print(lst)

lst=[1,2,3,4,5,6,6]
count_occurrences(lst)

    

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    pass  # Implement this

def merge_sorted_lists():
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    lst1 = [1,2,3,4]
    lst2 = [5,6,7,8]
    newlst = lst1 + lst2
    print(newlst)
merge_sorted_lists()

 

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    pass  # Implement this


def is_anagram():
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    str1 = 'gum'
    str2= 'mug'
    for letters in str1 and str2:
        if letters in str1 == letters in str2:
            print("True")
        else:
            print("False")
is_anagram()





def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
pass  # Implement this


def remove_duplicates():
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    a = [1, 2, 2, 3, 4, 4, 5]
    lst= []
    [lst.append(val) for val in a if val not in lst]
    print(lst)
remove_duplicates()

def find_common_elements(lst1,lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    lst1 = set(lst1)
    lst2 = set(lst2)
 
    if (lst1 & lst2):
        print(lst1 & lst2)
    else:
        print("No common elements") 

lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 6, 7, 8, 9]
        
find_common_elements(lst1,lst2)
          
