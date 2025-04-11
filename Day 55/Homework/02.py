def even_numbers(arr,n):
    even = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
    result = even[-n:]
    return  result
            
            