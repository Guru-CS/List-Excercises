def check_primes_in(num):
    primes = []
    for i in range(2, num + 1):
        is_prime = True
        for j in range(2, int(i/2) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

input_num = int(input("Enter a number: "))
prime_numbers = check_primes_in(input_num)
print(f"Prime numbers up to {input_num}: {prime_numbers}")