def insertion_sort(arr) -> None:
    # time: O(n^2)
    # space: O(1)
    n = len(arr)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

if __name__ == "__main__":
    B = [-5, 3, 2, 1, -3, 7, 2, 2]
    print(B)
    insertion_sort(B)
    print(B)
