import csv
import random
import requests
from lxml import etree

# 获取数据
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"
]
headers = {'User-Agent': random.choice(my_headers)}
url="https://search.jd.com/Search?keyword=%E5%9B%BE%E4%B9%A6&enc=utf-8&pvid=1743496e5f6941c99cac0342622b0c72"
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
text = res.text

# 抽取数据
selector = etree.HTML(text)
list = selector.xpath('//*[@id="J_goodsList"]/ul/li')

# 将数据写入CSV文件中
with open('products.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'price', 'product_id', 'address'])
    for i in list:
        title=i.xpath('.//div[@class="p-name p-name-type-2"]/a/em/text()')[0]
        price = i.xpath('.//div[@class="p-price"]/strong/i/text()')[0]
        product_id = i.xpath('.//div[@class="p-commit"]/strong/a/@id')[0].replace("J_comment_","")
        address = i.xpath('.//div[@class="p-shop"]/span/a/text()')
        writer.writerow([title, price, product_id, address])
