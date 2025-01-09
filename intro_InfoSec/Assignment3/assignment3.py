def square_and_multiply(x, y, n):
    if x > n - 1:
        print("Invalid number.")
    
    bi_a = bin(y)[2:]
    result = 1

    for i in bi_a:
        # Square Step
        result = (result * result) % n

        # If current position is 1, do Multiply step
        if i == '1':
            result = (result * x) % n

    return print(result)

print("Sample, x = 5, y = 20, n = 35, : ")
square_and_multiply(5, 20, 35)
print("Test Case 1, x = 5, y = 13, n = 23, : ")
square_and_multiply(5, 13, 23)
print("Test Case 2, x = 12, y = 17, n = 29, : ")
square_and_multiply(12, 17, 29)
print("Test Case 3, x = 10, y = 25, n = 37, : ")
square_and_multiply(10, 25, 37)





