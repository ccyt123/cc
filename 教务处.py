import requests
from bs4 import BeautifulSoup
from lxml import etree
if __name__ == '__main__':
    url='https://jwch.fzu.edu.cn/jxtz.htm'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
    page_text = requests.get(url=url, headers=headers).content
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="box-gl clearfix"]/ul[1]/li')
    # print(li_list)
    number = tree.xpath('//div[@class="ecms_pag"/div[1]/div[1]/span[1]/span[9]/a/text()')[0]
    # print(number)
    fp = open('教务处.txt','w',encoding='utf-8')
    notice=[]
    while 1:
        page = 0
        if page == 0:
            url = url
            page += 1
        elif page != 0:
            for page in range(number - 1)[::-1]:
                url = 'https://jwch.fzu.edu.cn/jxtz/{}.htm'.format(page)
        page_text = requests.get(url=url, headers=headers).content
        soup = BeautifulSoup(fp,'lxml')
        li_list = soup.selsct('.box_fl clearfix > ul > li')[0].text
        for page in range(number - 1)[::-1]:
            url = 'https://jwch.fzu.edu.cn/jxtz/{}.htm'.format(page)
        page_text = requests.get(url=url, headers=headers).content
        soup = BeautifulSoup(fp, 'lxml')
        li_list = soup.selsct('.box_fl clearfix > ul > li')[0].text
        for li in li_list:
            if len(notice) >= 99:
             break
        href = li.soup('. > a  >href')[0]
        detail_url = 'https://jwch.fzu.edu.cn/' + href
        detail_page_text = requests.get(url=detail_url, headers=headers).content
        detail_soup = BeautifulSoup(detail_page_text)
        detail_name = detail_soup.selsct('.w-main-dh-text > a[3]')[0].text
        detail_title = detail_soup.selsct('.wapper > form[1] > div[1] > div[1] > div[1] >div[1] > h4')[0].text
        detail_time = detail_soup.selsct('.wapper > form[1] > div[1] > div[1] > div[1] > div[2] > div[1] > span')[0].text
        notice.append(detail_title)
        fp.write(detail_url)
        fp.write(detail_name)
        fp.write(detail_title)
        fp.write(detail_time)
        fujian_list = detail_soup.selsct('.list-style-type:none; > li').text
        for fujian in fujian_list:
            fujian_title = fujian.xpath('./a/text()')[0]
            fujian_url = fujian.xpath('./a/@href')[0]
            fp.write(fujian_title)
            fp.write(fujian_url)
        print("爬取成功")
