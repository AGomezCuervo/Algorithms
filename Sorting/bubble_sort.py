"""Bubble Sort Algorithm"""

def bubble_sort (arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) -1 - i):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux

array = [2,5,6,7,16,1,2,4,8,9]

bubble_sort(array)

print(array)