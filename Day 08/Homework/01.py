mark = int(input("How many marks did you get in the exam: "))


is_A = mark >= 9
is_B = 8 <= mark < 9
is_C = 7 <= mark < 8
is_D = 6 <= mark < 7
is_F = mark < 6

print("is_A is", is_A)
print("is_B is", is_B)
print("is_C is", is_C)
print("is_D is", is_D)
print("is_F is", is_F)

