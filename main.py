p_n = 0
c_n = 0
print("Printing current and previous number sum in a range(10)")
for num in range(10):
    sum = c_n + p_n
    print (f"Current Number {c_n} Previous Number {p_n}  Sum:  {sum}")
    p_n = c_n
    c_n += 1

