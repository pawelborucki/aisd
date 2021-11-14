def prime(n: int) -> bool:
    if n < 2:
        return
    if n % prime(n-1):
        return False
    else:
        return prime(n-1)

print(prime(8))