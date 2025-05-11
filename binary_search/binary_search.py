import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000} ms")
        return result
    return wrapper


@time_it
def linear_search(numbers_list, number_to_find):
    # O(n)
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            print(f"number found at index {index} using linear search")
            return index

    print(f"number found at index {index} using linear search")
    return -1


@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    print(f"number found at index {index} using binary search")
    return -1



def binary_search_recursive(number_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    
    return binary_search_recursive(number_list, number_to_find, left_index, right_index)


if __name__ == "__main__":
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 24

    numbers_list = [i for i in range(1000001)]
    number_to_find = 1000000

    index = linear_search(numbers_list, number_to_find)

    index = binary_search(numbers_list, number_to_find)

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))