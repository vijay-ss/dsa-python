
def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            print(i, j)
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    elements = [5, 9, 2, 1, 64, 34, 88, 34]

    bubble_sort(elements)
    print(elements)