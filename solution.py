def merge_data(customerData1, customerData2):

    position = 0
    list_length = len(customerData1)
    list_length -= 1
    while customerData2 and position <= list_length:
        if customerData1[position] < customerData2[0]:
            position += 1
        else:
            customerData1[position] = customerData2[0]
            customerData2.pop(0)
            position += 1
    position -= 1
    while customerData2:
            customerData1[position] = customerData2[0]
            customerData2.pop(0)
            position += 1
    return customerData1

if __name__ == '__main__':
    print(merge_data([101, 104, 107, 0, 0, 0],[102, 105, 108]))