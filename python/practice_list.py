"""
This script generates a list of even numbers from 0 to 100"""

even_list = []

for i in range(0, 101, 2):
    even_list.append(i)

for index, num in enumerate(even_list, start=1):
    print(f"{index}: {num}")
