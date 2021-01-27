import requests
import json
import time

null = None
true = True
false = False

headers = {

'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100004770263&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'


comment_url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'


def get_comment(prod_id, page_num):
    response = requests.get(url=comment_url.format(prod_id, page_num), headers=headers)
    resp_text = response.text.replace('fetchJSON_comment98(', '').replace(');', '')
    resp = json.loads(resp_text)
    return resp_text, resp


def run_spider(prod_id):

    flag = True
    page_num = 1
    while flag:
        resp_text, resp = get_comment(prod_id=prod_id, page_num=page_num)

        if len(resp_text) < 4000:
            flag = False
        print(resp)
        page_num += 1


def main():
    prod_list = ['100004770263']
    for prod_id in prod_list:
        run_spider(prod_id)


if __name__ == '__main__':
    main()