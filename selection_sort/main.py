# Finds the smallest value in an array
def findSmallest(arr):
    # Stores the smallest value
    smallest = arr[0]
    # Stores the index of the smallest value
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index

# Sort array


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # Finds the smallest element in the array and adds it to the new array
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


# Example test 1
print("Test case 1")
print(selectionSort([5, 3, 6, 2, 10]))

# Example test 2
print("Test case 2")
print(selectionSort([12, 3, 36, 2, 85, 6, 2, 7, 10, 11, 69, 24, 36]))
