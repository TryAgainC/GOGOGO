import random
def generate_number(num_digits=9):
    # 9位数的范围是从100,000,000到999,999,999
    range_start = 10**(num_digits - 1)
    range_end = (10**num_digits) - 1
    random_number = random.randint(range_start, range_end)
    return random_number