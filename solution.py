def merge_data(customerData1, customerData2):
    position = 0
    
    while customerData2:
        if customerData1[position]>customerData2[0]:
            insert(customerData2[position], customerData1[0])
            position += 1

    return customerData1

if __name__ == '__main__':
    print(customerData1)