# @Time: 2023/12/13 14:43
# @Author: 李树斌
# @File : data_to_csv.py
# @Software :PyCharm
import pandas as pd
import json

# 读取JSONL文件（指定编码）
# 读取JSONL文件
jsonl_file_path = 'comment_20231213143758.jsonl'  # 替换为你的JSONL文件路径
data_list = []

with open(jsonl_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        data_list.append(data)

# 将数据转为DataFrame
df = pd.DataFrame(data_list)

# 将DataFrame写入CSV文件（指定编码）
csv_output_path = 'output_data.csv'  # 替换为你的输出CSV文件路径
df.to_csv(csv_output_path, index=False, encoding='utf-8')

# 打印成功消息
print(f'Data written to {csv_output_path}')
