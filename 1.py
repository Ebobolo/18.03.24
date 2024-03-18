def shell_sort(arr):
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

arr = [5, 3, 8, 4, 6]
shell_sort(arr)
print(arr)  #[3, 4, 5, 6, 8]