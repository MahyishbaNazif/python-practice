#Find min and max from array
def find(arr):
    minn ,maxx = arr[0], arr[0]
    for num in arr[1:]:
        if num < minn:
            minn = num
        elif num > maxx:
            maxx = num
    return minn, maxx
arr = [4, 7, 40, 4, 3, 1, 16, 90, 22, 8]
minn, maxx = find(arr)
print(minn, maxx)
#Time complexity O(n)
            