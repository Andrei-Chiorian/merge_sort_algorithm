def merge_sort(array):
    """
    Sorts an array using the Merge Sort algorithm.

    It starts by splitting the array in half, sorting each half, and then merging the two halves back together.

    This algorithm is O(n log n)
    """
    if len(array) <= 1:
        return

    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively call merge sort on each half
    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merge the two halves
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # If the left half's element is smaller than the right half's, append the left half's element to the sorted array
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        # Else append the right half's element to the sorted array
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # If there are remaining elements in the left half, append them to the sorted array
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # If there are remaining elements in the right half, append them to the sorted array
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ' + str(numbers))
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))