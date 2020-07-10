def intersection(arrays):
    hash_table = {}
    result = []
    

    for sub_list in arrays:
        for number in sub_list:
            if number in hash_table:
                hash_table[number] += 1

            if number not in hash_table:
                hash_table[number] = 1
            
        for key, value in hash_table.items():
            if value == len(arrays):
                result.append(key)


        


        
    





    return result 


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
