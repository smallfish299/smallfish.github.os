# 按照性别 品类 地区进行分类
# 按照数据根据 适宜性别 品类 地区 进行分类
# 产品地区 11 12 13 71 代表了不同的地区
import csv

with open('products.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        # Process each row
        print(row)