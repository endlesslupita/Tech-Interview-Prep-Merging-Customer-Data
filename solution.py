def merge_data(customerData1, customerData2):
    position = -1
    
    while customerData2:
        position += 1
        if customerData1[position] > customerData2[0]:
            customerData1.insert(position,customerData2[0])
            customerData2.pop(0)

    return customerData1

if __name__ == '__main__':
    print(merge_data([101, 104, 107, 0, 0, 0],[102, 105, 108]))