def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        def check(num):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        if check(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a+b+c



result = sum_three(2, 3, 6)
print(result)
