def quick_sort(arr):
    # time: O(nlogn) avg case, O(n^2) worst case
    # space: O(n)
    if len(arr) < 1:
        return arr
    
    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R

if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    print(quick_sort(elements))