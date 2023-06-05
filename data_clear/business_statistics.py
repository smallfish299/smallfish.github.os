import pandas as pd

# 读取CSV文件
df = pd.read_csv('products.csv', encoding="GBK", header=None)

# 重命名列名
df.columns = ['书名', '价格', '数据', '地区']

# 将价格列转换为浮点数
df['价格'] = df['价格'].astype(float)

# 创建一个新的DataFrame，其中包含第二列价格的统计信息
price_stats = pd.DataFrame({
    '最小价格': [df['价格'].min()],
    '最大价格': [df['价格'].max()],
    '平均价格': [df['价格'].mean()]
})

# 创建一个新的DataFrame，其中包含第三列数据的统计信息
data_stats = pd.DataFrame({
    '文学作品': [df[df['数据'].astype(str).str.startswith('11')]['数据'].count()],
    '美学作品': [df[df['数据'].astype(str).str.startswith('12')]['数据'].count()],
    '艺术作品': [df[df['数据'].astype(str).str.startswith('71')]['数据'].count()],
    '其他类型': [df[~df['数据'].astype(str).str.startswith(('11', '12', '71'))]['数据'].count()]
})

# 创建一个新的DataFrame，其中包含第四列地区的统计信息
region_stats = pd.DataFrame({
    '北京': [df[df['地区'].astype(str).str.contains('北京')]['地区'].count()],
    '天津': [df[df['地区'].astype(str).str.contains('天津')]['地区'].count()],
    '广东': [df[df['地区'].astype(str).str.contains('广东')]['地区'].count()],
    '安徽': [df[df['地区'].astype(str).str.contains('安徽')]['地区'].count()],
    '其他地区': [df[~df['地区'].astype(str).str.contains(('北京', '天津', '广东', '安徽'))]['地区'].count()]
})

# 打印统计信息
print('价格统计信息：')
print(price_stats)
print('\n数据类型统计信息：')
print(data_stats)
print('\n地区统计信息：')
print(region_stats)