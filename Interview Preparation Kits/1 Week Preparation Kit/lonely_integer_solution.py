def lonelyinteger(a):
    first_entry_of_numbers = []
    repeated_number_list = []
    index = 0
    index2 = 0

    for i in a:
        if a[index] not in first_entry_of_numbers:
            first_entry_of_numbers.append(a[index])
        else:
            repeated_number_list.append(a[index])
        index += 1

    # print(first_entry_of_numbers)
    # print(repeated_number_list)

    for i in range(0, len(first_entry_of_numbers)):
        if first_entry_of_numbers[index2] in repeated_number_list:
            pass
        else:
            unique_element = first_entry_of_numbers[index2]
            return unique_element
        index2 += 1
        
#lonelyinteger([])        
