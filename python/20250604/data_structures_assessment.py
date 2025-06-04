
"""All assignment related to lists."""
# Write a function to check if an input is a palindrome (same forwards and backwards, like MALAYALAM). The function should work for any input including strings and numbers.

def is_palindrome(input_value):
    str_input = str(input_value)
    return str_input == str_input[::-1]

print(is_palindrome("MALAYALAM"))
print(is_palindrome(1231))

# Write a function to insert items into a list at a given index.

def insert_at_index(data_list, index, item):
    data_list.insert(index, item)
    return data_list
print(insert_at_index([1, 2, 3, 4], 2, 'a'))

#Give two lists, a and b, write code to show the difference in insert(), append(), and extend().
def list_operations_demo(a, b):
    # Using append
    a.append(100)
    print("After append:", a)

    # Using insert
    a.insert(0, 50)
    print("After insert at index 0:", a)

    # Using extend
    a.extend(b)
    print("After extend with b:", a)
    
    print("List a after all operations:", a)
list_operations_demo([1, 2, 3], [4, 5, 6])

# Count the occurrence of each unique element from a list with 72,165 items.
def count_occurrences(big_list):
    
    unique_elements = set(big_list)
    count_dict = {}
    for item in unique_elements:
        count = 0
        for element in big_list:
            if element == item:
                count += 1
        count_dict[item] = count
    return count_dict
print(count_occurrences([1, 2, 2, 3, 4, 4, 5]))

# Remove duplicate items from a given list of items.
def remove_duplicates(data_list):
    return list(set(data_list))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
# Write a function prime_numbers(n) that prints all prime numbers between, and including, 1 and n.
# Example:
# - prime_numbers(31) will return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# - prime_numbers(32) will return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def prime_numbers(n):
    primes = []
    for num in range(1, n + 1):
        if num == 1:
            primes.append(1)
        elif num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
print(prime_numbers(31))

# Write a Python code snippet to remove the last element from a list.
def remove_last_element(data_list):
    if data_list:
        return data_list[:-1] # another way is data_list.pop()
    return data_list
print(remove_last_element([1, 2, 3, 4, 5]))

#How can you check if a certain element exists in a list?
def element_exists(data_list, element):
    return element in data_list
print(element_exists([1, 2, 3, 4, 5], 3))

#Write a Python function to find the maximum element in a list. (without using max())
def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([1, 2, 3, 4, 5]))

#Given a list of integers, write a Python function to remove all occurrences of a specific integer from the list.
def remove_occurrences(lst, target):
    return [x for x in lst if x != target]
print(remove_occurrences([1, 2, 3, 4, 2, 5], 2))


"""All assignment related to dictionaries."""
# Write a Python function to merge two dictionaries.
def merge_dicts(d1, d2):
    merged = d1.copy()  # Start with a copy of d1
    for key in d2:
        merged[key] = d2[key]  # Add/overwrite with d2's items
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

# Given a dictionary of items and their prices, write a Python function to find the most expensive item.
def most_expensive_item(price_dict):
    def get_price(item):
        return item[1]
    return max(price_dict.items(), key=get_price)
print(most_expensive_item({'apple': 15, 'banana': 50, 'cherry': 20}))

# Write a Python function that takes a dictionary as input and returns a new dictionary where the keys and values are swapped.
def swap_dict(d):
    return {v: k for k, v in d.items()}
print(swap_dict({'a': 1, 'b': 2, 'c': 3}))

# Write a Python function to remove all items with a specific value from a dictionary.
def remove_by_value(d, value):
    return {k: v for k, v in d.items() if v != value}
print(remove_by_value({'a': 1, 'b': 2, 'c': 1}, 1))

"""All assignment related to tuples."""

# Write a Python function that takes two tuples as input and returns a new tuple containing elements from both tuples.
def merge_tuples(t1, t2):
    return t1 + t2
print(merge_tuples((1, 2, 3), (4, 5, 6)))

# Given a tuple containing the heights of students, write a Python function to find the average height.
def average_height(heights):
    return sum(heights) / len(heights) if heights else 0
print(average_height((150, 160, 170, 180)))

# Given a tuple of numbers, write a Python function to find the index of the first occurrence of a specific number.
def find_index(t, number):
    return t.index(number) if number in t else -1
print(find_index((1, 2, 3, 4, 5), 3))

"""All assignment related to strings."""
# Given a sentence, write a Python function to capitalize the first letter of each word.
def capitalize_words(sentence):
    words = sentence.split()
    capitalized = [word[0].upper() + word[1:].lower() if word else '' for word in words]
    return ' '.join(capitalized)
print(capitalize_words("hello world! this is a test."))

# Given a string containing multiple words separated by spaces, write a Python function to reverse the order of words.
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
print(reverse_words("A quick brown fox jumps over the lazy dog"))

# Write a Python function to find the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ''
print(longest_word("A quick brown fox jumps over the lazy dog and jumps high again from mountain and dies"))