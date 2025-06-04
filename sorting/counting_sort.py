# Time: O(n + k) where k is the range of data
# Note - this example does not account for negative arrays
# so k is the max of the array.
# Space: O(k)

def counting_sort(arr) -> None:
    n = len(arr)
    maxx = max(arr)
    counts = [0] * (maxx + 1)

    for x in arr:
        counts[x] += 1
    
    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1


if __name__ == "__main__":
    F = [5, 3, 2, 1, 3, 3, 7, 2, 2]
    print(F)
    counting_sort(F)
    print(F)