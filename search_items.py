import requests
import time
from parsel import Selector
import re
from jd_comment import run_spider as get_comment  # input shopid , get response obj

headers = {

'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

keywords = ['手机']

keywd = '手机'

search_url = 'https://search.jd.com/Search?keyword={}&page={}'


if __name__ == '__main__':


    for kw in keywords:
        flag = True
        page_num = 1
        while flag:
            response = requests.get(url=search_url.format(kw, page_num), headers=headers)
            response = Selector(response.text)
            links = response.xpath('//ul[@class="gl-warp clearfix"]/li//a/@href').getall()
            for one_link in set(links):
                if 'item' in one_link:
                    print(one_link)
                    item_id = re.findall(r'\d+', one_link)
                    if item_id:
                        get_comment(item_id[0])
                    print(item_id)

            if len(links) == 0:
                flag = False
            else:
                page_num += 1


