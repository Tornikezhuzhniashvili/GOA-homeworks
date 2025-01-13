#Highest and Lowest

#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#Examples
#Input: "1 2 3 4 5" => Output: "5 1"
#Input: "1 2 -3" => Output: "2 -3"
#Input: "1 2 -39 33 11 223 -4 13" => Output: "-39 223"

def high_low(_str):
    res = _str.split(" ")
    arr = []
    for i in res:
        arr.append(int(i))

    max_num = max(arr)
    min_num = min(arr)
    return f"{max_num} {min_num}"


print(high_low("1 2 3 4 5"))
print(high_low("1 2 -3"))
print(high_low("1 2 -39 33 11 223 -4 13"))
    
    
    



