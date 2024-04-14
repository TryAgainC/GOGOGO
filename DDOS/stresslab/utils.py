import random
import string


def generate_random_string(min_length=6, max_length=8):
    # 确保最小长度不超过最大长度
    if min_length > max_length:
        raise ValueError("最小长度不能大于最大长度")

    # 定义字母表，包括大小写字母
    letters = string.ascii_letters

    # 随机选择一个在指定范围内的长度
    length = random.randint(min_length, max_length)

    # 使用random.choices()函数从字母表中随机选择指定长度的字母
    random_string = ''.join(random.choices(letters, k=length))

    return random_string
