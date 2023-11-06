import requests
from lxml import etree
if __name__ == '__main__':
    url='https://baike.baidu.com/cms/home/eventsOnHistory/11.json?_=1699197527774'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
    page_text = requests.get(url=url,headers=headers).content
    tree = etree.HTML(page_text)
    dd_list = tree.xpath('//dl[@class="events"]//dd')
    fp = open('bd.txt','w',encoding='utf-8')
    for dd in dd_list:
        year = dd.xpath('./div@class="year"/text()')[0]
        event = dd.xpath('./div@class="event"/div@class="event_tit-wrapper"//text()')[0]
        event_tit = dd.xpath('./div@class="event"/div@class="event_tit"//text()')[0]
        print(year)
        print(event)
        print(event_tit)
        fp.write(year + '\n')
        fp.write(event + '\n')
        fp.write(event_tit + '\n')

