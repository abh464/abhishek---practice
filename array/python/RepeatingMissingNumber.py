def repeating_missing_number_brute_force(arr):
    arr_length = len(arr)
    
    arr.sort()
    # print(arr)
    result = [0,0]

    for i in range(arr_length):
        if i == arr_length-1:
            break
        
        if arr[i] == arr[i+1]:
            result[0] = arr[i]
            break

    for i in range(arr_length):
        if i == arr_length-1:
            break

        if arr[i] != i+1:
            result[1] = i+1
            break
    
    return result

def repeating_missing_number_better(arr):
    arr_length = len(arr)

    result = [0,0]

    count_array = [0] * (len(arr))

    for i in range(arr_length):
        count_array[arr[i]-1]+=1
    
    for i in range(arr_length):
        if count_array[i] == 0:
            result[1] = i+1

        if count_array[i] == 2:
            result[0] = i+1

    return result

def repeating_missing_number_optimized(arr):
    arr_length = len(arr)

    result = [0,0]
    
    i = 0

    while (i< arr_length):
        if arr[i] == arr[arr[i]-1]:
            i+=1
        else:
            if arr[i] != arr[arr[i]-1]:
                arr[i],arr[arr[i]-1] = arr[arr[i]-1],arr[i]
            else:
                i+=1
    
    for i in range(arr_length):
        if arr[i] != i+1:
            result[0] = arr[i]
            result[1] = i+1;
            break
    
    return result

arr = [3,1,3]

print("Brute-force")
for i in repeating_missing_number_brute_force(arr):
    print(i)

print("Better")
for i in repeating_missing_number_better(arr):
    print(i)

print("Optimized")
for i in repeating_missing_number_optimized(arr):
    print(i)