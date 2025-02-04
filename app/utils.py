def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_armstrong(num: int) -> bool:
    digits = [int(digit) for digit in str(num)]
    power = len(digits)
    return sum(digit ** power for digit in digits) == num

def get_number_properties(num: int, is_armstrong_number: bool) -> list:
    if is_armstrong_number:
        return ["armstron", "even"] if num % 2 == 0 else ["armstrong", "odd"]
    return ["even"] if num % 2 == 0 else ["odd"]
