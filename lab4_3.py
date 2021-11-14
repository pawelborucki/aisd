def power(number: int, n: int) -> int:
    if n == 1:
        return number
    return number * power(number, n-1)

print(power(3,2))