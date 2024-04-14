import pandas as pd
import numpy as np

data = pd.read_excel('1.xlsx',usecols=[2],names=None)

df_li = data.values.tolist()
array = []
target = 200.00
target2 = -200.00
for s_li in df_li:
    array.append(s_li[0])

# print(array)
# for i in array:
#     for j in array:
#         if(array[i]-array[j] == target or array[i]-array[j] == target2 ) :
#             print(i+"  "+j)

# print(array)
def two_sum(nums, target):
    hashmap = {}  # 创建字典作为hash表

    for i in range(len(nums)):
        complement = target - nums[i]  # 计算目标值与当前元素的补数

        if complement in hashmap:  # 如果补数在hash表中存在
            return [hashmap[complement], i]  # 返回对应索引位置

        hashmap[nums[i]] = i  # 将当前元素及其索引添加到hash表中

    return None  # 若未找到符合条件的结果则返回None或者空列表[]

map = two_sum(array,200)


