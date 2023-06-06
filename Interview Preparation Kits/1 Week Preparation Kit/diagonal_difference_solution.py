def diagonalDifference(arr):
    left_to_right_index_1 = 0
    left_to_right_index_2 = 0
    left_sum = 0

    length_of_arr = len(arr)
    right_to_left_index_1 = 0
    right_to_left_index_2 = length_of_arr - 1
    right_sum = 0

    # print(len(a))

    # Left Sum
    for i in range(0, len(arr)):
        left_sum += arr[left_to_right_index_1][left_to_right_index_2]

        left_to_right_index_1 += 1
        left_to_right_index_2 += 1

    #print(left_sum)

     # Right Sum
    for i2 in range(0, len(arr)):
        if right_to_left_index_2 >= 0 and right_to_left_index_1 >= 0:
            right_sum += arr[right_to_left_index_1][right_to_left_index_2]
            right_to_left_index_1 += 1
            right_to_left_index_2 -= 1

    #print(right_sum)
    
    absolute_difference = abs(left_sum - right_sum)
    return absolute_difference

#diagonalDifference([[],[]])
