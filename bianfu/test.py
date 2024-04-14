import random
import string
def generate_number(num_digits=9):
    # 9位数的范围是从100,000,000到999,999,999
    range_start = 10**(num_digits - 1)
    range_end = (10**num_digits) - 1
    random_number = random.randint(range_start, range_end)
    return random_number


def generate_password():
    # 随机决定密码的前缀是两个还是三个字母
    prefix_length = random.choice([2,3])

    # 生成随机的字母前缀
    prefix = ''.join(random.choices(string.ascii_lowercase, k=prefix_length))

    # 生成5-8位的随机数字后缀
    suffix_length = random.randint(6, 8)
    suffix = ''.join(random.choices(string.digits, k=suffix_length))

    # 合并前缀和后缀，形成完整的密码
    password = prefix + suffix

    return password
