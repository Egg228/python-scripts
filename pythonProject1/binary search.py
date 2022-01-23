



def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


my_list = [3,4,9,8,9,5,15,40,21]
my_list.sort()
print(my_list)

print(binary_search(my_list, 8))