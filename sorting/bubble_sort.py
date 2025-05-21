"""
Your algorithms comparisons all happen inside your inner loop where we do comparisons and swaps in the reverse order. 
Your outer loop is there only to keep your algorithm running for as many swaps as it takes to put your list in order.
"""


def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
        if not swapped:
            break


def bubble_sort_recursive(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                flag = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 64, 34, 88, 34]
    bubble_sort(elements)
    print(elements)

    elements = [5, 9, 2, 1, 64, 34, 88, 34]
    bubble_sort_recursive(elements)
    print(elements)