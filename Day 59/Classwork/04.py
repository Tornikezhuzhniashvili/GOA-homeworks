def create_phone_number(n):
    first = "(" + str(n[0]) + str(n[1]) + str(n[2]) + ")"
    second = str(n[3]) + str(n[4]) + str(n[5])
    third = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    phone_num = first + " " + second + "-" + third
    return phone_num 