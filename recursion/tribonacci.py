def tribonacci(arr, n):  
    if len(arr) == n:
        return arr
    if n == 0:
        return []
    if n == 1:
        return [arr[0]]
    
    i = len(arr) - 3
    j = len(arr)

    arr.append(sum(arr[i:j]))

    return tribonacci(arr,n)

print(tribonacci([1,1,1], 10))