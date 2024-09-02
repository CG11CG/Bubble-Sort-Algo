A = [-3, -8, 1, 7, 3, 2, 10, 5]
def bubblesort(arr):
    n = len(arr)
    yes = True
    while yes:
        yes = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                yes = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

bubblesort(A)
print(A)