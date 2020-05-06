def find_smallest_int(arr):
    check = arr[0]
    for x in arr:
        if x < check:
            check = x
    print(check)

find_smallest_int([34, 15, 88, 2])
find_smallest_int([34, -345, -1, 100])
