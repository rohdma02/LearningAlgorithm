"""Start with the full list.
Calculate the middle index of the list.
Check the item at the middle index against
the target item you are searching for.
If it matches, return the middle index.
If the target is less than the middle item,
then search the left half of the list.
If the target is greater than the middle item,
search the right half.
Calculate the middle index of the new half and repeat steps 3-6.
Repeat this process of dividing the search
interval in half until you either
find the item, or the search interval is empty.
If the search interval is empty,
return None to indicate the item is not found.
"""


def binary_search(lista, item):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lista[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(binary_search(my_list, 3))
