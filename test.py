import requests
from lxml import etree
import pymysql

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
}

res = requests.get("https://book.douban.com/tag/%E6%96%87%E5%AD%A6", headers=header)
html = etree.HTML(res.content, parser=etree.HTMLParser(encoding='utf8'))
# print(html)

book_name_ = html.xpath('//div[@class="info"]/h2/a/text()')
book_name = []
for i in book_name_:
    book_name.append(i.strip('\n '))
print(book_name)

author = []; press = []; publication_time = []; price = []
book_infos_ = html.xpath('//div[@class="pub"]/text()')
book_infos = []
for i in book_infos_:
    book_infos.append(i.strip('\n '))
for i in book_infos:
    data = i.split('/')
    author.append(data[0])
    if len(data) == 4:
        press.append(data[1])
        publication_time.append(data[2])
        price.append(data[3])
    elif len(data) == 5:
        press.append(data[2])
        publication_time.append(data[3])
        price.append(data[4])
print(author)
print(press)
print(publication_time)
print(price)

rating_nums = html.xpath('//span[@class="rating_nums"]/text()')
print(rating_nums)

rating_people_ = html.xpath('//span[@class="pl"]/text()')
rating_people = []
for i in rating_people_:
    rating_people.append(i.strip('()\n 人评价'))
print(rating_people)

book_img = html.xpath('//a[@class="nbg"]/img/@src')
print(book_img)

book_summary_ = html.xpath('//div[@class="info"]/p/text()')
book_summary = []
for i in book_summary_:
    book_summary.append(i.replace('\n',''))
print(book_summary)
print(book_summary[0])
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='1911231157',db='test',charset='utf8mb4')
cursor = conn.cursor()
for i in range(len(book_name)-1):
    book_name1 = book_name[i]
    author1 = author[i]
    rating_nums1 = rating_nums[i]
    rating_people1= rating_people[i]
    press1 = press[i]
    publication_time1 = publication_time[i]
    price1 = price[i]
    book_img1 = book_img[i]
    book_summary1 = book_summary[i]
    book_target = "文学"
    sql = "insert into app01_book_info_literature(book_name,author,rating_nums,rating_people,press,publication_time,price,book_img,book_summary,book_target) " \
          "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,[book_name1,author1,rating_nums1,rating_people1,press1,publication_time1,price1,book_img1,book_summary1,book_target])
    conn.commit()
conn.close()
cursor.close()
# print(1)