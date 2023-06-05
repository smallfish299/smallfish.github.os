import pandas as pd

# 读取CSV文件
df = pd.read_csv('products.csv', encoding='GBK')

# 选择第二列并转换为数字类型
prices = pd.to_numeric(df.iloc[:, 1])

# 计算五大指标
max_price = prices.max()
min_price = prices.min()
avg_price = prices.mean()
unique_count = len(prices.unique())
total_count = len(prices)

# 生成分类图表
data = {'指标': ['最大值', '最小值', '平均值', '单个数量', '总计数量'], '价格': [max_price, min_price, avg_price, unique_count, total_count]}
df = pd.DataFrame(data)
print(df)