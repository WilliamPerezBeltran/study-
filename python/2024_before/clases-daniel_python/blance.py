

# arr = [1,2,3,4,6]  rta =>3
# arr = [1,2,3,3]  rta =>2
# arr = [1,2,1]  rta =>1
arr = [1,2,1]

def balancedSum(arr):
    array_len = len(arr)-1
    expected_sum = arr[-1]
    acom_sum = 0
    pivote_resut = 0

    for x in range(array_len):
        acom_sum += arr[x]
        if acom_sum == expected_sum:
            pivote_resut = x
            break
    return pivote_resut + 1

print(balancedSum(arr))