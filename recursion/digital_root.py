def tribonacci(arr, n):  
    if len(arr) == n:
        return arr
    if n == 0:
        return []
    if n == 1:
        return [arr[0]]
    
 
    i = len(arr) - 3
    arr.append(arr[i:-1])

    return tribonacci(arr,n)