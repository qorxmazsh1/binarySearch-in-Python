# BINARY SEARCH
n = int(input("axtarilan ededi daxil et: "))
list1 = [4, 5, 7, 34, 23, 67, 87, 53, 23]

def binary_search(n, list1):
    list1.sort()
    left = 0
    right = len(list1) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if list1[mid] == n:
            return mid 
        elif list1[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
print("siralanmiş siyahi:", list1)
index = binary_search(n, list1)
if index != -1:
    print(f"axtarilan eded: {n}\nindeks: {index}")
else:
    print(f"axtarilan eded siyahida yoxdur.")