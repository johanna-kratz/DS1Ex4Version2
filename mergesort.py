import matplotlib.pyplot as plt 



def merge_sort(list_to_sort_by_merge): 
    if len(list_to_sort_by_merge) == 1:  # this is shorter and better readable than having a long if statement for case >1
        return list_to_sort_by_merge # base case
        
    sorted_list=[]
    mid = len(list_to_sort_by_merge) // 2
    left = list_to_sort_by_merge[:mid]
    right = list_to_sort_by_merge[mid:]

    sorted_left= merge_sort(left)
    sorted_right= merge_sort(right)

    left_position = 0
    right_position = 0

    # Merge the sorted halves back into the original array
    while left_position < len(sorted_left) and right_position < len(sorted_right):
        if sorted_left[left_position] <= sorted_right[right_position]:
            sorted_list.append(sorted_left[left_position])
            left_position += 1
        else:
            sorted_list.append(sorted_right[right_position])
            right_position += 1

    # add remaing numbers from left half
    while left_position < len(sorted_left):
        sorted_list.append(sorted_left[left_position])
        left_position += 1

    # add remaining numbers from right half
    while right_position < len(sorted_right):
        sorted_list.append(sorted_right[right_position])
        right_position += 1

    return sorted_list


if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.show()
    my_sorted_list= merge_sort(my_list)
    x = range(len(my_sorted_list))
    plt.plot(x, my_sorted_list)
    plt.show()
