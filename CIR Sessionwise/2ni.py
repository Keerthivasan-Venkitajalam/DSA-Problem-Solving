def sum_of_series(n):
    total_sum=0
    for i in range(1,n+1):
        total_sum+=sum(range(1, i+1))
    return total_sum
n=int(input("Enter the value of n: "))
sum_series=sum_of_series(n)
print(f"The sum of the series is: {sum_series}")
