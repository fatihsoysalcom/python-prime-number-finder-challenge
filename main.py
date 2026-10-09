# This script demonstrates a common type of "DEV Challenge" problem:
# implementing a basic algorithm to solve a specific task.
# The article emphasizes problem-solving and skill development, 
# which this example aims to reflect.

def is_prime(num):
    """
    Checks if a number is prime using trial division.
    A core problem-solving step in many challenges.
    """
    if num < 2:
        return False
    # Iterate from 2 up to the square root of the number
    # This optimization is a common technique learned in challenges.
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def find_primes_up_to(limit):
    """
    Finds all prime numbers up to a given limit.
    This function represents the main task of a challenge.
    """
    primes = []
    print(f"\nStarting DEV Challenge: Find primes up to {limit}")
    for number in range(2, limit + 1):
        # Applying the 'is_prime' logic to each number
        if is_prime(number):
            primes.append(number)
            # Demonstrating progress, similar to how one might test during a challenge
            # print(f"Found prime: {number}") 
    print(f"Challenge completed! Found {len(primes)} primes.")
    return primes

if __name__ == "__main__":
    # Define the challenge parameter (e.g., the limit for prime search)
    challenge_limit = 50 

    # Execute the challenge task
    found_primes = find_primes_up_to(challenge_limit)

    print(f"\nAll prime numbers up to {challenge_limit}:")
    print(found_primes)

    # Another example to show scalability or different challenge parameters
    print("\n--- Trying another limit (e.g., a harder challenge) ---")
    found_primes_harder = find_primes_up_to(100)
    print(f"\nAll prime numbers up to 100:")
    print(found_primes_harder)
