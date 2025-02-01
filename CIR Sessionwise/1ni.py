def sum_of_series(n):
    return n * (n + 1) * (2 * n + 1) // 6
n = int(input("Enter the value of n: "))
sum_series = sum_of_series(n)
print(f"The sum of the series is: {sum_series}")